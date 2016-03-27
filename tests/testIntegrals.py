#!/usr/bin/env python

#
# LSST Data Management System
# Copyright 2008-2013 LSST Corporation.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.
#

import unittest
import os
import numpy
try:
    import scipy.integrate
except ImportError:
    scipy = None

import lsst.utils.tests
import lsst.meas.modelfit

numpy.random.seed(500)


class IntegralsTestCase(lsst.utils.tests.TestCase):

    def testBVN(self):
        data = numpy.loadtxt(os.path.join("tests", "reference", "bvn.txt"), delimiter=',')
        for h, k, r, p1 in data:
            p2 = lsst.meas.modelfit.bvnu(h, k, r)
            self.assertClose(p1, p2, rtol=1E-14)


def suite():
    """Returns a suite containing all the test cases in this module."""

    lsst.utils.tests.init()

    suites = []
    suites += unittest.makeSuite(IntegralsTestCase)
    suites += unittest.makeSuite(lsst.utils.tests.MemoryTestCase)
    return unittest.TestSuite(suites)


def run(shouldExit=False):
    """Run the tests"""
    lsst.utils.tests.run(suite(), shouldExit)

if __name__ == "__main__":
    run(True)
