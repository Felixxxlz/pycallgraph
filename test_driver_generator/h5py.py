import os


def generate(test_files: list, downstream):
    test_file_content = "import h5py\nh5py.run_tests()"
    return test_file_content