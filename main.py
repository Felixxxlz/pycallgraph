#!/usr/bin/env python
'''
This example demonstrates a simple recursive call.
'''
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import pytest
import numpy as np
import astropy
import numba
import obspy.core
import theano
import ccdproc
import asdf


def main():
    graphviz = GraphvizOutput()
    graphviz.repo = 'asdf'

    with PyCallGraph(output=graphviz):
        # np.test()
        # astropy.test()
        # numba.test()
        # obspy.core.run_tests(test_all_modules=True)
        # theano.test()
        # ccdproc.test()
        asdf.test()


if __name__ == '__main__':
    main()
