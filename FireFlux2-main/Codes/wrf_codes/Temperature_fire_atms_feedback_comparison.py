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
out_path = 'temp_from_wrfouts.pkl' #To change the file, change this name
if not osp.exists(out_path):
    # %% Reading in the files
    fire_atms_0 = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_cheyenne/fire_atms_0/wrfout_d01_2013-01-30_15:00:00')
    fire_atms_1 = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_cheyenne/fire_atms_1/wrfout_d01_2013-01-30_15:00:00')

    time_fire_atms_0 = fire_atms_0.variables['XTIME'][:]
    time_fire_atms_1 = fire_atms_1.variables['XTIME'][:]
    # Getting temperature 
    print('Getting temperature from the no_fire run')
    temp_no_fire = wrf.getvar(fire_atms_0, "tc", None)

    ht_no_fire = wrf.getvar(fire_atms_0, "z", units="m", msl = False)
    print('Getting temperature from the fire run') 
    temp_fire = wrf.getvar(fire_atms_1, "tc", None)

    ht_fire = wrf.getvar(fire_atms_1, "z", units="m", msl = False)
    print('Interpolating the temperature at the tower heights')

    # No fire

    # Main tower
    print('These will be for the no fire run')
    print('Interpolating temperature at 20 meters')
    t_h_no_fire_20 = wrf.interplevel(temp_no_fire, ht_no_fire, 20)[:, y_main, x_main]
    print('Interpolating temperature at 10 meters')
    t_h_no_fire_10 = wrf.interplevel(temp_no_fire, ht_no_fire, 10)[:, y_main, x_main]
    print('Interpolating height at 5.77 meters')
    t_h_no_fire_577 = wrf.interplevel(temp_no_fire, ht_no_fire, 5.77)[:, y_main, x_main]

    # West tower
    print('Interpolating temp at 5.33 meters for west tower')
    west_t_h_no_fire_533 = wrf.interplevel(temp_no_fire, ht_no_fire, 5.33)[:, y_west, x_west]

    # south tower
    print('Interpolating temp at 5.33 meters for south tower')
    south_t_h_no_fire_533 = wrf.interplevel(temp_no_fire, ht_no_fire, 5.33)[:, y_south, x_south]

    # east tower
    print('Interpolating temp at 5.33 meters for east tower')
    east_t_h_no_fire_528 = wrf.interplevel(temp_no_fire, ht_no_fire, 5.28)[:, y_east, x_east]


    # No fire

    # Main tower
    print('These will be for the fire run')
    print('Interpolating temperature at 20 meters')
    t_h_fire_20 = wrf.interplevel(temp_fire, ht_fire, 20)[:, y_main, x_main]
    print('Interpolating temperature at 10 meters')
    t_h_fire_10 = wrf.interplevel(temp_fire, ht_fire, 10)[:, y_main, x_main]
    print('Interpolating height at 5.77 meters')
    t_h_fire_577 = wrf.interplevel(temp_fire, ht_fire, 5.77)[:, y_main, x_main]

    # West tower
    print('Interpolating temp at 5.33 meters for west tower')
    west_t_h_fire_533 = wrf.interplevel(temp_fire, ht_fire, 5.33)[:, y_west, x_west]

    # south tower
    print('Interpolating temp at 5.33 meters for south tower')
    south_t_h_fire_533 = wrf.interplevel(temp_fire, ht_fire, 5.33)[:, y_south, x_south]

    # east tower
    print('Interpolating temp at 5.33 meters for east tower')
    east_t_h_fire_528 = wrf.interplevel(temp_fire, ht_fire, 5.28)[:, y_east, x_east]


   # Reading in the data from the main tower
    print("Reading in the data")
    print("Main tower data")
    main_tower1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))

    main_tower = main_tower1.truncate(before= np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:00:00')[0][0], 
                        after=np.where(main_tower1['TIMESTAMP'] == '1/30/2013  15:12:00')[0][0])

    # %% Getting the variables from the files
    # Main tower variables
    print("Getting the variables from the main tower data")
    time_main_tower = main_tower['TIMESTAMP']
    time_main = np.arange(0, 720.01, .1)

    print('20 meter variables')
    ts20 = main_tower['Ts_20m']

    print('10 meter variables')
    ts10 = main_tower['Ts_10m']

    print('5.77 meter variable')
    ts6 = main_tower['Ts_6m']

    # Short Tower data
    df_w1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTWdespikedrotated.csv')

    df_w = df_w1.truncate(before= np.where(df_w1['TIMESTAMP'] == '1/30/2013 15:00')[0][0], 
                        after=np.where(df_w1['TIMESTAMP'] == '1/30/2013 15:12')[0][0])

    df_e1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTEdespikedrotated.csv')

    df_e = df_e1.truncate(before= np.where(df_e1['TIMESTAMP'] == '1/30/2013 15:00')[0][0], 
                        after=np.where(df_e1['TIMESTAMP'] == '1/30/2013 15:12')[0][0])

    df_s1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTSdespikedrotated.csv')

    df_s = df_s1.truncate(before= np.where(df_s1['TIMESTAMP'] == '1/30/2013 15:00')[0][0], 
                        after=np.where(df_s1['TIMESTAMP'] == '1/30/2013 15:12')[0][0])

    # defining vars

    #west tower
    print("Reading variables from west tower")
    time_short_tower_w = df_w['TIMESTAMP']
    tw = df_w['t']
    #east tower
    print("Reading in variables from east tower")
    time_short_tower_e = df_e['TIMESTAMP']
    te = df_e['t']
    #south tower
    print("reading in variables from south tower")
    time_short_tower_s = df_s['TIMESTAMP']
    ts = df_s['t']


    results = {'t_h_fire_20':t_h_fire_20, 't_h_fire_10':t_h_fire_10, 't_h_fire_577':t_h_fire_577,
    't_h_no_fire_20':t_h_no_fire_20, 't_h_no_fire_10':t_h_no_fire_10, 't_h_no_fire_577':t_h_no_fire_577,
    'west_t_h_fire_533':west_t_h_fire_533, 'south_t_h_fire_533':south_t_h_fire_533, 'east_t_h_fire_528':east_t_h_fire_528,
    'west_t_h_no_fire_533':west_t_h_no_fire_533, 'south_t_h_no_fire_533':south_t_h_no_fire_533, 'east_t_h_no_fire_528':east_t_h_no_fire_528,
    'ts20':ts20, 'ts10':ts10, 'ts6':ts6, 'tw':tw, 'te':te, 'ts':ts, 'time_fire_atms_0':time_fire_atms_0, 'time_fire_atms_1':time_fire_atms_1} #put the other variables in here such as wsw and ww

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
ax[0].plot(time_fire_atms_1[0:774] * 60, t_h_fire_20[0:774], color = 'red', label = '20 Meter Fire Temp (C)')
ax[0].plot(time_fire_atms_0[0:774] * 60, t_h_no_fire_20[0:774], color = 'blue', label = '20 Meter No Fire Temp (C)')
ax[0].legend()
ax[0].set_ylabel('Temperature (C)', fontsize = 12, fontweight = 'bold')
ax[0].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[0].grid()

