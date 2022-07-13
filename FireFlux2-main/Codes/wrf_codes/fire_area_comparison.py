#this file will attempt to plot the fire area at the last point to see if I can calcualte a difference between two files

# %% Importing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import netCDF4 as nc
import numpy as np

# %% Reading in the files
print('Reading in the files')
# I am reading in two files to compare the fire area of them both at the last time step
wrfout_unmod = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_d01_2013-01-30_15:16:40')
wrfout_mod = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/backfire_modified_wrfout_d01_2013-01-30_15:16:40')

# %% Assigning variables
print('reading in the fxlat and fxlong variables')

# Unmodified files
print('Reading in lat and lon from unmodified files')
lat_unmod = wrfout_unmod.variables['FXLAT'][-1, :, :]
lon_unmod = wrfout_unmod.variables['FXLONG'][-1, :, :]
print('Reading in fire area from unmodified files')
fire_area_unmod = wrfout_unmod.variables['FIRE_AREA'][-1, :, :]

print('Reading in lat and lon from modified files')
lat_mod = wrfout_mod.variables['FXLAT'][-1, :, :]
lon_mod = wrfout_mod.variables['FXLONG'][-1, :, :]
print('Reading in fire area from modified files')
fire_area_mod = wrfout_mod.variables['FIRE_AREA'][-1, :, :]



#Modified files

# %%
