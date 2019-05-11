# import pytest
# import astropy
# import numba
# import pandas
# import theano
# import scipy as sp
# import matplotlib
# import tables
# import sympy
# import networkx
# import statsmodels.api as sm
# import obspy
# import gammapy
# import h5py
# from skbio.test import pytestrunner
# import ccdproc
# import numexpr
# import photutils
# import asdf
# import poppy
# import bottleneck as bn
# import pyregion
# import brian2
# import radio_beam
# import verde
# import astroimtools
# import stginga
# import synphot
# import pydl
from subprocess import Popen, PIPE
import os
import tqdm
import csv
import subprocess


def main():
    # pandas.test()
    # h5py.run_tests()
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/joblib"])
    # numexpr.test()
    # brian2.test()
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/pyjet"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/deap"])
    # tables.test(heavy=True)
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/shared_ndarray"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/nrrd"])
    # bn.test()
    # pytest.main(["./REPOS/Pyrr"])
    # pytest.main(["./REPOS/hienoi"])
    # pytest.main(["./REPOS/nnlib"])
    # pytest.main(["./REPOS/kravatte"])
    # pytest.main(["./REPOS/geometer"])
    # pytest.main(["./REPOS/zappy"])
    # pytest.main(["./REPOS/gfmm"])
    # pytest.main(["./REPOS/tidynamics"])
    # pytest.main(["./REPOS/texpy"])
    # pytest.main(["./REPOS/randNLA"])
    # pytest.main(["./REPOS/pyik"])
    # pytest.main(["./REPOS/dicom-numpy"])
    # pytest.main(["./REPOS/numpy-buffer"])
    # pytest.main(["./REPOS/slugnet"])
    # asdf.test()
    # pyregion.test()
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/atpy"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/gwcs"])
    # radio_beam.test()
    # synphot.test()
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/mpmath"])
    # pytest.main(["./REPOS/indi"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/numbagg"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/patsy"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/nptdms"])
    # pytest.main(["./REPOS/pytablewriter"])
    # pytest.main(["./REPOS/phildb"])
    # pytest.main(["./REPOS/espandas"])
    # pytest.main(["./REPOS/validada"])
    # pytest.main(["./REPOS/partridge"])
    # pytest.main(["./REPOS/pyjson_tricks"])
    # pytest.main(["./REPOS/datacompy"])
    # pytest.main(["./astropy-helpers"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/aplpy"])
    # theano.test()
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/pyamg"])
    # numba.test()
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/mahotas"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/randomgen"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/sparse"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/cvxpy"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/oct2py"])
    # pytest.main(["./REPOS/PVMismatch"])
    # pytest.main(["./REPOS/UTide"])
    # pytest.main(["./REPOS/npstreams"])
    # pytest.main(["./REPOS/PyXRD"])
    # pytest.main(["./REPOS/OOMMFTools"])
    # pytest.main(["./REPOS/pdepy"])
    # pytest.main(["./REPOS/psopy"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/sklearn"])
    # pytest.main(["./REPOS/molml"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/ibis"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/plydata"])
    # stginga.test()
    # astroimtools.test()
    # ccdproc.test()
    # sympy.utilities.runtests.test(subprocess=False)
    # pytest.main(["./REPOS/deepgraph"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/starfish"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/alphalens"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/dask"])
    # pydl.test()
    # poppy.test()
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/naima"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/specutils"])
    # photutils.test()
    # pytest.main(["./REPOS/lens"])
    # networkx.test()
    # obspy.core.run_tests()
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/pymc3"])
    # sm.test()
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/seaborn"])
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/xarray"])
    # pytest.main(["./REPOS/feets"])
    # pytest.main(["./REPOS/prince"])
    # verde.test()
    # pytestrunner()
    # pytest.main(["/usr/local/lib/python3.6/dist-packages/nilearn"])
    # sp.test()
    # gammapy.test()
    # astropy.test()
    # matplotlib.test()
    numpy_versions = [
    "9ae4f9bae9344ee0f1ca4d5767e49c196d534efc", "c4a840ed97f67cfdc7c5d8a04512cdc86098dff0",
    "a72f061ede7cf2058829668a4f5d110dec265f1c", "2f2dfa19839d69a20713b2fe05ca1ca35f6454a7", 
    "a090e46b9e3b5046f08e46b08df103d00985e47c", "25b5273834c73bb278a4741aad5ade4ad705f209",
    "ca5658bb0e63030011d8a0f30815b34f4dc6dc8a", "ba734f3160419771f82bb1f45c60d4871f2efd72", 
    "5e9c419a6d41eb9d544b6d87dd621ad5b346a0fa", "d89c4c7e7850578e5ee61e3e09abd86318906975",
    "632afad440193271535a33a89bc3e19c3ecc291c", "0c3c04ebc1f9b038ebc75b1dc0b46437accb3e7f",
    "81f0ddac64919e503beeea2c1812b36a607de55d", "d6dcaedad22f5842e28179351238b4847e74d5a9",
    "e6147b9bf580361f2f74ac72003f81e957587528", "f297d317f9d2355228fb3a265e9ff3c69e37b1e2"][5:] # 别忘记安装对应版本的numpy环境
    for numpy_version in numpy_versions:
        os.chdir(os.path.join("..", "REPOS", "numpy"))
        p = Popen(["git", "checkout", "master"])
        p.wait()
        p = Popen(["git", "checkout", numpy_version])
        p.wait()
        p = Popen("sudo -S pip3 install .", shell=True, stdin=PIPE)
        p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))
        p.wait()
        os.chdir(os.path.join("..", "..", "pycallgraph"))

        downstream_test_pyfiles = os.listdir("test_numpy")
        ok = set()
        with open(os.path.join("results", "numpy", numpy_version + ".csv"), encoding="gbk") as rf:
            reader = csv.reader(rf)
            next(reader)
            for row in reader:
                if int(row[4]):
                    ok.add(row[1])
        numpy_version = numpy_version[:7]
        try:
            os.makedirs(os.path.join("test_logs", "numpy", numpy_version))
        except:
            pass
        for downstream_test_pyfile in tqdm.tqdm(downstream_test_pyfiles):
            downstream_name = "_".join(downstream_test_pyfile.split('.')[0].split("_")[1:])
            if downstream_name not in ok:
                continue
            if downstream_name == "alphalens":
                continue
            if downstream_name == "joblib":
                continue
            if downstream_name == "dask":
                continue
            if downstream_name == "numpy_buffer":
                continue
            if downstream_name == "indi":
                continue
            print(downstream_name)
            pyfile_path = os.path.join("test_numpy", downstream_test_pyfile)
            with open(os.path.join("test_logs", "numpy", numpy_version, \
                "test_log_" + downstream_name + ".txt"), mode="w") as wf:
                p = Popen(["python3", pyfile_path], stdout=wf, stderr=wf)
                p.wait()


if __name__ == '__main__':
    main()
