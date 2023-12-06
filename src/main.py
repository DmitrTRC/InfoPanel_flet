import flet as ft


def main(page: ft.Page):
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        bgcolor='#1A2520',
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )

    page.bgcolor = '#191C1A'

    ''' Implement menu with items [ Switch User, Info Panel, Tasks, Weather Forecast ]
        Implement simple handler ( writing which item clicked )
        
        '''
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    pb = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(
                text="InfoPanel", checked=False, on_click=print('info')
            ),
            ft.PopupMenuItem(
                text="BacklogApi", checked=False, on_click=print('info')
            ),
            ft.PopupMenuItem(
                text="Weather forecast", checked=False, on_click=print('Weather forecast')
            )
                ,

            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Icon(ft.icons.HOURGLASS_TOP_OUTLINED),

                    ]
                ),
                on_click=lambda _: print("Button with a custom content clicked!"),
            ),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(
                text="Checked item", checked=False, on_click=check_item_clicked
            ),
        ]
    )
    page.add(pb)

ft.app(target=main)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
