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
    
    def test_all_doc_owners(self):
        test_list = []
        for entry in main.documents:
            owner = entry['name']
            test_list.append(owner)
        test_list = set(test_list)
        self.assertSetEqual(main.get_all_doc_owners_names(), test_list)
    
    def test_delete_doc_shelf(self):
        testing_pool = ('1006', '2207 876234', None, 'fgsfds', True)
        for test_entry in testing_pool:
            with self.subTest(test_entry=test_entry):
                directories = main.directories.copy()
                for key, directory in directories.items():
                    if test_entry in directory:
                        directory.remove(test_entry)
                main.remove_doc_from_shelf(test_entry)
                self.assertDictEqual(main.directories, directories)
    
    def test_add_new_shelf(self):
        
            