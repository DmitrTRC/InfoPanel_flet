import flet as ft

from src.App import InfoApp
from src.memory_store import InMemoryStore


if __name__ == '__main__':
    def main(page: ft.Page):
        """

        This method is the entry point for the InfoGraph Task Manager application. It takes a single parameter,
        'page', of type 'ft.Page'.

        :param page: an instance of the 'ft.Page' class representing the application page
        """
        page.title = 'InfoGraph Task Manager'
        page.padding = 0
        page.theme = ft.theme.Theme(
            color_scheme_seed='teal',
            font_family='Verdana'
            )
        page.theme.page_transitions.windows = 'cupertino'
        page.fonts = {
            'Pacific': '/Pacifico-Regular.ttf'
            }

        info_app = InfoApp(page, InMemoryStore())

        page.add(info_app)
        page.update()
        info_app.initialize()


    ft.app(target=main, assets_dir='../assets')
