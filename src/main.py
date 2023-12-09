import flet as ft

from NaviBarApp import NaviBarApp



def main(page: ft.Page):
    rail = NaviBarApp(page).build()
    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=200),
            ],
            expand=True,
        )
    )

    page.bgcolor = '#191C1A'

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()



ft.app(target=main)
