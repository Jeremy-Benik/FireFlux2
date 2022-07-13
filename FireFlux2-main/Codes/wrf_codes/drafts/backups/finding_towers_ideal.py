''' The purpose of this program is to find the locations of the towers for the ideal wrfout file
Here are the results of this code for quick access if needed
None of these are staggered, these are just using the regular grid

Main tower
South_north for main tower is at: 190
West_east for main tower is: 93

East tower
South_north for east tower is at: 158
West_east for east tower is: 117

West tower
South_north for west tower is at: 151
West_west for west tower is: 94

South tower
South_north for south tower is at: 119
West_south for south tower is: 115

Fire mesh coordinates

Main tower
South_north for main tower is at: 1908
West_east for main tower is: 937

East tower
South_north for east tower is at: 1581
West_east for east tower is: 1173

West tower
South_north for west tower is at: 1511
West_west for west tower is: 943

South tower
South_north for south tower is at: 1199
West_south for south tower is: 1155 '''
# -*- coding: utf-8 -*-
"""
Created on Tues March 29 11:36:54 2022

@author: Jeremy Benik
"""
# %% importing libraries
import netCDF4 as nc
import numpy as np
# %% importing the wrfout file from the ideal case
#wrfout file from the ideal case
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00', 'r')
# %% Calling in latitude and longitude from the wrfout file from the ideal case
#latitude
lat = wrfout.variables['XLAT'][:]

#longitude
lon = wrfout.variables['XLONG'][:]

# %% finding the towers on the atmospheric mesh
'''Coordinates as found on google earth: 
Main Tower: 469, 954
East Tower: 587, 791
West Tower: 472, 756
South Tower: 578, 600 '''

# Main tower
south_north_main_tower = np.argmin(abs(lat[0, :, 0] - 954))
west_east_main_tower = np.argmin(abs(lon[0, 0, :] - 469))

# East tower
south_north_east_tower = np.argmin(abs(lat[0, :, 0] - 791))
west_east_east_tower = np.argmin(abs(lon[0, 0, :] - 587))

# West Tower
south_north_west_tower = np.argmin(abs(lat[0, :, 0] - 756))
west_east_west_tower = np.argmin(abs(lon[0, 0, :] - 472))

# South Tower
south_north_south_tower = np.argmin(abs(lat[0, :, 0] - 600))
west_east_south_tower = np.argmin(abs(lon[0, 0, :] - 578))
# %% Printing where they are for easy access later
# Main tower
print('South_north for main tower is at:', south_north_main_tower)
print('West_east for main tower is:', west_east_main_tower)
#print('\n')
print('********************************************')

# East Tower
print('South_north for east tower is at:', south_north_east_tower)
print('West_east for east tower is:', west_east_east_tower)
#print('\n')
print('********************************************')

# West Tower
print('South_north for west tower is at:', south_north_west_tower)
print('West_west for west tower is:', west_east_west_tower)
#print('\n')
print('********************************************')

# South Tower
print('South_north for south tower is at:', south_north_south_tower)
print('West_south for south tower is:', west_east_south_tower)
#print('\n')
print('********************************************')
# %% Now trying to find them using the fire mesh
print('THESE NEXT INDEXES WILL BE FOR THE FIRE MESH ON THE IDEAL RUN')

# Callin in the variables fxlat and fxlong and assigning them to the same so I can copy the code easier
#latitude
lat = wrfout.variables['FXLAT'][:]

#longitude
lon = wrfout.variables['FXLONG'][:]

# %% finding the towers on the atmospheric mesh

# Main tower
south_north_main_tower = np.argmin(abs(lat[0, :, 0] - 954))
west_east_main_tower = np.argmin(abs(lon[0, 0, :] - 469))

# East tower
south_north_east_tower = np.argmin(abs(lat[0, :, 0] - 791))
west_east_east_tower = np.argmin(abs(lon[0, 0, :] - 587))

# West Tower
south_north_west_tower = np.argmin(abs(lat[0, :, 0] - 756))
west_east_west_tower = np.argmin(abs(lon[0, 0, :] - 472))

# South Tower
south_north_south_tower = np.argmin(abs(lat[0, :, 0] - 600))
west_east_south_tower = np.argmin(abs(lon[0, 0, :] - 578))
# %% Printing where they are for easy access later
# Main tower
print('South_north for main tower is at:', south_north_main_tower)
print('West_east for main tower is:', west_east_main_tower)
#print('\n')
print('********************************************')

# East Tower
print('South_north for east tower is at:', south_north_east_tower)
print('West_east for east tower is:', west_east_east_tower)
#print('\n')
print('********************************************')

# West Tower
print('South_north for west tower is at:', south_north_west_tower)
print('West_west for west tower is:', west_east_west_tower)
#print('\n')
print('********************************************')

# South Tower
print('South_north for south tower is at:', south_north_south_tower)
print('West_south for south tower is:', west_east_south_tower)
#print('\n')
print('********************************************')
