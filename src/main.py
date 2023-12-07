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
            # TODO: HW3 add Switch User item
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.ACCOUNT_BOX_SHARP),
                selected_icon_content=ft.Icon(ft.icons.ACCOUNT_BOX_SHARP),
                label="Info_panel",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.ANALYTICS),
                selected_icon_content=ft.Icon(ft.icons.ANALYTICS),
                label="Backlog_api",
            ),

            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.AIR),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Weather Forecast",
                # TODO: Refactor labels to be more readable
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


ft.app(target=main, view=ft.AppView.WEB_BROWSER)

''' 
HomeTask 2
Move HW1 to separate file PopUpMenu.py
Create menu from HW1 with ft.NavigationRail class 
'''
