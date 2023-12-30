import flet as ft
import itertools

from src.board_list import BoardList
from src.data_store import DataStore


class Board(ft.UserControl):
    id_counter = itertools.count()

    def __init__(self, app, store: DataStore, name: str):
        super().__init__()
        self.view = None
        self.board_id = next(Board.id_counter)
        self.store: DataStore = store
        self.app = app
        self.name = name
        self.add_list_button = ft.FloatingActionButton(
            icon=ft.icons.ADD, text="add a list", height=30, on_click=self.create_list
            )

        self.board_lists = [
            self.add_list_button
            ]
        for l in self.store.get_lists_by_board(self.board_id):
            self.add_list(l)

        self.list_wrap = ft.Row(
            self.board_lists,
            vertical_alignment=ft.CrossAxisAlignment.START,
            visible=True,
            scroll=ft.ScrollMode.AUTO,
            width=(self.app.page.width - 310),
            height=(self.app.page.height - 95)
            )

    def build(self):
        self.view = ft.Container(
            content=ft.Column(
                controls=[
                    self.list_wrap
                    ],

                scroll=ft.ScrollMode.AUTO,
                expand=True
                ),
            data=self,
            margin=ft.margin.all(0),
            padding=ft.padding.only(top=10, right=0),
            height=self.app.page.height,
            )

        return self.view

    def resize(self, nav_rail_extended, width, height):
        self.list_wrap.width = (
                width - 310) if nav_rail_extended else (width - 50)
        self.view.height = height
        self.list_wrap.update()
        self.view.update()

    def create_list(self, e):

        option_dict = {
            ft.colors.LIGHT_GREEN: self.color_option_creator(ft.colors.LIGHT_GREEN),
            ft.colors.RED_200: self.color_option_creator(ft.colors.RED_200),
            ft.colors.AMBER_500: self.color_option_creator(ft.colors.AMBER_500),
            ft.colors.PINK_300: self.color_option_creator(ft.colors.PINK_300),
            ft.colors.ORANGE_300: self.color_option_creator(ft.colors.ORANGE_300),
            ft.colors.LIGHT_BLUE: self.color_option_creator(ft.colors.LIGHT_BLUE),
            ft.colors.DEEP_ORANGE_300: self.color_option_creator(ft.colors.DEEP_ORANGE_300),
            ft.colors.PURPLE_100: self.color_option_creator(ft.colors.PURPLE_100),
            ft.colors.RED_700: self.color_option_creator(ft.colors.RED_700),
            ft.colors.TEAL_500: self.color_option_creator(ft.colors.TEAL_500),
            ft.colors.YELLOW_400: self.color_option_creator(ft.colors.YELLOW_400),
            ft.colors.PURPLE_400: self.color_option_creator(ft.colors.PURPLE_400),
            ft.colors.BROWN_300: self.color_option_creator(ft.colors.BROWN_300),
            ft.colors.CYAN_500: self.color_option_creator(ft.colors.CYAN_500),
            ft.colors.BLUE_GREY_500: self.color_option_creator(ft.colors.BLUE_GREY_500),
            }

        def set_color(e):
            color_options.data = e.control.data
            for k, v in option_dict.items():
                if k == e.control.data:
                    v.border = ft.border.all(3, ft.colors.BLACK26)
                else:
                    v.border = None
            dialog.content.update()

        color_options = ft.GridView(
            runs_count=3, max_extent=40, data="", height=150
            )

        for _, v in option_dict.items():
            v.on_click = set_color
            color_options.controls.append(v)

        def close_dlg(e):
            if (hasattr(e.control, "text") and e.control.text != "Cancel") or (
                    type(e.control) is ft.TextField and e.control.value != ""):
                new_list = BoardList(
                    self, self.store, dialog_text.value,
                    color=color_options.data
                    )
                self.add_list(new_list)
            dialog.open = False
            self.page.update()
            self.update()

        def textfield_change(e):
            if dialog_text.value == "":
                create_button.disabled = True
            else:
                create_button.disabled = False
            self.page.update()

        dialog_text = ft.TextField(
            label="New List Name",
            on_submit=close_dlg, on_change=textfield_change
            )
        create_button = ft.ElevatedButton(
            text="Create", bgcolor=ft.colors.BLUE_200, on_click=close_dlg, disabled=True
            )
        dialog = ft.AlertDialog(
            title=ft.Text("Name your new list"),
            content=ft.Column(
                [
                    ft.Container(
                        content=dialog_text,
                        padding=ft.padding.symmetric(horizontal=5)
                        ),
                    color_options,
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                text="Cancel", on_click=close_dlg
                                ),
                            create_button
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        )
                    ], tight=True, alignment=ft.MainAxisAlignment.CENTER
                ),

            on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        dialog_text.focus()

    def remove_list(self, b_list: BoardList, e):
        self.board_lists.remove(b_list)
        self.store.remove_list(self.board_id, list.board_list_id)
        self.update()

    def add_list(self, list: BoardList):
        self.board_lists.insert(-1, list)
        self.store.add_list(self.board_id, list)

    def color_option_creator(self, color: str):
        return Container(
            bgcolor=color,
            border_radius=border_radius.all(50),
            height=10,
            width=10,
            padding=padding.all(5),
            alignment=alignment.center,
            data=color
            )
