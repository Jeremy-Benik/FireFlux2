# This will be the final code for analyzing the wrfout files
# %% Importing Libraries
import netCDF4 as nc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import os.path as osp
import wrf
# %% Setting the tower values
 # main tower
y_main = 190
x_main = 93

# East tower
y_east = 158
x_east = 117

# West tower
y_west = 151
x_west = 94

# South tower
y_south = 119
x_south = 115

# Now these are the subgrid coords

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


# %% Creating the plots
#format:
# Plotting the tower data
# Plotting the rolling average data
# Plotting the no fire data
# Plotting the fire data
# Setting x limits
# Creating x label
# Creating y label
# Creating Title
# Adding a grid
# Adding the legend
out_path = 'pressure_from_wrfouts.pkl' #To change the file, change this name
if not osp.exists(out_path):
    # %% Reading in the files
    fire_atms_0 = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_cheyenne/fire_atms_0/wrfout_d01_2013-01-30_15:00:00')
    fire_atms_1 = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_cheyenne/fire_atms_1/wrfout_d01_2013-01-30_15:00:00')

    time_fire_atms_0 = fire_atms_0.variables['XTIME'][:]
    time_fire_atms_1 = fire_atms_1.variables['XTIME'][:]

    print('Getting preserature from the no_fire run')
    pres_no_fire = wrf.getvar(fire_atms_0, "pressure", None)

    ht_no_fire = wrf.getvar(fire_atms_0, "z", units="m", msl = False)
    print('Getting preserature from the fire run') 
    pres_fire = wrf.getvar(fire_atms_1, "pressure", None)

    ht_fire = wrf.getvar(fire_atms_1, "z", units="m", msl = False)
    print('Interpolating the preserature at the tower heights')

    print('These will be for the no fire run')
    print('Interpolating preserature at 20 meters')
    pres_h_no_fire_20 = wrf.interplevel(pres_no_fire, pres_no_fire, 20)[:, y_main, x_main]
    print('Interpolating preserature at 10 meters')
    pres_h_no_fire_10 = wrf.interplevel(pres_no_fire, pres_no_fire, 10)[:, y_main, x_main]
    print('Interpolating height at 5.77 meters')
    pres_h_no_fire_577 = wrf.interplevel(pres_no_fire, pres_no_fire, 5.77)[:, y_main, x_main]

    # West tower
    print('Interpolating pres at 5.33 meters for west tower')
    west_pres_h_no_fire_533 = wrf.interplevel(pres_no_fire, pres_no_fire, 5.33)[:, y_west, x_west]

    # south tower
    print('Interpolating pres at 5.33 meters for south tower')
    south_pres_h_no_fire_533 = wrf.interplevel(pres_no_fire, pres_no_fire, 5.33)[:, y_south, x_south]

    # east tower
    print('Interpolating pres at 5.33 meters for east tower')
    east_pres_h_no_fire_528 = wrf.interplevel(pres_no_fire, pres_no_fire, 5.28)[:, y_east, x_east]


    # No fire

    # Main tower
    print('These will be for the fire run')
    print('Interpolating preserature at 20 meters')
    pres_h_fire_20 = wrf.interplevel(pres_fire, pres_fire, 20)[:, y_main, x_main]
    print('Interpolating preserature at 10 meters')
    pres_h_fire_10 = wrf.interplevel(pres_fire, pres_fire, 10)[:, y_main, x_main]
    print('Interpolating height at 5.77 meters')
    pres_h_fire_577 = wrf.interplevel(pres_fire, pres_fire, 5.77)[:, y_main, x_main]

    # West tower
    print('Interpolating pres at 5.33 meters for west tower')
    west_pres_h_fire_533 = wrf.interplevel(pres_fire, pres_fire, 5.33)[:, y_west, x_west]

    # south tower
    print('Interpolating pres at 5.33 meters for south tower')
    south_pres_h_fire_533 = wrf.interplevel(pres_fire, pres_fire, 5.33)[:, y_south, x_south]

    # east tower
    print('Interpolating pres at 5.33 meters for east tower')
    east_pres_h_fire_528 = wrf.interplevel(pres_fire, pres_fire, 5.28)[:, y_east, x_east]

    results = {'pres_h_no_fire_20':pres_h_no_fire_20, 'pres_h_no_fire_10':pres_h_no_fire_10, 'pres_h_no_fire_577':pres_h_no_fire_577,
    'pres_h_fire_20':pres_h_fire_20, 'pres_h_fire_10':pres_h_fire_10, 'pres_h_fire_577':pres_h_fire_577,
    'west_pres_h_no_fire_533':west_pres_h_no_fire_533, 'south_pres_h_no_fire_533':south_pres_h_no_fire_533, 'east_pres_h_no_fire_528':east_pres_h_no_fire_528,
    'west_pres_h_fire_533':west_pres_h_fire_533, 'south_pres_h_fire_533':south_pres_h_fire_533, 'east_pres_h_fire_528':east_pres_h_fire_528,
    'time_fire_atms_0':time_fire_atms_0, 'time_fire_atms_1':time_fire_atms_1} #put the other variables in here such as wsw and ww

    with open(out_path, 'wb') as f:
        pickle.dump(results, f)
else:
    with open(out_path, 'rb') as f:
        results = pickle.load(f)
    locals().update(results)
# %% Creating plots with all the data
time_main = np.arange(0, 720.1, .1)
# Main Tower Plot
fig, ax = plt.subplots(3, figsize = (12, 8))

# 20 meter calculated fire wind
ax[0].plot(time_fire_atms_1[0:774] * 60, pres_h_fire_20[0:774], color = 'red', label = '20 Meter Pressure (hPa)')
ax[0].plot(time_fire_atms_0[0:774] * 60, pres_h_no_fire_20[0:774], color = 'blue', label = '20 Meter No Fire Pressure (hPa)')
ax[0].legend()
ax[0].set_ylabel('Temperature (C)', fontsize = 12, fontweight = 'bold')
ax[0].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[0].grid()

# 10 meter calculated fire wind
ax[1].plot(time_fire_atms_1[0:774] * 60, pres_h_fire_10[0:774], color = 'red', label = '10 Meter Fire Pressure (hPa)')
ax[1].plot(time_fire_atms_0[0:774] * 60, pres_h_no_fire_10[0:774], color = 'blue', label = '10 Meter No Fire Pressure (hPa)')

ax[1].legend()
ax[1].set_ylabel('Pressure (hPa)', fontsize = 12, fontweight = 'bold')
ax[1].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[1].grid()
# 5.77 meter calculated fire wind
ax[2].plot(time_fire_atms_1[0:774] * 60, pres_h_fire_577[0:774], color = 'red', label = '5.77 Meter Fire Pressure (hPa)')
ax[2].plot(time_fire_atms_0[0:774] * 60, pres_h_no_fire_577[0:774], color = 'blue', label = '5.77 Meter No Fire Pressure (hPa)')
ax[2].legend()
ax[2].set_ylabel('Temperature (C)', fontsize = 12, fontweight = 'bold')
ax[2].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[2].grid()

plt.tight_layout()
plt.show()
# %%
