#!/usr/bin/env python
'''
This example demonstrates a simple recursive call.
'''
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import numpy as np
import astropy
import scipy as sp


def main():
    graphviz = GraphvizOutput()

    with PyCallGraph(output=graphviz):
        # np.test()
        # sp.test('full')
        astropy.test()


if __name__ == '__main__':
    main()
