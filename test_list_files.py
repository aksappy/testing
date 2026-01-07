import os
import unittest
from list_files import list_all_files

class TestListAllFiles(unittest.TestCase):

    def setUp(self):
        self.test_directory = os.getcwd()  # current "testing" folder

# Check if the current working directory exists and is a valid directory.
    def test_directory_exists(self): 
        self.assertTrue(os.path.isdir(self.test_directory))

# Check if the function returns a list.
    def test_function_returns_list(self):
        result = list_all_files(self.test_directory)
        self.assertIsInstance(result, list)

# Check if the files present in the main directory are included in the result.
    def test_main_directory_files_present(self):
        result = list_all_files(self.test_directory)
        self.assertTrue(any("fibannocci" in f for f in result))

# Check if the files inside the sub-dirctories are found.
    def test_subdirectory_files_present(self):
        result = list_all_files(self.test_directory)
        self.assertTrue(any("new.py" in f for f in result))

# Verify that only files are returned but not the directory paths.
    def test_directories_not_in_result(self):
        result = list_all_files(self.test_directory)
        for item in result:
            self.assertTrue(os.path.isfile(item))


if __name__ == "__main__":
    unittest.main()
