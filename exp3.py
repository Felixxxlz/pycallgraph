from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import pytest
import os
import time
import numpy as np
import astropy
import numba
import pandas
import theano
import scipy as sp
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
import verde
import astroimtools
import stginga
import synphot
import pydl


def main():
    astropy.test()
    pytest.main(["/usr/local/lib/python3.6/dist-packages/joblib"])
    matplotlib.test()
    np.test()
    pandas.test()
    pytest.main(["/usr/local/lib/python3.6/dist-packages/sklearn"])
    sp.test()
    tables.test(heavy=True)
    theano.test()
    sympy.utilities.runtests.test(subprocess=False)
    networkx.test()
    obspy.core.run_tests()
    sm.test()
    pytest.main(["/usr/local/lib/python3.6/dist-packages/dask"])
    gammapy.test()
    h5py.run_tests()
    pytest.main(["/usr/local/lib/python3.6/dist-packages/nilearn"])
    pytestrunner()
    pytest.main(["/usr/local/lib/python3.6/dist-packages/seaborn"])
    ccdproc.test()
    numexpr.test()
    pytest.main(["/usr/local/lib/python3.6/dist-packages/specutils"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/xarray"])
    asdf.test()
    pytest.main(["./astropy-helpers"])
    bn.test()
    photutils.test()
    poppy.test()
    pyregion.test()
    astroplan.test()
    brian2.test()
    pytest.main(["/usr/local/lib/python3.6/dist-packages/naima"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/patsy"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/pyamg"])
    radio_beam.test()
    numba.test()
    pytest.main(["/usr/local/lib/python3.6/dist-packages/randomgen"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/shared_ndarray"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/mahotas"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/nrrd"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/sparse"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/alphalens"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/pyjet"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/numbagg"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/pymc3"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/cvxpy"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/aplpy"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/deap"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/mpmath"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/oct2py"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/atpy"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/gwcs"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/starfish"])
    pytest.main(["./REPOS/UTide"])
    pytest.main(["./REPOS/pyik"])
    pytest.main(["./REPOS/npstreams"])
    pytest.main(["./REPOS/PyXRD"])
    pytest.main(["./REPOS/PVMismatch"])
    pytest.main(["./REPOS/spampy"])
    pytest.main(["./REPOS/Pyrr"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/nptdms"])
    pytest.main(["./REPOS/hienoi"])
    pytest.main(["./REPOS/molml"])
    pytest.main(["./REPOS/OOMMFTools"])
    pytest.main(["./REPOS/nnlib"])
    pytest.main(["./REPOS/kravatte"])
    pytest.main(["./REPOS/dicom-numpy"])
    pytest.main(["./REPOS/geometer"])
    pytest.main(["./REPOS/slugnet"])
    pytest.main(["./REPOS/zappy"])
    pytest.main(["./REPOS/gfmm"])
    pytest.main(["./REPOS/pyjson_tricks"])
    pytest.main(["./REPOS/pdepy"])
    pytest.main(["./REPOS/tidynamics"])
    pytest.main(["./REPOS/texpy"])
    pytest.main(["./REPOS/numpy-buffer"])
    pytest.main(["./REPOS/feets"])
    verde.test()
    pytest.main(["./REPOS/psopy"])
    pytest.main(["./REPOS/randNLA"])
    pytest.main(["./REPOS/indi"])
    pytest.main(["./REPOS/pytablewriter"])
    astroimtools.test()
    stginga.test()
    synphot.test()
    pydl.test()
    pytest.main(["./REPOS/prince"])
    pytest.main(["./REPOS/Coinsta"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/iexfinance"])
    pytest.main(["./REPOS/kodiak"])
    pytest.main(["./REPOS/phildb"])
    pytest.main(["./REPOS/datacompy"])
    pytest.main(["./REPOS/espandas"])
    pytest.main(["./REPOS/deepgraph"])
    pytest.main(["./REPOS/lens"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/plydata"])
    pytest.main(["/usr/local/lib/python3.6/dist-packages/ibis"])
    pytest.main(["./REPOS/validada"])
    pytest.main(["./REPOS/partridge"])
    pytest.main(["./REPOS/finta"])


if __name__ == '__main__':
    main()