# 10 meter calculated fire wind
ax[1].plot(time_fire_atms_1[0:774] * 60, t_h_fire_10[0:774], color = 'red', label = '10 Meter Fire Temp (C)')
ax[1].plot(time_fire_atms_0[0:774] * 60, t_h_no_fire_10[0:774], color = 'blue', label = '10 Meter No Fire Temp (C)')
ax[1].plot(time_main, ts10, color = 'green', label = '10m Observation Wind')

ax[1].legend()
ax[1].set_ylabel('Temperature (C)', fontsize = 12, fontweight = 'bold')
ax[1].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[1].grid()
# 5.77 meter calculated fire wind
ax[2].plot(time_fire_atms_1[0:774] * 60, t_h_fire_577[0:774], color = 'red', label = '5.77 Meter Fire Temp (C)')
ax[2].plot(time_fire_atms_0[0:774] * 60, t_h_no_fire_577[0:774], color = 'blue', label = '5.77 Meter No Fire Temp (C)')
ax[2].legend()
ax[2].set_ylabel('Temperature (C)', fontsize = 12, fontweight = 'bold')
ax[2].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[2].grid()

plt.tight_layout()
plt.show()

# %% Creating plots with all the data
time_main = np.arange(0, 720.1, .1)
# Main Tower Plot
fig, ax = plt.subplots(3, figsize = (12, 8))

