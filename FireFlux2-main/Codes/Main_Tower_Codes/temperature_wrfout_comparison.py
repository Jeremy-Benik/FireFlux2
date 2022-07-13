''' this program plots the temperature at the main tower'''
#The info below are the indices for the towers
'''Here are the results of this code for quick access if needed
None of these are staggered, these are just using the regular grid

Main tower
y for main tower is at: 190
x for main tower is: 93

East tower
y for east tower is at: 158
x for east tower is: 117

West tower
y for west tower is at: 151
West_west for west tower is: 94

South tower
y for south tower is at: 119
West_south for south tower is: 115

Fire mesh coordinates

Main tower
y for main tower is at: 1908
x for main tower is: 937

East tower
y for east tower is at: 1581
x for east tower is: 1173

West tower
y for west tower is at: 1511
West_west for west tower is: 943

South tower
y for south tower is at: 1199
West_south for south tower is: 1155 '''
# %% Importing libraries
print("importing libraries")
import pandas as pd
import netCDF4 as nc
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import wrf
import statistics as st
import glob
import pickle
import os.path as osp
out_path = 'main_tower_temp_wrfout_with_time_mod_vars.pkl' #To change the file, change this name
if not osp.exists(out_path):
    # %% Assigning tower coords
    #These values can be found in the code titled finding_towers_ideal.py. 
    # these values are not on the subgrid
    print('Setting indices for the towers')
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
    # %% Reading in the data
    print("Reading in the data")
    print("Main tower data")
    main_tower1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))

    main_tower = main_tower1.truncate(before= np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][0], 
                        after=np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:07:00')[0][0])
    # Wrfout file 
    print("Reading in the wrfout file from the ideal case")
    wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_cheyenne/run_8/wrfout_d01_2013-01-30_15:00:00', 'r')
 
    # %% Getting the variables from the files
    # Main tower variables
    print("Getting the variables from the main tower data")
    time_main_tower = main_tower['TIMESTAMP']
    time2 = np.arange(240, 420.01, .1)

    ts20 = main_tower['Ts_20m']

    ts10 = main_tower['Ts_10m']

    ts6 = main_tower['Ts_6m']
    # %% Variables from the wrfout file
    # To get the variables from thw wrfout file, I am using the wrf library to get them so they won't be staggered in the grid
    print('Getting Time from wrfout file')
    time = wrfout.variables['XTIME'][:]
    print('Getting temperature from the wrfout file')
    T_wrfout = wrf.getvar(wrfout, "temp", None, units = 'K')
    T_wrfout -= 273.15 #converting it to celcius
    print("Now I am getting height")
    ht = wrf.getvar(wrfout, "z", units="m", msl = False)
    # %% Interpolating the variables to specific heights

    # 20 meters
    print("Interpolating heights")
    print("Interpolating T at 20 meters")
    T_h_20 = wrf.interplevel(T_wrfout, ht, 20)[y_main, x_main]

    # 10 meters
    print("Interpolating U at 10 meters")
    T_h_10 = wrf.interplevel(T_wrfout, ht, 10)[y_main, x_main]
    # 5.77 meters
    print('Interpolating T at 5.77 meters')
    T_h_577 = wrf.interplevel(T_wrfout, ht, 5.77)[y_main, x_main]

    wrfout_time = wrfout.variables['XTIME'][:]
    # %% Saving the results into new file
    results = {'T_h_20':T_h_20, 'T_h_10':T_h_10, 'T_h_577':T_h_577, 
    'ts20':ts20, 'ts10':ts10, 'ts6':ts6, 'wrfout_time':wrfout_time} #put the other variables in here such as wsw and ww

    with open(out_path, 'wb') as f:
        pickle.dump(results, f)
else:
    with open(out_path, 'rb') as f:
        results = pickle.load(f)
    locals().update(results)

# %% Making the plots
#defining n which is the number of intervals for the rolling average
n = 10
#I chose 10 here since the data is taken at 10Hz, so this way I can see what it is like every second

print("Plotting")
fig, ax  = plt.subplots(1, 3, figsize = (15, 10))
plt.suptitle("Temperature (\N{DEGREE SIGN}C) at the Main tower comapred to the wrfout file", fontsize = 15, fontweight = 'bold')

# 20 meters
ax[0].plot(time2, ts20, color = 'green', label = 'Main tower Data')
ax[0].plot(time2, ts20.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[0].plot(np.array(wrfout.variables['XTIME'][240:420]) * 60, T_h_20, color = 'red', label = 'wrfout file')
#ax[1, 0].plot(np.array(wrfout.variables['XTIME'][:]), T_h_20.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[0].set_xlabel('Time (seconds)', fontsize = 12, fontweight = 'bold')
ax[0].set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 12, fontweight = 'bold')
ax[0].set_title("Temperature at 20 Meters", fontsize = 15, fontweight = 'bold')
ax[0].set_xlim(220, 420)
ax[0].legend()

ax[1].plot(time2, ts10, color = 'green', label = 'Main tower Data')
ax[1].plot(time2, ts10.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[1].plot(np.array(wrfout.variables['XTIME'][240:420]) * 60, T_h_10, color = 'red', label = 'wrfout file')
#ax[1, 1].plot(np.array(wrfout.variables['XTIME'][:]), T_h_10.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[1].set_xlabel('Time (seconds)', fontsize = 12, fontweight = 'bold')
ax[1].set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 12, fontweight = 'bold')
ax[1].set_title("Temperature at 10 Meters", fontsize = 15, fontweight = 'bold')
ax[1].set_xlim(220, 420)
ax[1].legend()

ax[2].plot(time2, ts6, color = 'green', label = 'Main tower Data')
ax[2].plot(time2, ts6.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[2].plot(np.array(wrfout.variables['XTIME'][240:420]) * 60, T_h_577, color = 'red', label = 'wrfout file')
#ax{1, 2].plot(np.array(wrfout.variables['XTIME'][:]), T_h_577.rolling(window = n).mean(), color = 'black', label = 'wrfout file')
ax[2].set_xlabel('Time (seconds)', fontsize = 12, fontweight = 'bold')
ax[2].set_ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize = 12, fontweight = 'bold')
ax[2].set_title("Temperature at 5.77 Meters", fontsize = 15, fontweight = 'bold')
ax[2].set_xlim(220, 420)
ax[2].legend()


ax[0].grid()
ax[1].grid()
ax[2].grid()


plt.tight_layout()
#plt.savefig('/home/jbenik/FireFlux2/Codes_and_Data/Data/images/wrfout_Main_Tower_temp_backfire_ros.png')
plt.show()
plt.pause(0.0001)
plt.close()
# %%
