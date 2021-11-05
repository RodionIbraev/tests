import app
import unittest
from unittest.mock import patch


class FunctionTests(unittest.TestCase):

    def test_get_doc_owner_name(self):
        num_doc = app.documents[1]['number']
        correct_res = app.documents[1]['name']
        with patch('builtins.input', return_value=num_doc):
            result = app.get_doc_owner_name()
        self.assertEqual(result, correct_res)
        with patch('builtins.input', return_value=num_doc + 'for fail'):
            result = app.get_doc_owner_name()
        self.assertEqual(result, None)


    def test_get_all_doc_owners_names(self):
        func_res = app.get_all_doc_owners_names()
        users_list = []
        for current_document in app.documents:
            doc_owner_name = current_document['name']
            users_list.append(doc_owner_name)
        for name in func_res:
            self.assertTrue(name in users_list)


    def test_delete_doc(self):
        num_doc = app.documents[1]['number']
        with patch('builtins.input', return_value=num_doc):
            result = app.delete_doc()
        self.assertTrue(result[1])
        for shelf, docs in app.directories.items():
            self.assertFalse(num_doc in docs)


    def test_show_all_docs_info(self):
        correct_result = []
        received_result = app.show_all_docs_info()
        self.assertEqual(received_result[0], 'Список всех документов:\n')
        for doc_info in received_result[1]:
            correct_result.append({"type": doc_info[0], "number": doc_info[1], "name": doc_info[2]})
        self.assertTrue(correct_result == app.documents)


    def test_get_doc_shelf(self):
        num_doc = app.directories['1'][0]
        with patch('builtins.input', return_value=num_doc):
            result = app.get_doc_shelf()
        self.assertEqual(result, '1')


    def test_add_new_doc(self):
        new_doc_number = '123'
        new_doc_type = 'pass'
        new_doc_owner_name = 'Thomas'
        new_doc_shelf_number = '3'
        new_dict_in_documents = {"type": new_doc_type, "number": new_doc_number, "name": new_doc_owner_name}
        new_element_in_directories = (new_doc_shelf_number, new_doc_number)
        with patch('builtins.input', side_effect=[new_doc_number,
                                                  new_doc_type,
                                                  new_doc_owner_name,
                                                  new_doc_shelf_number]):
            app.add_new_doc()
            self.assertTrue(new_dict_in_documents in app.documents)
            self.assertTrue(new_element_in_directories[0] in app.directories.keys() and \
                            new_element_in_directories[1] in app.directories[new_element_in_directories[0]])


    def test_move_doc_to_shelf(self):
        doc_number = app.directories['1'][0]
        shelf = '2'
        with patch('builtins.input', side_effect=[doc_number, shelf]):
            app.move_doc_to_shelf()
        self.assertTrue(doc_number not in app.directories['1'])
        self.assertTrue(doc_number in app.directories['2'])


    def test_add_new_shelf(self):
        shelf_1 = '12345'
        shelf_2 = '1'
        with patch('builtins.input', return_value=shelf_1):
            result = app.add_new_shelf()
        self.assertTrue(shelf_1 in app.directories.keys())
        self.assertTrue(result[1] and result[0] == shelf_1)
        with patch('builtins.input', return_value=shelf_2):
            result = app.add_new_shelf()
        self.assertEqual(result[1], False)



if __name__ == '__main__':
  unittest.main()