# 20 meter calculated fire wind
ax[0].plot(time_fire_atms_1[0:774] * 60, t_h_fire_20[0:774], color = 'red', label = '20 Meter Fire Temp (C)')
ax[0].plot(time_fire_atms_0[0:774] * 60, t_h_no_fire_20[0:774], color = 'blue', label = '20 Meter No Fire Temp (C)')
ax[0].plot(time_main, ts20, color = 'green', label = '20m Observation Wind')
ax[0].legend()
ax[0].set_ylabel('Temperature (C)', fontsize = 12, fontweight = 'bold')
ax[0].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[0].grid()

# 10 meter calculated fire wind
ax[1].plot(time_fire_atms_1[0:774] * 60, t_h_fire_10[0:774], color = 'red', label = '10 Meter Fire Temp (C)')
ax[1].plot(time_fire_atms_0[0:774] * 60, t_h_no_fire_10[0:774], color = 'blue', label = '10 Meter No Fire Temp (C)')
ax[1].plot(time_main, ts10, color = 'green', label = '10m Observation Wind')
ax[1].legend()
ax[1].set_ylabel('Temperature (C)', fontsize = 12, fontweight = 'bold')
ax[1].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[1].grid()
# 5.77 meter calculated fire wind
ax[2].plot(time_fire_atms_1[0:774] * 60, t_h_fire_577[0:774], color = 'red', label = '5.77 Meter Fire Temp (C)')
ax[2].plot(time_fire_atms_0[0:774] * 60, t_h_no_fire_577[0:774], color = 'blue', label = '5.77 Meter No Fire Temp (C)')
ax[2].plot(time_main, ts6, color = 'green', label = '5.77m Observation Wind')
ax[2].legend()
ax[2].set_ylabel('Temperature (C)', fontsize = 12, fontweight = 'bold')
ax[2].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[2].grid()

plt.tight_layout()
plt.show()

# %% subtracting them to see what it looks like

time_main = np.arange(0, 720.1, .1)
# Main Tower Plot
fig, ax = plt.subplots(3, figsize = (12, 8))

# 20 meter calculated fire wind
ax[0].plot(time_fire_atms_1[0:774] * 60, abs(t_h_fire_20[0:774] - t_h_no_fire_20[0:774]), color = 'red', label = '20 Meter Fire Temp (C)')
ax[0].legend()
ax[0].set_ylabel('Temperature (C)', fontsize = 12, fontweight = 'bold')
ax[0].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[0].grid()

# 10 meter calculated fire wind
ax[1].plot(time_fire_atms_1[0:774] * 60, abs(t_h_fire_10[0:774] - t_h_no_fire_10[0:774]), color = 'red', label = '10 Meter Fire Temp (C)')
ax[1].legend()
ax[1].set_ylabel('Temperature (C)', fontsize = 12, fontweight = 'bold')
ax[1].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[1].grid()
# 5.77 meter calculated fire wind
ax[2].plot(time_fire_atms_1[0:774] * 60, abs(t_h_fire_577[0:774] - t_h_no_fire_577[0:774]), color = 'red', label = '5.77 Meter Fire Temp (C)')
ax[2].legend()
ax[2].set_ylabel('Temperature (C)', fontsize = 12, fontweight = 'bold')
ax[2].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[2].grid()

plt.tight_layout()
plt.show()

# %% subtracting them to see what it looks like

# %%
