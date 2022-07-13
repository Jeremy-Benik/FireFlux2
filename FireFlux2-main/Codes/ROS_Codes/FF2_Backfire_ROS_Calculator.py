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
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_d01_2013-01-30_15:00:00')
#wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_cheyenne/run_7/wrfout_d01_2013-01-30_15:00:00')
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
#initial run coords are: 2032, 753 and the ROS is: 0.022056307586713404
#run 1 coords are: 2025, 769 and the ROS is:  0.016343623213698418
#run 2 was 2024, 767 and 0.016343623213698418
#run 3 was 2024, 765 and 0.016968406861031387
#run 4 was 2026, 765 and 0.01733921815889029
#run 5 was 2020, 761 and 0.17
#run 6 was 2022, 761 and 
#run 7 was 2026, 763 and 0.018075580912794587

# ^ were the old results, The results below will be based on the first wrfout file at timestep 900

#initial run was 2010, 793 and 
#run 1 was 2007, 790 and 0.015989734039574453
#run 2 was 2010, 796 and 0.016798221788879665
#run 3 was 2010, 793 and 0.01709021600282394
#run 4 was 2007, 790 and 0.01720178385015444
#run 5 was 2004, 785 and 0.01767115575900313
#run 6 was 2010, 793 and 0.017712621441470035
#run 7 was 2010, 793 and 0.017739540319040657

south_north_2 = 2010
west_east_2 = 793

time = (929 - 248) # Use the same number
#time = 1550
print('The total backfire ROS is:', 
np.sqrt(((fxlat[0, south_north_2, 0] - fxlat[0, south_north_ig_line, 0]) ** 2) + ((fxlong[0, 0, west_east_ig_line]
 - fxlong[0, 0, west_east_2]) ** 2)) 
/ (np.where(fire_area[:, south_north_2, west_east_2] > 0)[0][0] - 248))


# %%
