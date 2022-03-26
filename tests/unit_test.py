import unittest
from unittest.mock import patch
import main

class BasicTester(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_existance(self):
        testing_pool = [
            ('10006', True),
            ('11-2', True),
            ('ASDF', False),
            ('zxc', False)
        ]
        for pair in testing_pool:
            with self.subTest(pair=pair):
                self.assertIs(main.check_document_existance(pair[0]), pair[1])

    @patch('builtins.input', side_effect = ['11-2', '10006', 'asdf', None])
    def test_owner_check(self, mock_input):
        testing_pool = ['Геннадий Покемонов', 'Аристарх Павлов', None , None]
        for item in testing_pool:
            with self.subTest(item=item):
                self.assertEqual(main.get_doc_owner_name(), item)