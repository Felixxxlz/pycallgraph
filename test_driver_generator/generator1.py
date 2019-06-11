import os


def convert_downstream_to_repo_dir(repo: str):
    if repo == "sklearn":
        repo = "scikit-learn"
    elif repo == "skbio":
        repo = "scikit-bio"
    elif repo == "tables":
        repo = "PyTables"
    elif repo == "astropy_helpers":
        repo = "astropy-helpers"
    elif repo == "radio_beam":
        repo = "radio-beam"
    elif repo == "nrrd":
        repo = "pynrrd"
    elif repo == "synphot":
        repo = "synphot_refactor"
    elif repo == "dicom_numpy":
        repo = "dicom-numpy"
    elif repo == "json_tricks":
        repo = "pyjson_tricks"
    elif repo == "numpy_buffer":
        repo = "numpy-buffer"
    elif repo == "tgan":
        repo = "TGAN"
    elif repo == "skopt":
        repo = "scikit-optimize"
    elif repo == "scikitplot":
        repo = "scikit-plot"
    elif repo == "profanity_check":
        repo = "profanity-check"
    elif repo == "sklearn_evaluation":
        repo = "sklearn-evaluation"
    elif repo == "sklearn_lvq":
        repo = "sklearn-lvq"
    elif repo == "astropy_healpix":
        repo = "astropy-healpix"
    elif repo == "coinsta":
        repo = "Coinsta"
    elif repo == "oommftools":
        repo = "OOMMFTools"
    elif repo == "pyrr":
        repo = "Pyrr"
    elif repo == "pyxrd":
        repo = "PyXRD"
    elif repo == "randnla":
        repo = "randNLA"
    elif repo == "utide":
        repo = "UTide"
    elif repo == "pvmismatch":
        repo = "PVMismatch"
    return repo


def test_one_module(test_file, repo_dir):
    spl_file = test_file.split(".")
    spl_file[-1] += ".py"
    test_file = "/".join(spl_file)
    return "try:\n\tpytest.main([\"repos/%s/%s\"])\nexcept:\n\tpass\n" % (repo_dir, test_file)


def generate(test_files: list, downstream):
    repo_dir = convert_downstream_to_repo_dir(downstream)
    test_file_content = "import pytest\n"
    for test_file in test_files:
        test_file_content += test_one_module(test_file, repo_dir)
    return test_file_content
