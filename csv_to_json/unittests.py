import unittest
from converter_csv_json import converter_csv_json

class Test(unittest.TestCase):
    def setUp(self):
        self.converter_csv_json = converter_csv_json()
    def test_title(self):
        data= ['1','2','3']
        title, data =  self.converter_csv_json.prepare_data(data)
        self.assertEqual(title, ['1'])

    def test_empty_data(self):
        data= ['id,name,birth,salary,department\n']
        result = self.converter_csv_json.convert_csv_to_json(data)
        self.assertEqual(result, '[]')

    def test_passes(self):
         title=['id', 'name', 'birth', 'salary', 'department']
         data = '3,,,,8'
         result =self.converter_csv_json.convert_row_to_pretty_json(title, data)
         print(result)

         self.assertEqual(result, '{\n    "id": 3,\n    "name": ,\n    "birth": ,\n    "salary": ,\n    "department": 8\n        }')
    def test_valid_data(self):
         title=['id', 'name', 'birth', 'salary', 'department']
         data = '3,Igor,1999,200000,8'
         result =self.converter_csv_json.convert_row_to_pretty_json(title, data)
         print(result)

         self.assertEqual(result, '{\n    "id": 3,\n    "name": Igor,\n    "birth": 1999,\n    "salary": 200000,\n    "department": 8\n        }')    
if __name__ == "__main__":
    unittest.main()
