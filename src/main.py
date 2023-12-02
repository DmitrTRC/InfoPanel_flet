import flet as ft


def main(page: ft.Page) -> None:
    def btn_clicked(e):
        page.add(ft.Text('Button Clicked', color='blue'))

    t = ft.Text(value="Hello, world!", color="red")
    page.controls.append(t)
    page.add(
        ft.Row(controls=[
            ft.Text("Dmitry"),
            ft.Text("Arseniy"),
            ft.Text("Arina")
        ])
    )

    page.add(ft.ElevatedButton(text='Press button', on_click=btn_clicked))
    page.update()


ft.app(target=main)
