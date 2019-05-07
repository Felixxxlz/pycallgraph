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
from subprocess import Popen
import os
import tqdm


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
    numpy_version = ["9ae4f9bae9344ee0f1ca4d5767e49c196d534efc"][-1][:7]
    try:
        os.makedirs(os.path.join("test_logs", "numpy", numpy_version))
    except:
        pass
    downstream_test_pyfiles = os.listdir("test_numpy")
    for downstream_test_pyfile in tqdm.tqdm(downstream_test_pyfiles[46:]):
        downstream_name = "_".join(downstream_test_pyfile.split('.')[0].split("_")[1:])
        if downstream_name == "alphalens":
            continue
        pyfile_path = os.path.join("test_numpy", downstream_test_pyfile)
        with open(os.path.join("test_logs", "numpy", numpy_version, \
            "test_log_" + downstream_name + ".txt"), mode="w") as wf:
            p = Popen(["python3", pyfile_path], stdout=wf, stderr=wf)
            p.wait()


if __name__ == '__main__':
    main()
