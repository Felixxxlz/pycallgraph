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
import tox
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
import unittest
import wcsaxes


def main():
    graphviz = GraphvizOutput()
    graphviz.repo = 'radio_beam'
    start_time = time.time()
    with PyCallGraph(output=graphviz):
        # np.test()
        # astropy.test()
        # numba.test()
        # theano.test()
        # pandas.test()
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/sklearn"])
        # sp.test()
        # matplotlib.test()
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/joblib"])
        # tables.test(heavy=True)
        # sympy.utilities.runtests.test(subprocess=False)
        # os.chdir('pyjulia')
        # tox.cmdline()
        # IPython.testing.test()
        # os.chdir('scrapy')
        # tox.cmdline()
        # networkx.test()
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/bokeh"])
        # sm.test()
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/nbconvert", "--pyargs", "nbconvert"])
        # obspy.core.run_tests()
        # gammapy.test()
        # h5py.run_tests()
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/seaborn"])
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/sunpy"])
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/chainer"])
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/nilearn"])
        # pytestrunner()
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/dask"])
        # ccdproc.test()
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/xarray"])
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/specutils"])
        # numexpr.test()
        # photutils.test()
        # asdf.test()
        # poppy.test()
        # pytest.main(["-x", "./xlrd"])
        # pytest.main(["-x", "./astropy-helpers"])
        # bn.test()
        # pyregion.test()
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/oct2py"])
        # brian2.test()
        # astroplan.test()
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/naima"])
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/pyamg"])
        # pytest.main(["-x", "/usr/local/lib/python3.6/dist-packages/patsy"])
        radio_beam.test()
    end_time = time.time()
    print(end_time - start_time)


if __name__ == '__main__':
    main()
