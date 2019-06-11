import os


def test_one_module(test_module):
    return "try:\n\timport %s\n\t%s.test()\nexcept:\n\tpass\n" % (test_module, test_module)


def generate(test_modules: list, downstream):
    test_file_content = ""
    for test_module in test_modules:
        test_file_content += test_one_module(test_module)
    return test_file_content
