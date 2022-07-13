''' This code will plot the variables at the short tower compared to the wrfout file'''
#The information below is the indicies for the short towers

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
out_path = 'short_tower_winds_wrfout_no_fire.pkl' #To change the file, change this name
if not osp.exists(out_path):

    # %% Assigning tower coords
    #These values can be found in the code titled finding_towers_ideal.py. 
    # these values are not on the subgrid
    print('Setting indicies for the towers')
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
    # Wrfout file 
    print("Reading in the wrfout file from the ideal case")
    wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_cheyenne/fire_atms_0/wrfout_d01_2013-01-30_15:00:00', 'r')


    # %% Variables from the wrfout file
    # To get the variables from thw wrfout file, I am using the wrf library to get them so they won't be staggered in the grid
    print('Reading in time from the wrfout file')
    time = wrfout.variables['XTIME'][:]
    print("I am getting the u variable from the wrfout file")
    u_wrfout = wrf.getvar(wrfout, "ua", None, units = "m/s")
    print("U wind is done, now I am getting the V wind")
    v_wrfout = wrf.getvar(wrfout, "va", None, units = "m/s")
    print("V wind is done, now I am getting the W wind")
    w_wrfout = wrf.getvar(wrfout, "wa", None, units = "m/s")
    print("Now I am getting height")
    ht = wrf.getvar(wrfout, "z", units="m", msl = False)
    # %% Short towers
    print('Reading in the short tower data')
    n = 5 #this is a 5 second average of the data
    df_w1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTWdespikedrotated.csv')

    df_w = df_w1.truncate(before= np.where(df_w1['TIMESTAMP'] == '1/30/2013 15:04')[0][0], 
                        after=np.where(df_w1['TIMESTAMP'] == '1/30/2013 15:14')[0][0])

    df_e1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTEdespikedrotated.csv')

    df_e = df_e1.truncate(before= np.where(df_e1['TIMESTAMP'] == '1/30/2013 15:04')[0][0], 
                        after=np.where(df_e1['TIMESTAMP'] == '1/30/2013 15:14')[0][0])

    df_s1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTSdespikedrotated.csv')

    df_s = df_s1.truncate(before= np.where(df_s1['TIMESTAMP'] == '1/30/2013 15:04')[0][0], 
                        after=np.where(df_s1['TIMESTAMP'] == '1/30/2013 15:14')[0][0])

    # defining vars

    #west tower
    print("Reading variables from west tower")
    time_short_tower_w = df_w['TIMESTAMP']
    uw = df_w['u']
    vw = df_w['v']
    ww = df_w['w']
    tw = df_w['t']
    wsw = np.sqrt((uw ** 2) + (vw ** 2))
    #east tower
    print("Reading in variables from east tower")
    time_short_tower_e = df_e['TIMESTAMP']
    ue = df_e['u']
    ve = df_e['v']
    we = df_e['w']
    te = df_e['t']
    wse = np.sqrt((ue ** 2) + (ve ** 2))
    #south tower
    print("reading in variables from south tower")
    time_short_tower_s = df_s['TIMESTAMP']
    us = df_s['u']
    vs = df_s['v']
    ws = df_s['w']
    ts = df_s['t']
    wss = np.sqrt((us ** 2) + (vs ** 2))

    short_tower_time = np.arange(240, 841)
    # Interpolating the vars to heights and defining the location of them
    #west tower is at 5.33m
    #east tower is at 5.28 meters
    #south tower is at 5.33m
    # %% Getting locations of the towers then assigning variables to them

    #west tower
    print('Interpolating west tower at 5.33 meters')
    Uw_h_533 = wrf.interplevel(u_wrfout, ht, 5.33)[:, y_west, x_west]
    Vw_h_533 = wrf.interplevel(v_wrfout, ht, 5.33)[:, y_west, x_west]
    wsw_h_533 = np.sqrt((Uw_h_533 ** 2) + (Vw_h_533 ** 2))
    Ww_h_533 = wrf.interplevel(w_wrfout, ht, 5.33)[:, y_west, x_west]

    #east tower
    print('Interpolating the east tower at 5.28 meters')
    Ue_h_528 = wrf.interplevel(u_wrfout, ht, 5.28)[:, y_east, x_east]
    Ve_h_528 = wrf.interplevel(v_wrfout, ht, 5.28)[:, y_east, x_east]
    wse_h_528 = np.sqrt((Ue_h_528 ** 2) + (Ve_h_528 ** 2))
    We_h_528 = wrf.interplevel(w_wrfout, ht, 5.28)[:, y_east, x_east]

    #south tower
    print('interpolating the south tower at 5.33 meters')
    Us_h_533 = wrf.interplevel(u_wrfout, ht, 5.33)[:, y_south, x_south]
    Vs_h_533 = wrf.interplevel(v_wrfout, ht, 5.33)[:, y_south, x_south]
    wss_h_533 = np.sqrt((Us_h_533 ** 2) + (Vs_h_533 ** 2))
    Ws_h_533 = wrf.interplevel(w_wrfout, ht, 5.33)[:, y_south, x_south]


    wrfout_time = wrfout.variables['XTIME'][:]

    # %% Saving the results into new file
    results = {'wsw_h_533':wsw_h_533, 'Ww_h_533':Ww_h_533, 'wse_h_528':wse_h_528, 
    'We_h_528':We_h_528, 'wss_h_533':wss_h_533, 'Ws_h_533':Ws_h_533, 'wsw':wsw, 
    'ww':ww, 'wss':wss, 'ws':ws, 'wse':wse, 'we':we, 'wrfout_time':wrfout_time} #put the other variables in here such as wsw and ww

    with open(out_path, 'wb') as f:
        pickle.dump(results, f)
