#This code will compute the backfire rate of spread for the wrfout file. This way, I can add an adjustment factor to the original run to rerun it and compare those two
# %% importing necessary libraries
print('Importing libraries')
import netCDF4 as nc
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %% Reading in the wrfout file

print('Reading in the second file')
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_cheyenne/wrfout_d01_2013-01-30_15:29:01')
# %% importing variables

print('Reading in the variables')
print('Reading in fire area')
fire_area = wrfout.variables['FIRE_AREA'][:, :, :] #time, south_north subgrid, west_east subgrid

fxlat = wrfout.variables['FXLAT'][:, :, :]
fxlong = wrfout.variables['FXLONG'][:, :, :]

south_north_ig_line = np.argmin(abs(fxlat[0, :, 0] - 997))
west_east_ig_line = np.argmin(abs(fxlong[0, 0, :] - 405))
print('The location for the ignition line are:', south_north_ig_line, west_east_ig_line)

# %% Calculating the backfire ROS

south_north_2 = 2013
west_east_2 = 760

time = (894 - 248) + 904
print('The total backfire ROS is:', 
np.sqrt(((fxlat[0, south_north_2, 0] - fxlat[0, south_north_ig_line, 0]) ** 2) + ((fxlong[0, 0, west_east_ig_line]
 - fxlong[0, 0, west_east_2]) ** 2)) 
/ (np.where(fire_area[:, south_north_2, west_east_2] > 0)[0][0] + time))

