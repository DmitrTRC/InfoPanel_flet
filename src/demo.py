import flet as ft


def main(page: ft.Page) -> None:
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_todo_task.value))
        new_todo_task.value = ""
        new_todo_task.focus()
        new_todo_task.update()

    new_todo_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_todo_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    for i in range(4):
        page.add(ft.Checkbox(label=f'Task number {i}'))

    page.update()


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
