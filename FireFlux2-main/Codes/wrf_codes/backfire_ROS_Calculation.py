#This code will compute the backfire rate of spread for the wrfout file. This way, I can add an adjustment factor to the original run to rerun it and compare those two
'''This code is in 3 parts. The first part will calculate the backfire ROS from a point just above and to the 
left of the fire line

The second part of this code will calculate the backfire ROS based on the video with the roof of the building as the reference point

The third part of this code will calculate the backfire ROS based on the last point of the run.'''

'''PART 1'''
# %% importing necessary libraries
print('Importing libraries')
import netCDF4 as nc
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# %% Importing the file

print('Reading in the file')
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_d01_2013-01-30_15:00:00')


# %% importing variables
print('Reading in the variables')

print('Reading in fire area')
fire_area = wrfout.variables['FIRE_AREA'][:, :, :] #time, south_north subgrid, west_east subgrid

print('Reading in fxlat and fxlong')
fxlat = wrfout.variables['FXLAT'][:, :, :]
fxlong = wrfout.variables['FXLONG'][:, :, :]

print('Assigning the subgrid')
start_y_subgrid = fxlat[:, 1993, :]
start_x_subgrid = fxlong[:, :, 809]
# %% Calculations
print('Calculating the backfire ROS')
time = np.where(fire_area[:, 2001, 801] > 0)[0][0] #this was done to see where the fire area backfires to 4 meters up and 4 meters left

#With this I can calculate the backfire rate of spread. Since everything is in seconds, it's easy to calculate
time_original = np.where(fire_area[:, 1993, 809] > 0)[0][0]
print('The time difference between them is:', time - time_original)
print('The backfire rate of spread is:', (np.sqrt((4 ** 2) + (4 ** 2))/(time - time_original)),'m/s')
print('The correction factors that needs to be added is: ', (0.02)/(np.sqrt((4 ** 2) + (4 ** 2))/(time - time_original)))

''' PART TWO '''
# %% Importing the second file since the first file doesn't reach the point for calculating the backfire ros at the house
print('That was for 4 meters away from the burn, now I will be calculating the distance recorded in the video')


print('Reading in the second file')
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_d01_2013-01-30_15:16:40')


# %% importing variables

print('Reading in the variables')
print('Reading in fire area')
fire_area = wrfout.variables['FIRE_AREA'][:, :, :] #time, south_north subgrid, west_east subgrid

print('Reading in fxlat and fxlong')
fxlat = wrfout.variables['FXLAT'][:, :, :]
fxlong = wrfout.variables['FXLONG'][:, :, :]

print('Assigning the subgrid')
start_y_subgrid = fxlat[:, 1993, :]
start_x_subgrid = fxlong[:, :, 809]
# %% Calculations
# Point 1 location
x1 = 365.28
y1 = 975.88
# Point 2 location
x2 = 357.28
y2 = y1

print('Assigning the values')
south_north_point_1 = np.argmin(abs(fxlat[0, :, 0] - 976))
west_east_point_1 = np.argmin(abs(fxlong[0, 0, :] - 365))
print('The values for south_north and west_east are:', south_north_point_1, west_east_point_1)
south_north_point_2 = south_north_point_1
west_east_point_2 = np.argmin(abs(fxlong[0, 0, :] - 357))

time_point_1 = np.where(fire_area[:, south_north_point_1, west_east_point_1] > 0)[0][0] #this was done to see where the fire area backfires to 4 meters up and 4 meters left

time_point_2 = np.where(fire_area[:, south_north_point_2, west_east_point_2] > 0)[0][0]
print('The ROS between the roof is:', 8/(time_point_2 - time_point_1))

# %% Part three

''' PART THREE '''
#Based on the ncview, I went to the last timestep and found that the location 2032, 753 has the last timestep for the backfire.
#So I will use that to calculate the backfire ROS. It seems like it's closest to the ignition point so that will
#make life easier for calculating it too.

start_y_subgrid = fxlat[:, 1993, :]
start_x_subgrid = fxlong[:, :, 809]


end_y_subgrid = fxlat[:, 2032, :]
end_x_subgrid = fxlong[:, :, 753]

print('The total backfire ROS is:', 
np.sqrt(((fxlat[0, 2032, 0] - fxlat[0, 1993, 0]) ** 2) + ((fxlong[0, 0, 809] - fxlong[0, 0, 753]) ** 2)) 
/ (np.where(fire_area[:, 2032, 753] > 0)[0][0] + (1000 - 248)))