else:
    with open(out_path, 'rb') as f:
        results = pickle.load(f)
    locals().update(results)
# %% Creating a plot for the short towers
n = 5
times = wrfout_time * 60
short_tower_time = np.arange(240, 841)
print("Creating the plot")
fig, ax = plt.subplots(3, 2, figsize = (15, 12))
plt.suptitle('Short Tower Winds Compared to wrfout File', fontsize = 15, fontweight = 'bold')
# Plotting the west tower first
#wind speed
ax[0, 0].plot(short_tower_time, wsw, color = 'blue', label = 'West Tower') #plotting the wind speed from west tower
ax[0, 0].plot(short_tower_time, wsw.rolling(window = n).mean(), color = 'black', linestyle = '--', label = '5s Rolling Average') #plotting the rolling average from the west tower wind speed
ax[0, 0].plot(times, wsw_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[0, 0].set_xlabel('Time (Seconds)', fontsize = 12)
ax[0, 0].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[0, 0].set_title('West Tower Wind Speed vs. wrfout', fontsize = 12, fontweight = 'bold')
ax[0, 0].legend()
# w wind
ax[0, 1].plot(short_tower_time, ww, color = 'blue', label = 'West Tower') #plotting the wind speed from west tower
ax[0, 1].plot(short_tower_time, ww.rolling(window = n).mean(), color = 'black', linestyle = '--', label = '5s Rolling Average') #plotting the rolling average from the west tower wind speed
ax[0, 1].plot(times, Ww_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[0, 1].set_xlabel('Time (Seconds)', fontsize = 12)
ax[0, 1].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[0, 1].set_title('West Tower W Wind vs. wrfout', fontsize = 12, fontweight = 'bold')
ax[0, 1].legend()

# Plotting the South Tower
#wind speed
ax[1, 0].plot(short_tower_time, wss, color = 'blue', label = 'South Tower') #plotting the wind speed from South tower
ax[1, 0].plot(short_tower_time, wss.rolling(window = n).mean(), color = 'black', label = '5s Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 0].plot(times, wss_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[1, 0].set_xlabel('Time (Seconds)', fontsize = 12)
ax[1, 0].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[1, 0].set_title('South Tower Wind Speed vs. wrfout', fontsize = 12, fontweight = 'bold')
ax[1, 0].legend()

# w wind
ax[1, 1].plot(short_tower_time, ws, color = 'blue', label = 'South Tower') #plotting the wind speed from South tower
ax[1, 1].plot(short_tower_time, ws.rolling(window = n).mean(), color = 'black', label = '5s Rolling Average') #plotting the rolling average from the South tower wind speed
ax[1, 1].plot(times, Ws_h_533, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[1, 1].set_xlabel('Time (Seconds)', fontsize = 12)
ax[1, 1].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[1, 1].set_title('South Tower W Wind vs. wrfout', fontsize = 12, fontweight = 'bold')
ax[1, 1].legend()

# Plotting the East Tower
#wind speed
ax[2, 0].plot(short_tower_time, wse, color = 'blue', label = 'East Tower') #plotting the wind speed from South tower
ax[2, 0].plot(short_tower_time, wse.rolling(window = n).mean(), color = 'black', label = '5s Rolling Average') #plotting the rolling average from the South tower wind speed
ax[2, 0].plot(times, wse_h_528, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[2, 0].set_xlabel('Time (Seconds)', fontsize = 12)
ax[2, 0].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[2, 0].set_title('East Tower Wind Speed vs. wrfout', fontsize = 12, fontweight = 'bold')
ax[2, 0].legend()

# w wind
ax[2, 1].plot(short_tower_time, we, color = 'blue', label = 'East Tower') #plotting the wind speed from South tower
ax[2, 1].plot(short_tower_time, we.rolling(window = n).mean(), color = 'black', label = '5s Rolling Average') #plotting the rolling average from the South tower wind speed
ax[2, 1].plot(times, We_h_528, color = 'red', label = 'wrfout file') #plotting the wind speed from the wrfout file
ax[2, 1].set_xlabel('Time (Seconds)', fontsize = 12)
ax[2, 1].set_ylabel('Wind Speed (m/s)', fontsize = 12)
ax[2, 1].set_title('East Tower W Wind vs. wrfout', fontsize = 12, fontweight = 'bold')
ax[2, 1].legend()

ax[0, 0].grid()
ax[0, 1].grid()
ax[1, 0].grid()
ax[1, 1].grid()
ax[2, 0].grid()
ax[2, 1].grid()

plt.tight_layout()
#plt.savefig('/home/jbenik/FireFlux2/Codes_and_Data/Data/images/wrfout_short_towers_wind_ideal_new_backfire.png')
plt.show()
plt.close() 
# %%
