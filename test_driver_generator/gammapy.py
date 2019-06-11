import os


def generate(test_files: list, downstream):
    test_file_content = "import gammapy\ngammapy.test()"
    return test_file_content