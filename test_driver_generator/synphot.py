import os


def test_one_module(test_module):
    return "try:\n\tsynphot.test(package=\"%s\")\nexcept:\n\tpass\n" % (test_module, )


def generate(test_modules: list, downstream):
    test_file_content = "import synphot\n"
    for test_module in test_modules:
        test_file_content += test_one_module(test_module)
    return test_file_content
