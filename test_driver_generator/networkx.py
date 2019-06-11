import os


def generate(test_files: list, downstream):
    test_file_content = "import networkx\nnetworkx.test()"
    return test_file_content