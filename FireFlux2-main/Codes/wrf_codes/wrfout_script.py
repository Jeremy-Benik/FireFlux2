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
import matplotlib.pyplot as plt
import pandas as pd
#from metpy.plots import SkewT, Hodograph
#from metpy.units import units
#import metpy.calc as mpcalc
#from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import xarray as xr
import netCDF4 as nc
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature
from wrf import getvar, interplevel
# %%
#since I don't know where the towers are, I will define that later, but I'll make
#it easier to do so by using variables 
n = 10
m = 20
#this next variables is the length of time, in this case it's 64 but it should be something different in the future
t = 64
bot_top = 80
df1 = nc.Dataset('/home/jbenik/FirefluxII/FireFlux2_base/wrfout_d01_2013-01-30_15:00:00', 'r', format='NETCDF4') #opening the file using netcdf
df = xr.open_dataset('/home/jbenik/FirefluxII/FireFlux2_base/wrfout_d01_2013-01-30_15:00:00') # opening the file using xarray since it opens it a different way
#print(df1.variables.keys())
#print(df.info())
lat = df1.variables['XLAT'][:] #south is negatuive
lon = df1.variables['XLONG'][:] #west is negative
#lat(Time, south_north, west_east)
#lon(time, south_north, west_east)
#print(df.info())
u = df1.variables['U'][:] #defining the U wind and setting that to u
#u(time, bottom_top, south_north, west_east_stag)
v = df1.variables['V'][:] #defining the v wind and setting that to v
#v(time, bottom_top, south_north_stag, west_east)
w = df1.variables['W'][:] #defining the w wind and setting that to w
#w(time, bottom_top_stag, south_north, west east)
fire_area = df.variables['FIRE_AREA'][:]
#fire_area(time, south_north_subgrid, west_east_subgrid)

# %%
# u = getvar(df1, 'ua')
# v = getvar(df1, 'va')
# w = getvar(df1, 'wa')

# u_wind = []
# for i in range(t):
#     for 
u_wind = []
for i in range(t):
	for j in range(bot_top):
		u_wind.append(u[i, j, n, m])
#print(u[60, 0, n, m])
# %%
