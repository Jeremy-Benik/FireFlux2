#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:10:46 2022

@author: Jeremy Benik
"""

# %% Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
from metpy.plots import SkewT, Hodograph
from metpy.units import units
import metpy.calc as mpcalc
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import xarray as xr
import netCDF4 as nc
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from wrf import getvar, interplevel
# %%
df1 = nc.Dataset('/media/jeremy/Data/Fireflux2/Spartan_Files/wrfout', 'r', format='NETCDF4') #opening the file using netcdf
df = xr.open_dataset('/media/jeremy/Data/Fireflux2/Spartan_Files/wrfout') # opening the file using xarray since it opens it a different way
print(df1.variables.keys())
lat = df1.variables['XLAT'][:] #south is negatuive
lon = df1.variables['XLONG'][:] #west is negative
#print(df.info())
u = df1.variables['U'][:] #defining the U wind and setting that to u
v = df1.variables['V'][:] #defining the v wind and setting that to v
w = df1.variables['W'][:] #defining the w wind and setting that to w
fire_area = df.variables['FIRE_AREA']

# %%
u = getvar(df1, 'ua')
v = getvar(df1, 'va')
w = getvar(df1, 'wa')