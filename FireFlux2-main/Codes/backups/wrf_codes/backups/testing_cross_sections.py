#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:10:46 2022

@author: Jeremy Benik
"""

'''Notes: this program was made with the wrfout file that was not completed, so the times will
be slighly off. In this run, I only have 64 times, but I want to tru and get a head start
Important numbers: 
	Time = 64 ;
	bottom_top = 80 ;
	bottom_top_stag = 81 ;
	fuel_moisture_classes_stag = 5 ;
	seed_dim_stag = 2 ;
	soil_layers_stag = 5 ;
	south_north = 319 ;
	south_north_stag = 320 ;
	south_north_subgrid = 3200 ;
	west_east = 199 ;
	west_east_stag = 200 ;
	west_east_subgrid = 2000 ;'''
# %% Importing libraries
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

# import metpy.calc as mpcalc
# from metpy.cbook import get_test_data
from metpy.interpolate import cross_section
# %%
data = xr.open_dataset('/home/jbenik/FirefluxII/fireflux2_3/wrfout_d01_2013-01-30_15:00:00', False)
lat = df.variables['XLAT'][:]
lon = df.variables['XLON'][:]
start = (0, 0)
end = (199, 199)

# %%
cross = cross_section(data, start, end).set_coords(('lat', 'lon'))