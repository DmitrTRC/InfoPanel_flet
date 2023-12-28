import flet

from flet import (

    Column,
    Container,
    Page,
    Row,
    Text,
    UserControl,
    View,
    TemplateRoute,
    AppBar,
    PopupMenuItem,
    PopupMenuButton,
    AlertDialog,
    ElevatedButton,
    TextField,
    Icon,
    icons,
    TextAlign,
    theme,
    padding,
    margin,

    )

from app_layout import AppLayout
from board import Board
from data_store import DataStore
from memory_store import InMemoryStore
from user import User


class InfoApp(UserControl):

    def __init__(self, page: Page, store: DataStore):
        super().__init__()
        self.layout = None
        self.page = page
        self.store: DataStore = store
        self.page.on_route_change = self.route_change
        self.boards = self.store.get_boards()

        self.login_profile_button = PopupMenuItem(
            text="Log in",
            on_click=self.login
            )

        self.settings_button = PopupMenuItem(
            text="Settings",
            on_click=self.settings
            )

        self.appbar_items = [
            self.login_profile_button,
            PopupMenuItem(),  # divider
            self.settings_button,
            ]

        self.appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text(
                'Info Graph', font_family="Pacifico",
                size=32, text_align=TextAlign.START
                ),
            center_title=False,
            toolbar_height=75,
            # bgcolor=Palette.SECONDARY_VARIANT,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items,
                        ),
                    margin=margin.only(left=50, right=25),
                    )
                ],
            )

        self.page.appbar = self.appbar
        self.page.update()

    def build(self):
        self.layout = AppLayout(
            self, self.page, self.store,
            tight=True, expand=True, vertical_alignment=TextAlign.START
            )
        return self.layout

    def initialize(self):
        self.page.views.append(
            View(
                "/",
                [
                    self.appbar,
                    self.layout
                    ],
                padding=padding.all(0),
                # bgcolor=Palette.PRIMARY
                )
            )

        self.page.update()

        # create an initial board for demonstration if no boards
        if len(self.boards) == 0:
            self.create_new_board("Task Board")
        self.page.go("/")

    def login(self, e):

        def close_dlg(e):
            if user_name.value == "" or password.value == "":
                user_name.error_text = "Please provide username"
                password.error_text = "Please provide password"
                self.page.update()
                return
            else:
                user = User(user_name.value, password.value)
                if user not in self.store.get_users():
                    self.store.add_user(user)
                self.user = user_name.value
                self.page.client_storage.set("current_user", user_name.value)

            dialog.open = False
            self.appbar_items[0] = PopupMenuItem(
                text=f"{self.page.client_storage.get('current_user')}'s Profile"
                )
            self.page.update()

        user_name = TextField(label="User name")
        password = TextField(label="Password", password=True)
        dialog = AlertDialog(
            title=Text("Please enter your login credentials"),
            content=Column(
                [
                    user_name,
                    password,
                    ElevatedButton(text="Login", on_click=close_dlg),
                    ], tight=True
                ),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def settings(self, e):
        from palette import show_theme_colors

        def close_dlg(e):
            dialog.open = False
            self.page.update()

        theme_colors = show_theme_colors()

        dialog = AlertDialog(
            title=Text("Theme Colors"),
            content=Column(
                [
                    theme_colors,
                    ElevatedButton(text="Close", on_click=close_dlg),
                    ], tight=True
                ),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )

        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def route_change(self, e):
        t_route = TemplateRoute(self.page.route)

        if t_route.match("/"):
            self.page.go("/boards")
        elif t_route.match("/board/:id"):
            if int(t_route.id) > len(self.store.get_boards()):
                self.page.go("/")
                return
            self.layout.set_board_view(int(t_route.id))
        elif t_route.match("/boards"):
            self.layout.set_all_boards_view()
        elif t_route.match("/members"):
            self.layout.set_members_view()
        elif t_route.match("/weather"):
            self.layout.set_weather_view()

        self.page.update()

    def add_board(self, e):

        def close_dlg(e):
            if (hasattr(e.control, "text") and e.control.text != "Cancel") or (
                    type(e.control) is TextField and e.control.value != ""):
                self.create_new_board(dialog_text.value)
            dialog.open = False
            self.page.update()

        def textfield_change(e):
            if dialog_text.value == "":
                create_button.disabled = True
            else:
                create_button.disabled = False
            self.page.update()

        dialog_text = TextField(
            label="New Board Name",
            # color=Palette.ON_PRIMARY,
            on_submit=close_dlg,
            on_change=textfield_change
            )

        create_button = ElevatedButton(
            text="Create",
            # bgcolor=Palette.SECONDARY,
            on_click=close_dlg,
            disabled=True
            )

        dialog = AlertDialog(
            title=Text("Name your new board"),
            content=Column(
                [
                    dialog_text,
                    Row(
                        [
                            ElevatedButton(
                                text="Cancel", on_click=close_dlg
                                ),
                            create_button
                            ], alignment="spaceBetween"
                        )
                    ], tight=True
                ),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),

            )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        dialog_text.focus()

    def create_new_board(self, board_name):
        new_board = Board(self, self.store, board_name)
        self.store.add_board(new_board)
        self.layout.hydrate_all_boards_view()

    def delete_board(self, e):
        self.store.remove_board(e.control.data)
        self.layout.set_all_boards_view()


if __name__ == "__main__":
    def main(page: Page):
        page.title = "InfoGraph Task Manager"
        page.padding = 0
        page.theme = theme.Theme(
            color_scheme_seed='green',
            font_family="Verdana"
            )
        page.theme.page_transitions.windows = "cupertino"
        page.fonts = {
            "Pacifico": "/Pacifico-Regular.ttf"
            }
        # page.bgcolor = Palette.ON_BACKGROUND
        info_app = InfoApp(page, InMemoryStore())
        page.add(info_app)
        page.update()
        info_app.initialize()


    flet.app(target=main, assets_dir="../assets")
