import os


def test_one_module(test_file):
    spl_file = test_file.split(".")
    spl_file[-1] += ".py"
    test_file = "/".join(spl_file)
    return "try:\n\tpytest.main([\"/usr/local/lib/python3.6/dist-packages/%s\"])\nexcept:\n\tpass\n" % (test_file, )


def generate(test_files: list, downstream):
    test_file_content = "import pytest\n"
    for test_file in test_files:
        test_file_content += test_one_module(test_file)
    return test_file_content
