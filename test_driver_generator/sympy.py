import os


def test_one_file(test_file):
    test_file = test_file.split(".")
    test_file[-1] += ".py"
    return "try:\n\tsympy.test(\"%s\")\nexcept:\n\tpass\n" % (os.path.join("repos", "sympy", *test_file), )


def generate(test_files: list, downstream):
    test_file_content = "import sympy\n"
    for test_file in test_files:
        test_file_content += test_one_file(test_file)
    return test_file_content
