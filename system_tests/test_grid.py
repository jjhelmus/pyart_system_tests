#!/usr/bin/env python

import tempfile
import os
import os.path

import pyart
import numpy as np

DIR = os.path.dirname(__file__)
NETCDF_FILE = os.path.join(DIR, 'swx_20120520_0641.nc')


def test_grid():
    xsapr_se = pyart.io.read_netcdf(NETCDF_FILE)
    grid = pyart.map.grid_from_radars(
        (xsapr_se, ),
        grid_shape=(101, 101, 2),
        grid_limits= ((-50000, 50000), (-50000, 50000), (0, 1000)),
        fields=['corrected_reflectivity_horizontal'],
        refl_field='corrected_reflectivity_horizontal',
        max_refl=100.)
    tmpfile = tempfile.mkstemp(suffix='.nc', dir='.')[1]
    grid.write(tmpfile)
    grid2 = pyart.io.read_grid(tmpfile)

    # check metadata
    for k, v in grid.metadata.iteritems():
        print "Checking key:", k, "should have value:", v
        print grid2.metadata
        assert grid2.metadata[k] == v

    # check axes
    for axes_key in grid.axes.keys():
        for k, v in grid.axes[axes_key].iteritems():
            print "Checking axes_key:", axes_key, "key:", k
            if k == 'data':
                assert np.all(grid.axes[axes_key][k] == v)
            else:
                assert grid2.axes[axes_key][k] == v

    # check fields
    for field in grid.fields.keys():
        for k, v in grid.fields[field].iteritems():
            print "Checking field:", field, "key:", k
            if k == 'data':
                assert np.all(grid.fields[field][k] == v)
            else:
                assert grid2.fields[field][k] == v

    os.remove(tmpfile)
