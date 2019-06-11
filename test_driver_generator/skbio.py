import os


def generate(test_files: list, downstream):
    test_file_content = "from skbio.test import pytestrunner\npytestrunner()"
    return test_file_content