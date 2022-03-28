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
    
    def test_delete_doc_from_shelf(self):
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
        testing_pool = [
            ('4', True),
            ('5', True),
            ('3', False),
            ('1', False)
        ]
        for test_entry in testing_pool:
            with self.subTest(test_entry=test_entry):
                self.assertEqual(main.add_new_shelf(test_entry[0]), test_entry)
    
    def test_append_doc_to_shelf(self):
        testing_pool = [
            ('1008', '2'),
            ('12345', '3)'),
            ('12qw43', '7'),
            ('6543', '4')
        ]
        for test_entry in testing_pool:
            with self.subTest(test_entry=test_entry):
                main.append_doc_to_shelf(test_entry[0], test_entry[1])
                self.assertIn(test_entry[0], main.directories[test_entry[1]])
    
    @patch('builtins.input', side_effect = ['2207 876234', 'asdf', 'fgsfds'])
    def test_delete_doc(self, mock_input):
        testing_results = [True, None, None]
        for result in testing_results:
            with self.subTest(result=result):
                returned_value = main.delete_doc()
                if returned_value is None:
                    self.assertEqual(returned_value, result)
                else:
                    self.assertEqual(returned_value[1], result)
    
    @patch('builtins.input', side_effect = ['11-2', '10006', 'qwer', '5'])
    def test_get_doc_shelf(self, mock_input):
        estimated_results = ['1', '2', None, None]
        for result in estimated_results:
            with self.subTest(result=result):
                self.assertEqual(main.get_doc_shelf(), result)
    
    @patch('builtins.input', side_effect = ['11-2', '3', '5455 028765', '3'])
    def test_move_doc_to_shelf(self, mock_input):
        check_pool = [
            ('11-2', '3'),
            ('5455 028765', '3')
        ]
        for pair in check_pool:
            with self.subTest(pair=pair):
                main.move_doc_to_shelf()
                self.assertIn(pair[0], main.directories[pair[1]])
    
    @patch('builtins.input', side_effect = [
        '12345', 'passport', 'Петр Сидоров', '0',
        '2365 4321', 'driver license', 'Федор Пупкин', '1',
        '5423', 'insurance', 'Иван Пивохлебов', '2'
        ])
    def test_add_new_doc(self, mock_input):
        check_pool = [
        {'type': 'passport', 'number': '12345', 'name': 'Петр Сидоров'},
        {'type': 'driver license', 'number': '2365 4321', 'name': 'Федор Пупкин'},
        {'type': 'insurance', 'number': '5423', 'name': 'Иван Пивохлебов'}
        ]
        for number, person_data in enumerate(check_pool):
            with self.subTest(person_data=person_data, number=number):
                result = main.add_new_doc()
                self.assertEqual(result, str(number))
                self.assertIn(person_data, main.documents)
    