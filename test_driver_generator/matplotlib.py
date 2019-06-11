import os


def test_one_module(test_file):
    return "try:\n\tmatplotlib.test(argv=[\"%s\"])\nexcept:\n\tpass\n" % (test_file, )


def generate(test_files: list, downstream):
    test_file_content = "import matplotlib\n"
    for test_file in test_files:
        test_file_content += test_one_module(test_file)
    return test_file_content
