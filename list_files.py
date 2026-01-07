import os

def list_all_files(directory_path):
    """
    Returns a list of all files inside a directory
    and its sub-directories.
    """
    if not os.path.isdir(directory_path):
        raise FileNotFoundError("Directory does not exist")

    files = []

    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)

        if os.path.isfile(full_path):
            files.append(full_path)

        elif os.path.isdir(full_path):
            files.extend(list_all_files(full_path))  # recursion

    return files
