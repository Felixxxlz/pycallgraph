import os


def generate(test_files: list, downstream):
    test_file_content = "import tables\ntables.test(heavy=True)"
    return test_file_content