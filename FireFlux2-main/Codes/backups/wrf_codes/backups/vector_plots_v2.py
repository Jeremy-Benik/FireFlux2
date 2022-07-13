# %% Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xarray as xr
import netCDF4 as nc
from wrf import getvar, interplevel
#import wrf-python lookup how to do this. interpolate them at the different levels
# then repeat the levels using the np.tile the same way we repeated the time
# %% Reading in the data using netcdf4
df1 = xr.open_dataset('/home/jbenik/FirefluxII/backups/FireFlux2_base/wrfout_d01_2013-01-30_15:00:00')
df = nc.Dataset('/home/jbenik/FirefluxII/backups/FireFlux2_base/wrfout_d01_2013-01-30_15:00:00', 'r', format='NETCDF4') #opening the file using netcdf
# %% Reading in some variables
#here is what I have found so far:
'''Notes: I think the coordinate system 
Faces north and starts at the bottom left. 
My reasoning behind this is that in the ncview function, 
I see the fire propagate downwards, indicating 
it would then have to start from the bottom left since the wind vector 
plot has all positive lat an lon values. Now I need to find where the 
towers are but I should be able to do that using google. 
Bottom left anemometer:
lat:  29°22'55.74"N = 29.38215
lon:  95° 2'34.01"W = -95.04280555555556

Main tower: 
 29°23'16.71"N = 29.387975
 95° 2'29.12"W = -95.04142222222222

658 meters, 11.50 degree
xlat = 131.184
xlon = 644.79

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
V = df.variables['V'][:, :, 30, 30]
U = df.variables['U'][:, :, 30, 30]
#U = np.swapaxes(U, 0 ,1)
#V = np.swapaxes(V, 0 ,1)
#height = df.variables['ZS']
time = df.variables['XTIME'][:]
PH = df.variables['PH'][:, :, 30, 30]
PHB = df.variables['PHB'][:, :, 30, 30] #calculate 
height = 0.5*(PHB[:,:-1] + PH[:,:-1] + PHB[: , 1:] + PH[:, 1:])/9.81 #what this does is it takes everything from the first levels up until the last level of the cube
#and then adds those two together, then it takes everything except the first layer of the cube and adds those together, this way the units will line up better
#and be treated as in the middle of the cube per the example that I was told. This mainly has to do with the fact that the variables needed are bottom_top stag
#which changes a lot here since it is not treated in the middle of the cube, instead the face of the cube, so we need to do this math to average it out
#this equation along with a better explanation can be found at https://wiki.openwfm.org/wiki/How_to_interpret_WRF_variables
#this is elevation_theta in the doc
#
#height = (PH + PHB) / 9.81
len_height = height.shape[1]
time = np.tile(time, {1, len_height}) #tile repeats time len(height) times
#I will need one similar line for height, and this will at the height that I want.
#wrf-python tool should return the wind at that height.

fig, ax = plt.subplots(figsize = (12, 12))
ax.quiver(time, height, U, V)

plt.show()
