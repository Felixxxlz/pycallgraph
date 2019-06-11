import os


def generate(test_files: list, downstream):
    test_file_content = "import numba\nnumba.test()"
    return test_file_content