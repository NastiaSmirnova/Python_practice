import unittest
import md_converter as converter


class Md_converter_tests(unittest.TestCase):

    def test_prepare_md_titles(self):
        data = "# title Merge two sorted arrays\n# author smb\n# description Merge two arrays into one"
        title ='Merge two sorted arrays'
        description = 'Merge two arrays into one'

        data1 = "# title \n# author smb\n# description "
        title1 =''
        description1 = ''

        res = converter.prepare_md_titles(data)
        self.assertEqual(res, (title,description))

        res1 = converter.prepare_md_titles(data1)
        self.assertEqual(res1, (title1,description1))

    def test_prepare_md_format(self):
        title ='Merge two sorted arrays'
        description = 'Merge two arrays into one'
        source_code = 'print([0,1,2].extend([3,4,5]))'

        exp = "## Merge two sorted arrays\n\nMerge two arrays into one\n\n``` python\nprint([0,1,2].extend([3,4,5]))\n```"
        self.assertEqual(converter.prepare_md_format(title, description, source_code), exp)

    def test_prepare_md_link(self):
        title ='Task 1'
        exp = '+ [Task 1](#task-1)'
        self.assertEqual(converter.prepare_md_link(title), exp)

    def test_convert_data(self):
        content ='# title Task 1 \n# description Merge two arrays into one\n# ---end----\nprint([0,1,2].extend([3,4,5]))'
        old_c = '<!---md_file_delimeter>'
        exp = '+ [Task 1 ](#task-1)\n<!---md_file_delimeter>\n\n## Task 1 \n\nMerge two arrays into one\n\n``` python\n-\nprint([0,1,2].extend([3,4,5]))\n```'
        self.assertEqual(converter.convert_data(content, old_c), exp)
if __name__ == "__main__":
    unittest.main()