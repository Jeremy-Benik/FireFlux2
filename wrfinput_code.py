# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 19:27:25 2021

@author: Rubix
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
# %% #reading in the file
df = xr.open_dataset('wrfinput_d01') # opening the file using xarray since it opens it a different way
df1 = nc.Dataset('wrfinput_d01') #opening the file using netcdf
print(df1.variables.keys()) #this is used to see all the variables in the dataframe
u = df.variables['U'][:] #defining the U wind and setting that to u
v = df.variables['V'][:] #defining the v wind and setting that to v
w = df.variables['W'][:] #defining the w wind and setting that to w
p = df.variables['P'][:] #defining pressure and setting it to p this is in pa
u10 = df.variables['U10'][:] #defining u at 10 meters as u10
v10 = df.variables['V10'][:] #defining v at 10 meters as v10
# %% Attempting to make a plot of the variables vs height

print(p)
