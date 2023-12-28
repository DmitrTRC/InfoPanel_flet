import unittest
from unittest.mock import Mock

# Make sure to import your actual InfoApp class
from src.main import InfoApp, ft, DataStore


class TestInfoApp(unittest.TestCase):

    # Optional: Setup and Teardown
    def setUp(self):
        self.page = Mock(spec=ft.Page)
        self.store = Mock(spec=DataStore)
        self.info_app = InfoApp(self.page, self.store)

    def tearDown(self):
        # TODO document why this method is empty
        pass

    def test_initialize(self):
        self.info_app.initialize()
        # Assert statements as necessary

    def test_login(self):
        mock_event = Mock()
        self.info_app.login(mock_event)
        # Assert statements as necessary

    def test_settings(self):
        mock_event = Mock()
        self.info_app.settings(mock_event)
        # Assert statements as necessary

    def test_route_change(self):
        mock_event = Mock()
        self.info_app.route_change(mock_event)
        # Assert statements as necessary

    def test_add_board(self):
        mock_event = Mock()
        self.info_app.add_board(mock_event)
        # Assert statements as necessary

    def test_create_new_board(self):
        board_name = 'Test Board'
        self.info_app.create_new_board(board_name)
        # Assert statements as necessary

    def test_delete_board(self):
        mock_event = Mock()
        self.info_app.delete_board(mock_event)
        # Assert statements as necessary


if __name__ == '__main__':
    unittest.main()
