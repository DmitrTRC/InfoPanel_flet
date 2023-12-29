import flet as ft

from src.app_layout import AppLayout
from src.board import Board
from src.data_store import DataStore
from src.memory_store import InMemoryStore
from src.user import User


class InfoApp(ft.UserControl):
    """
    This class represents an application that provides information using a graphical user interface. It inherits from
    the ft.UserControl class.

    Attributes:
    - layout (None): The layout of the application.
    - page (ft.Page): An instance of the Page class representing the page associated with this application.
    - store (DataStore): An instance of the DataStore class representing the data store used by this application.
    - boards (list): A list of boards available in the data store.
    - login_profile_button (ft.PopupMenuItem): A button for logging in.
    - settings_button (ft.PopupMenuItem): A button for accessing settings.
    - appbar_items (list): A list of appbar items.
    - appbar (ft.AppBar): The appbar of the application.
    """

    def __init__(self, page: ft.Page, store: DataStore):
        """

        :param page: an instance of the Page class
        :param store: an instance of the DataStore class

        Initializes an instance of the __init__ method.

        This method sets up the layout, page, store, and event handlers for the page. It also initializes the appbar
        items and sets up the appbar.

        The page parameter is an instance of the Page class. It represents the page that this instance of the method
        is associated with.

        The store parameter is an instance of the DataStore class. It represents the data store that this instance of
        the method uses.

        No return value.

        """
        super().__init__()
        self.layout = None
        self.page = page
        self.store: DataStore = store
        self.page.on_route_change = self.route_change
        self.boards = self.store.get_boards()

        self.login_profile_button = ft.PopupMenuItem(
            text='Log in',
            on_click=self.login
            )

        self.settings_button = ft.PopupMenuItem(
            text='Settings',
            on_click=self.settings
            )

        self.appbar_items = [
            self.login_profile_button,
            ft.PopupMenuItem(),  # divider
            self.settings_button,
            ]

        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=ft.Text(
                'Info Graph', font_family='Pacifico',
                size=32, text_align=ft.TextAlign.START
                ),
            center_title=False,
            toolbar_height=75,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=self.appbar_items,
                        ),
                    margin=ft.margin.only(left=50, right=25),
                    )
                ],
            )

        self.page.appbar = self.appbar
        self.page.update()

    def build(self):
        """
        Builds the layout of the application.

        :returns: the built layout
        """
        self.layout = AppLayout(
            self, self.page, self.store,
            tight=True, expand=True, vertical_alignment=ft.TextAlign.START
            )
        return self.layout

    def initialize(self):
        """Initializes the software application.

        This method initializes the software application by performing the following steps:
        - Appending the appbar and layout to the list of views in the `page` object.
        - Setting the padding of the views to 0.
        - Updating the `page` object.
        - Creating a new board with the name 'Task Board' if no boards exist.
        - Redirecting the page to the home directory ('/').

        Parameters:
            self: The object instance.

        Returns:
            None
        """
        self.page.views.append(
            ft.View(
                '/',
                [
                    self.appbar,
                    self.layout
                    ],
                padding=ft.padding.all(0),
                )
            )

        self.page.update()

        # create an initial board for demonstration if no boards
        if len(self.boards) == 0:
            self.create_new_board('Task Board')
        self.page.go('/')

    def login(self, e):
        """
        Login method

        This method opens a modal dialog to allow the user to login. It takes an event object as a parameter.

        Parameters:
        - e: The event object triggered by the login action.

        Returns:
        None

        Example usage:
        app.login(e)

        """

        def close_dlg(e):
            """

            Close the Dialog on Login

            This method is used to close the dialog after the user has successfully logged in. It updates the
            necessary components and displays the user's profile name in the app bar.

            Parameters:
            - e: The event object that triggered the method (not used)

            Returns:
            This method does not return anything.

            """
            if user_name.value == '' or password.value == '':
                user_name.error_text = 'Please provide username'
                password.error_text = 'Please provide password'
                self.page.update()
                return
            else:
                user = User(user_name.value, password.value)
                if user not in self.store.get_users():
                    self.store.add_user(user)
                self.user = user_name.value
                self.page.client_storage.set('current_user', user_name.value)

            dialog.open = False
            self.appbar_items[0] = ft.PopupMenuItem(
                text=f"{self.page.client_storage.get('current_user')}'s Profile"
                )
            self.page.update()

        user_name = ft.TextField(label='User name')
        password = ft.TextField(label='Password', password=True)
        dialog = ft.AlertDialog(
            title=ft.Text('Please enter your login credentials'),
            content=ft.Column(
                [
                    user_name,
                    password,
                    ft.ElevatedButton(text='Login', on_click=close_dlg),
                    ], tight=True
                ),
            on_dismiss=lambda event: print('Modal dialog dismissed!'),
            )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def settings(self, e):
        """
        Open theme colors settings dialog.

        :param e: The event object.
        """
        from src.palette import show_theme_colors

        def close_dlg(e):
            """
            Closes the dialog window.

            Parameters:
            e (Event): The event object.

            Returns:
            None

            Example:
            # Create an instance of the InfoApp class
            app = InfoApp()

            # Call the close_dlg method passing an event object
            app.close_dlg(event)
            """
            dialog.open = False
            self.page.update()

        theme_colors = show_theme_colors()

        dialog = ft.AlertDialog(
            title=ft.Text('Theme Colors'),
            content=ft.Column(
                [
                    theme_colors,
                    ft.ElevatedButton(text='Close', on_click=close_dlg),
                    ], tight=True
                ),
            on_dismiss=lambda e: print('Modal dialog dismissed!'),
            )

        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def route_change(self, e):
        """
        Changes the route of the page and updates the layout accordingly.

        Args:
            e: The event object.

        Returns:
            None
        """
        t_route = ft.TemplateRoute(self.page.route)

        if t_route.match('/'):
            self.page.go('/boards')
        elif t_route.match('/board/:id'):
            if int(t_route.id) > len(self.store.get_boards()):
                self.page.go('/')
                return
            self.layout.set_board_view(int(t_route.id))
        elif t_route.match('/boards'):
            self.layout.set_all_boards_view()
        elif t_route.match('/members'):
            self.layout.set_members_view()
        elif t_route.match('/weather'):
            self.layout.set_weather_view()

        self.page.update()

    def add_board(self, e):
        """
        This method `add_board` is used to add a new board to the system.

        Parameters:
        - `self`: This parameter refers to the instance of the object calling the method.
        - `e`: This parameter represents the event object.

        Returns:
        - None

        Example Usage:
        ```python
        add_board(self, e)
        ```

        """

        def close_dlg(e):
            """

            Close the dialog

            Parameters:
            - e: Event object

            Returns:
            None

            """
            if (hasattr(e.control, 'text') and e.control.text != 'Cancel') or (
                    type(e.control) is ft.TextField and e.control.value != ''):
                self.create_new_board(dialog_text.value)
            dialog.open = False
            self.page.update()

        def textfield_change(e):
            """
            Method to trigger when the text field value changes.

            :param e: The event object representing the change event.
            :type e: Event

            :return: None
            """
            if dialog_text.value == '':
                create_button.disabled = True
            else:
                create_button.disabled = False
            self.page.update()

        dialog_text = ft.TextField(
            label='New Board Name',
            on_submit=close_dlg,
            on_change=textfield_change
            )

        create_button = ft.ElevatedButton(
            text='Create',
            on_click=close_dlg,
            disabled=True
            )

        dialog = ft.AlertDialog(
            title=ft.Text('Name your new board'),
            content=ft.Column(
                [
                    dialog_text,
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                text='Cancel', on_click=close_dlg
                                ),
                            create_button
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ], tight=True
                ),
            on_dismiss=lambda e: print('Modal dialog dismissed!'),

            )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        dialog_text.focus()

    def create_new_board(self, board_name):
        """
        Create a new board with the given name.

        Parameters:
            board_name (str): The name of the new board.

        Returns:
            None
        """
        new_board = Board(self, self.store, board_name)
        self.store.add_board(new_board)
        self.layout.hydrate_all_boards_view()

    def delete_board(self, e):
        """
        Delete board from the store and update the view layout.

        Parameters:
        - e: The event object containing the board to delete.

        Return:
        None
        """
        self.store.remove_board(e.control.data)
        self.layout.set_all_boards_view()
