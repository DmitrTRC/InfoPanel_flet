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