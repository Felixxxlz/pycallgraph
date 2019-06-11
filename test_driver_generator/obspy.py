import os


def generate(test_files: list, downstream):
    test_file_content = "import obspy\nobspy.core.run_tests()"
    return test_file_content