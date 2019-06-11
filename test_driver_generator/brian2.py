import os


def generate(test_files: list, downstream):
    test_file_content = "import brian2\nbrian2.test()"
    return test_file_content