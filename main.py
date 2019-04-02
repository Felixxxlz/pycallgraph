from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import pytest
import numpy as np
import astropy
import numba
import theano
import pandas
import os
import scipy as sp
import time
import matplotlib
import tables
import sympy
import IPython
import Cython
import networkx
import statsmodels.api as sm
import obspy
import gammapy
import h5py
from skbio.test import pytestrunner
import ccdproc
import numexpr
import photutils
import asdf
import poppy
import bottleneck as bn
import pyregion
import brian2
import astroplan
import radio_beam


def main(repo):
    graphviz = GraphvizOutput()
    graphviz.repo = repo
    start_time = time.time()
    with PyCallGraph(output=graphviz):
        # np.test()
        # astropy.test()
        # numba.test()
        # theano.test()
        # pandas.test()
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/sklearn"])
        # sp.test()
        # matplotlib.test()
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/joblib"])
        # tables.test(heavy=True)
        # sympy.utilities.runtests.test(subprocess=False)
        # IPython.testing.test()
        # networkx.test()
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/bokeh"])
        # sm.test()
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/nbconvert", "--pyargs", "nbconvert"])
        # obspy.core.run_tests()
        # gammapy.test()
        # h5py.run_tests()
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/seaborn"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/sunpy"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/chainer"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/nilearn"])
        # pytestrunner()
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/dask"])
        # ccdproc.test()
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/xarray"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/specutils"])
        # numexpr.test()
        # photutils.test()
        # asdf.test()
        # poppy.test()
        # pytest.main(["./xlrd"])
        # pytest.main(["./astropy-helpers"])
        # bn.test()
        # pyregion.test()
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/oct2py"])
        # brian2.test()
        # astroplan.test()
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/naima"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/pyamg"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/patsy"])
        # radio_beam.test()
        # os.chdir("/home/ly/Desktop/REPOS/sphinx")
        # tox.cmdline()
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/randomgen"])
        # os.chdir("./hienoi")
        # pytest.main()
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/shared_ndarray"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/eliot"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/mahotas"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/nrrd"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/autoptim"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/sparse"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/alphalens"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/pyjet"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/numbagg"])

        # 19.04.02
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/pymc3"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/cvxpy"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/aplpy"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/numpydoc"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/deap
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/mpmath"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/oct2py"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/atpy"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/gwcs"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/starfish"])

        pytest.main(["./REPOS/cython-blis"])
    end_time = time.time()
    print(end_time - start_time)


if __name__ == '__main__':
    main('dill')
