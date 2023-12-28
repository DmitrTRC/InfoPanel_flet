import flet as ft

from flet import UserControl


class NaviBarApp(UserControl):

    def __init__(self, page):
        super().__init__()
        self.rail = None
        self.page = page
        self.view = None

    def menu_choice_manager(self, message):
        print(f'Selected destination: {message.control.selected_index}')
        match message.control.selected_index:
            case 0:
                print("Info Panel")
            case 1:
                print("Change User")
            case 2:
                print("Task Manager")
            case 3:
                print("Weather forecast ")

        return message.control.selected_index
        # TODO: Implement reaction for each menu item ( try to use Python match )

    def build(self):
        self.initialize()
        self.view = ft.Row(
            [
                self.rail,
                ft.VerticalDivider(width=200),
                ],
            expand=True
            )

        return self.view

    def initialize(self):
        self.rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
            group_alignment=-0.9,
            bgcolor='#1A2520',
            destinations=[
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.ACCOUNT_BOX_SHARP),
                    selected_icon_content=ft.Icon(ft.icons.ACCOUNT_BOX_SHARP),
                    label="Info Panel",
                    ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.SUPERVISED_USER_CIRCLE),
                    selected_icon_content=ft.Icon(ft.icons.SUPERVISED_USER_CIRCLE),
                    label="Change User",
                    ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.ANALYTICS),
                    selected_icon_content=ft.Icon(ft.icons.ANALYTICS),
                    label="Task Manager",
                    ),

                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.AIR),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                    label="Weather Forecast",
                    ),
                ],
            on_change=self.menu_choice_manager
            # TODO: HW4 Replace lambda expression to method menu_choice_manager()
            )
