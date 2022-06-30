'''The purpose of this code is to find when the fire reaches the points on the grid'''
# -*- coding: utf-8 -*-
"""
Created on Sat March 15 11:36:54 2022

@author: Jeremy Benik
"""
# %% Importing libraries
print("importing necessary libraries")
import netCDF4 as nc
import numpy as np
import xarray as xr
import pandas as pd
import wrf
# %% Reading in the files
print("Reading in the wrfout file")
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00', 'r')
print('reading in the short towers')
df_w1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTWdespikedrotated.csv')

df_e1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTEdespikedrotated.csv')

df_s1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTSdespikedrotated.csv')


# %% Calling fire area
print('I am now reading in the fire_area')
fire_area = wrfout.variables['FIRE_AREA'][:, :, :] #time, south_north_subgrid, west_east_subgrid
print('I am reading in the time variable')
time = wrfout.variables['XTIME'][:]
time2 = np.arange(0, 1000)
# %% Specifying where the towers are on the subgrid scale
# Main tower
y_main_sub = 1908
x_main_sub = 937

# East tower
y_east_sub = 1581
x_east_sub = 1173

# West tower
y_west_sub = 1511
x_west_sub = 943

# South tower
y_south_sub = 1199
x_south_sub = 1155
# %% Now I will use the fire area variable and see what time the fire hit the area
print('Main tower data')
print('The time in seconds when the fire area hit the main tower is at:', time[np.where(fire_area[:, y_main_sub, x_main_sub] > 0)[0][0]] * 60, 'seconds')
print('The index when the fire area hit the main tower is at:',np.where(fire_area[:, y_main_sub, x_main_sub] > 0)[0][0])
print('**************************************************************************************************************************************************')
print('East tower data')
print('The time in seconds when the fire area hit the east tower is at:', time[np.where(fire_area[:, y_east_sub, x_east_sub] > 0)[0][0]] * 60, 'seconds')
print('The index when the fire area hit the east tower is at:',np.where(fire_area[:, y_east_sub, x_east_sub] > 0)[0][0])
print('**************************************************************************************************************************************************')
print('West tower data')
print('The time in seconds when the fire area hit the west tower is at:', time[np.where(fire_area[:, y_west_sub, x_west_sub] > 0)[0][0]] * 60, 'seconds')
print('The index when the fire area hit the west tower is at:',np.where(fire_area[:, y_west_sub, x_west_sub] > 0)[0][0])
print('**************************************************************************************************************************************************')
print('South tower data')
print('The time in seconds when the fire area hit the south tower is at:', time[np.where(fire_area[:, y_south_sub, x_south_sub] > 0)[0][0]] * 60, 'seconds')
print('The index when the fire area hit the south tower is at:',np.where(fire_area[:, y_south_sub, x_south_sub] > 0)[0][0])
