import unittest
from unittest.mock import mock_open, patch

def file_parser(file_path, find_str, replace_str=None):
    with open(file_path, 'r') as file:
        content = file.read()
        if replace_str:
            new_content = content.replace(find_str, replace_str)
            with open(file_path, 'w') as file:
                file.write(new_content)
            return f"Replaced {content.count(find_str)} strings"
        else:
            return f"Found {content.count(find_str)} strings"

class ParserTest(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='hello world hello')
    def test_file_parser_count(self, mock_file):
        result = file_parser('file.txt', 'hello')
        self.assertEqual(result, "Found 2 strings")
        mock_file.assert_called_with('file.txt', 'r')

    @patch('builtins.open', new_callable=mock_open, read_data='hello world hello')
    def test_file_parser_replace(self, mock_file):
        result = file_parser('file.txt', 'hello', 'world')
        self.assertEqual(result, "Replaced 2 strings")


if __name__ == '__main__':
    unittest.main()