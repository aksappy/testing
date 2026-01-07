import os
import unittest
from list_files import list_all_files

class TestListAllFiles(unittest.TestCase):

    def setUp(self):
        self.test_directory = os.getcwd()  # current "testing" folder

    def test_directory_exists(self):
        self.assertTrue(os.path.isdir(self.test_directory))

    def test_function_returns_list(self):
        result = list_all_files(self.test_directory)
        self.assertIsInstance(result, list)

    def test_main_directory_files_present(self):
        result = list_all_files(self.test_directory)
        self.assertTrue(any("fibannocci" in f for f in result))

    def test_subdirectory_files_present(self):
        result = list_all_files(self.test_directory)
        self.assertTrue(any("new.py" in f for f in result))

    def test_directories_not_in_result(self):
        result = list_all_files(self.test_directory)
        for item in result:
            self.assertTrue(os.path.isfile(item))


if __name__ == "__main__":
    unittest.main()
