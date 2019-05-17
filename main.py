from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import pytest
import os
import time
# import numpy as np
# import astropy
# import numba
# import pandas
# import theano
# import scipy as sp
# import matplotlib
# import tables
# import sympy
# import IPython
# import Cython
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
# import astroplan
# import radio_beam
# import verde
# import pooch
# import astroimtools
# import stginga
# import synphot
# import pydl


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

        # 19.04.03
        # pytest.main(["./REPOS/UTide"])
        # pytest.main(["./REPOS/pyik"])
        # pytest.main(["./REPOS/npstreams"])
        # pytest.main(["./REPOS/PyXRD"])
        # pytest.main(["./REPOS/PVMismatch"])
        # pytest.main(["./REPOS/spampy"])
        # pytest.main(["./REPOS/Pyrr"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/nptdms"])
        # pytest.main(["./REPOS/hienoi"])
        # pytest.main(["./REPOS/molml"])
        # pytest.main(["./REPOS/OOMMFTools"])
        # pytest.main(["./REPOS/nnlib"])
        # pytest.main(["./REPOS/kravatte"])
        # pytest.main(["./REPOS/dicom-numpy"])

        # 19.04.04
        # pytest.main(["./REPOS/geometer"])
        # pytest.main(["./REPOS/slugnet"])
        # pytest.main(["./REPOS/zappy"])
        # pytest.main(["./REPOS/gfmm"])
        # pytest.main(["./REPOS/pyjson_tricks"])
        # pytest.main(["./REPOS/pdepy"])
        # pytest.main(["./REPOS/tidynamics"])
        # pytest.main(["./REPOS/texpy"])
        # pytest.main(["./REPOS/numpy-buffer"])
        # pytest.main(["./REPOS/pandas_degreedays"])

        # 19.04.08
        # pytest.main(["./REPOS/pyshapes"])
        # pytest.main(["./REPOS/feets"])
        # droplet.run()
        # verde.test()
        # pooch.test()
        # pytest.main(["./REPOS/psopy"])
        # pytest.main(["./REPOS/randNLA"])
        # pytest.main(["./REPOS/sdaopt"])
        # pytest.main(["./REPOS/indi"])
        # pytest.main(["./REPOS/pytablewriter"])
        
        # 19.04.09
        # astroimtools.test()
        # stginga.test()
        # synphot.test()
        # pydl.test()

        # 19.04.12
        # pytest.main(["./REPOS/prince"])
        # pytest.main(["./REPOS/Coinsta"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/iexfinance"])
        # pytest.main(["./REPOS/kodiak"])
        # pytest.main(["./REPOS/phildb"])
        # pytest.main(["./REPOS/datacompy"])
        # pytest.main(["./REPOS/espandas"])
        # pytest.main(["./REPOS/deepgraph"])
        # pytest.main(["./REPOS/lens"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/plydata"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/ibis"])
        # pytest.main(["./REPOS/validada"])
        # pytest.main(["./REPOS/partridge"])
        # pytest.main(["./REPOS/meza"])
        # pytest.main(["./REPOS/finta"])

        # 19.05.15
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/imexam"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/astroscrappy"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/astroML"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/astroquery"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/baseband"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/ginga"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/halotools"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/poliastro"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/stingray"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/gala"])

        # 19.05.16
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/astropy_healpix"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/dust_extinction"])
        # pytest.main(["./REPOS/subsync"])
        # pytest.main(["./REPOS/TGAN"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/dipy"])
        # pytest.main(["./REPOS/auto_ml"])
        # pytest.main(["./REPOS/scikit-optimize"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/xcessiv"])
        # pytest.main(["./REPOS/scikit-plot"])

        # 19.05.17
        # pytest.main(["./REPOS/onnxmltools"])
        # pytest.main(["./REPOS/seqlearn"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/pystruct"])
        # pytest.main(["./REPOS/kmodes"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/hdbscan"])
        # pytest.main(["/usr/local/lib/python3.6/dist-packages/gplearn"])
        # pytest.main(["./REPOS/spherecluster"])
        # pytest.main(["./REPOS/skpro"])
        # pytest.main(["./REPOS/profanity-check"])
        # pytest.main(["./REPOS/pailab"])
        # pytest.main(["./REPOS/chainer_sklearn"])
        # pytest.main(["./REPOS/sklearn-evaluation"])
        # pytest.main(["./REPOS/sklearn2"])
        pytest.main(["./REPOS/sklearn_lvq"])

    end_time = time.time()
    print(end_time - start_time)


if __name__ == '__main__':
    main("sklearn_lvq")
