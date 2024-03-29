#! /usr/bin/env python
# nose will check that figures can be created
# execute this script to create figure_plot_netcdf_*.png files.
# To compare results
# display figure_plot_netcdf_ppi.png& display figure_plot_netcdf_ppi_radar.png&
# display figure_plot_netcdf_rhi.png& display figure_plot_netcdf_rhi_radar.png&

import os.path

import netCDF4
import matplotlib.pyplot as plt
import pyart

DIR = os.path.dirname(__file__)
NETCDF_RHI = os.path.join(DIR, 'sgpxsaprrhicmacI5.c0.20110524.015604_NC4.nc')
NETCDF_PPI = os.path.join(DIR, 'sgpxsaprsesurcmacI4.c0.20110520.105511.nc')


def test_plot_netcdf_rhi(outfile=None):
    dataset = netCDF4.Dataset(NETCDF_RHI)
    display = pyart.graph.NetcdfDisplay(dataset)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    display.plot_rhi('reflectivity_horizontal', 0)
    if outfile:
        fig.savefig(outfile)


def test_plot_netcdf_ppi(outfile=None):
    dataset = netCDF4.Dataset(NETCDF_PPI)
    display = pyart.graph.NetcdfDisplay(dataset)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    display.plot_ppi('reflectivity_horizontal', 0)
    if outfile:
        fig.savefig(outfile)


# version of above which use the RadarDisplay to return similar images.


def test_plot_netcdf_radar_rhi(outfile=None):
    radar = pyart.io.read_netcdf(NETCDF_RHI)
    radar.metadata['instrument_name'] = ''
    display = pyart.graph.RadarDisplay(radar)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    display.plot_rhi('reflectivity_horizontal', 0)
    if outfile:
        fig.savefig(outfile)


def test_plot_netcdf_radar_ppi(outfile=None):
    radar = pyart.io.read_netcdf(NETCDF_PPI)
    display = pyart.graph.RadarDisplay(radar)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    display.plot_ppi('reflectivity_horizontal', 0)
    if outfile:
        fig.savefig(outfile)


if __name__ == "__main__":
    test_plot_netcdf_rhi('figure_plot_netcdf_rhi.png')
    test_plot_netcdf_ppi('figure_plot_netcdf_ppi.png')
    test_plot_netcdf_radar_rhi('figure_plot_netcdf_rhi_radar.png')
    test_plot_netcdf_radar_ppi('figure_plot_netcdf_ppi_radar.png')
