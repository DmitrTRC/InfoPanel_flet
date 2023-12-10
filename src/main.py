import flet as ft

from NaviBarApp import NaviBarApp


def main(page: ft.Page):
    rail = NaviBarApp(page)
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


ft.app(target=main)
