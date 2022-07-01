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
out_path = 'winds_from_wrfouts_one_file_5.pkl' #To change the file, change this name
if not osp.exists(out_path):
    # %% Reading in the files
    fire_atms_0 = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_cheyenne/fire_atms_0/wrfout_d01_2013-01-30_15:00:00')
    fire_atms_1 = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_cheyenne/fire_atms_1/wrfout_d01_2013-01-30_15:00:00')

    # %% Reading in variables
    # Fire Variables
    print('Reading in time')
    time_fire = fire_atms_1.variables['XTIME'][:]

    print("I am getting the u variable from the wrfout file")
    u_fire = wrf.getvar(fire_atms_1, "ua", None, units = "m/s")

    print("I am getting the v variable from the wrfout file")
    v_fire = wrf.getvar(fire_atms_1, "va", None, units = "m/s")

    print("I am getting the w variable from the wrfout file")
    w_fire = wrf.getvar(fire_atms_1, "wa", None, units = "m/s")

    print('Now I am getting the height')
    ht_fire = wrf.getvar(fire_atms_1, "z", units="m", msl = False)

    #No fire variables
    print('Reading in time')
    time_no_fire = fire_atms_0.variables['XTIME'][:]

    print("I am getting the u variable from the wrfout file")
    u_no_fire = wrf.getvar(fire_atms_0, "ua", None, units = "m/s")

    print("I am getting the v variable from the wrfout file")
    v_no_fire = wrf.getvar(fire_atms_0, "va", None, units = "m/s")

    print("I am getting the w variable from the wrfout file")
    w_no_fire = wrf.getvar(fire_atms_0, "wa", None, units = "m/s")

    print('Now I am getting the height')
    ht_no_fire = wrf.getvar(fire_atms_0, "z", units="m", msl = False)


    # %% Interpolating the variables to specific heights

    # 20 meters

    #Fire
    print("Interpolating heights")
    print("Interpolating U at 20 meters")
    U_h_fire_20 = wrf.interplevel(u_fire, ht_fire, 20)[:, y_main, x_main] # Run this for all time
    print("Interpolating V at 20 meters")
    V_h_fire_20 = wrf.interplevel(v_fire, ht_fire, 20)[:, y_main, x_main]
    print("Calculating Wind Speed")
    ws_h_fire_20 = np.sqrt((U_h_fire_20 ** 2) + (V_h_fire_20 ** 2))
    print("Interpolating W at 20 meters")
    W_h_fire_20 = wrf.interplevel(w_fire, ht_fire, 20)[:, y_main, x_main]

    # No fire
    print("Interpolating heights for No fire")
    print("Interpolating U at 20 meters")
    U_h_no_fire_20 = wrf.interplevel(u_no_fire, ht_no_fire, 20)[:, y_main, x_main] # Run this for all time
    print("Interpolating V at 20 meters")
    V_h_no_fire_20 = wrf.interplevel(v_no_fire, ht_no_fire, 20)[:, y_main, x_main]
    print("Calculating Wind Speed")
    ws_h_no_fire_20 = np.sqrt((U_h_no_fire_20 ** 2) + (V_h_no_fire_20 ** 2))
    print("Interpolating W at 20 meters")
    W_h_no_fire_20 = wrf.interplevel(w_no_fire, ht_no_fire, 20)[:, y_main, x_main]

    # 10 meters
    #Fire
    print("Interpolating heights for 10 meters")
    print("Interpolating U at 10 meters")
    U_h_fire_10 = wrf.interplevel(u_fire, ht_fire, 10)[:, y_main, x_main] # Run this for all time
    print("Interpolating V at 10 meters")
    V_h_fire_10 = wrf.interplevel(v_fire, ht_fire, 10)[:, y_main, x_main]
    print("Calculating Wind Speed")
    ws_h_fire_10 = np.sqrt((U_h_fire_10 ** 2) + (V_h_fire_10 ** 2))
    print("Interpolating W at 10 meters")
    W_h_fire_10 = wrf.interplevel(w_fire, ht_fire, 10)[:, y_main, x_main]

    # No fire
    print("Interpolating heights for 10 meters no fire")
    print("Interpolating U at 10 meters")
    U_h_no_fire_10 = wrf.interplevel(u_no_fire, ht_no_fire, 10)[:, y_main, x_main] # Run this for all time
    print("Interpolating V at 10 meters")
    V_h_no_fire_10 = wrf.interplevel(v_no_fire, ht_no_fire, 10)[:, y_main, x_main]
    print("Calculating Wind Speed")
    ws_h_no_fire_10 = np.sqrt((U_h_no_fire_10 ** 2) + (V_h_no_fire_10 ** 2))
    print("Interpolating W at 10 meters")
    W_h_no_fire_10 = wrf.interplevel(w_no_fire, ht_no_fire, 10)[:, y_main, x_main]

    # 5.77 meters
    #Fire
    print("Interpolating heights at 5.77m")
    print("Interpolating U at 5.77 meters")
    U_h_fire_577 = wrf.interplevel(u_fire, ht_fire, 5.77)[:, y_main, x_main] # Run this for all time
    print("Interpolating V at 5.77 meters")
    V_h_fire_577 = wrf.interplevel(v_fire, ht_fire, 5.77)[:, y_main, x_main]
    print("Calculating Wind Speed")
    ws_h_fire_577 = np.sqrt((U_h_fire_577 ** 2) + (V_h_fire_577 ** 2))
    print("Interpolating W at 5.77 meters")
    W_h_fire_577 = wrf.interplevel(w_fire, ht_fire, 5.77)[:, y_main, x_main]

    # No fire
    print("Interpolating heights at 5.77m no fire")
    print("Interpolating U at 5.77 meters")
    U_h_no_fire_577 = wrf.interplevel(u_no_fire, ht_no_fire, 5.77)[:, y_main, x_main] # Run this for all time
    print("Interpolating V at 5.77 meters")
    V_h_no_fire_577 = wrf.interplevel(v_no_fire, ht_no_fire, 5.77)[:, y_main, x_main]
    print("Calculating Wind Speed")
    ws_h_no_fire_577 = np.sqrt((U_h_no_fire_577 ** 2) + (V_h_no_fire_577 ** 2))
    print("Interpolating W at 5.77 meters")
    W_h_no_fire_577 = wrf.interplevel(w_no_fire, ht_no_fire, 5.77)[:, y_main, x_main]

    #5.33 Meters

    # West Tower
    #Fire
    print("Interpolating heights at 5.33 meters for West")
    print("Interpolating U at 5.33 meters")
    West_U_h_fire_533 = wrf.interplevel(u_fire, ht_fire, 5.33)[:, y_west, x_west] # Run this for all time
    print("Interpolating V at 5.33 meters")
    West_V_h_fire_533 = wrf.interplevel(v_fire, ht_fire, 5.33)[:, y_west, x_west]
    print("Calculating Wind Speed")
    West_ws_h_fire_533 = np.sqrt((West_U_h_fire_533 ** 2) + (West_V_h_fire_533 ** 2))
    print("Interpolating W at 5.33 meters")
    West_W_h_fire_533 = wrf.interplevel(w_fire, ht_fire, 5.33)[:, y_west, x_west]

    # No fire
    print("Interpolating heights at 5.33 meters for west no fire")
    print("Interpolating U at 5.33 meters")
    West_U_h_no_fire_533 = wrf.interplevel(u_no_fire, ht_no_fire, 5.33)[:, y_west, x_west] # Run this for all time
    print("Interpolating V at 5.33 meters")
    West_V_h_no_fire_533 = wrf.interplevel(v_no_fire, ht_no_fire, 5.33)[:, y_west, x_west]
    print("Calculating Wind Speed")
    West_ws_h_no_fire_533 = np.sqrt((West_U_h_no_fire_533 ** 2) + (West_V_h_no_fire_533 ** 2))
    print("Interpolating W at 5.33 meters")
    West_W_h_no_fire_533 = wrf.interplevel(w_no_fire, ht_no_fire, 5.33)[:, y_west, x_west]


    # south Tower
    #Fire
    print("Interpolating heights at 5.33 meters for south tower")
    print("Interpolating U at 5.33 meters")
    south_U_h_fire_533 = wrf.interplevel(u_fire, ht_fire, 5.33)[:, y_south, x_south] # Run this for all time
    print("Interpolating V at 5.33 meters")
    south_V_h_fire_533 = wrf.interplevel(v_fire, ht_fire, 5.33)[:, y_south, x_south]
    print("Calculating Wind Speed")
    south_ws_h_fire_533 = np.sqrt((south_U_h_fire_533 ** 2) + (south_V_h_fire_533 ** 2))
    print("Interpolating W at 5.33 meters")
    south_W_h_fire_533 = wrf.interplevel(w_fire, ht_fire, 5.33)[:, y_south, x_south]

    # No fire
    print("Interpolating heights at 5.33 meters for south tower no fire")
    print("Interpolating U at 5.33 meters")
    south_U_h_no_fire_533 = wrf.interplevel(u_no_fire, ht_no_fire, 5.33)[:, y_south, x_south] # Run this for all time
    print("Interpolating V at 5.33 meters")
    south_V_h_no_fire_533 = wrf.interplevel(v_no_fire, ht_no_fire, 5.33)[:, y_south, x_south]
    print("Calculating Wind Speed")
    south_ws_h_no_fire_533 = np.sqrt((south_U_h_no_fire_533 ** 2) + (south_V_h_no_fire_533 ** 2))
    print("Interpolating W at 5.33 meters")
    south_W_h_no_fire_533 = wrf.interplevel(w_no_fire, ht_no_fire, 5.33)[:, y_south, x_south]


    # East Tower (5.28 meters)
    #Fire
    print("Interpolating heights at 5.28 meters for east tower")
    print("Interpolating U at 5.28 meters")
    east_U_h_fire_528 = wrf.interplevel(u_fire, ht_fire, 5.28)[:, y_east, x_east] # Run this for all time
    print("Interpolating V at 5.28 meters")
    east_V_h_fire_528 = wrf.interplevel(v_fire, ht_fire, 5.28)[:, y_east, x_east]
    print("Calculating Wind Speed")
    east_ws_h_fire_528 = np.sqrt((east_U_h_fire_528 ** 2) + (east_V_h_fire_528 ** 2))
    print("Interpolating W at 5.28 meters")
    east_W_h_fire_528 = wrf.interplevel(w_fire, ht_fire, 5.28)[:, y_east, x_east]

    # No fire
    print("Interpolating heights at 5.28 meters for east tower no fire")
    print("Interpolating U at 5.28 meters")
    east_U_h_no_fire_528 = wrf.interplevel(u_no_fire, ht_no_fire, 5.28)[:, y_east, x_east] # Run this for all time
    print("Interpolating V at 5.28 meters")
    east_V_h_no_fire_528 = wrf.interplevel(v_no_fire, ht_no_fire, 5.28)[:, y_east, x_east]
    print("Calculating Wind Speed")
    east_ws_h_no_fire_528 = np.sqrt((east_U_h_no_fire_528 ** 2) + (east_V_h_no_fire_528 ** 2))
    print("Interpolating W at 5.28 meters")
    east_W_h_no_fire_528 = wrf.interplevel(w_no_fire, ht_no_fire, 5.28)[:, y_east, x_east]
    # %% Saving the results into new file


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
    ux20 = main_tower['Ux_20m']
    uy20 = main_tower['Uy_20m']
    ws_20 = np.sqrt((ux20 ** 2) + (uy20 ** 2))
    uz20 = main_tower['Uz_20m']
    ts20 = main_tower['Ts_20m']

    print('10 meter variables')
    ux10 = main_tower['Ux_10m']
    uy10 = main_tower['Uy_10m']
    ws_10 = np.sqrt((ux10 ** 2) + (uy10 ** 2))
    uz10 = main_tower['Uz_10m']
    ts10 = main_tower['Ts_10m']

    print('5.77 meter variable')
    ux6 = main_tower['Ux_6m']
    uy6 = main_tower['Uy_6m']
    ws_6 = np.sqrt((ux6 ** 2) + (uy6 ** 2))
    uz6 = main_tower['Uz_6m']
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

    time_short = np.arange(0, 720)
    results = {'time_fire':time_fire, 'time_no_fire':time_no_fire,
    'ws_h_fire_20':ws_h_fire_20, 'W_h_fire_20':W_h_fire_20, 
    'ws_h_fire_10':ws_h_fire_10, 'W_h_fire_10':W_h_fire_10,
    'ws_h_fire_577':ws_h_fire_577, 'W_h_fire_577':W_h_fire_577,
    'ws_h_no_fire_20':ws_h_no_fire_20, 'W_h_no_fire_20':W_h_no_fire_20, 
    'ws_h_no_fire_10':ws_h_no_fire_10, 'W_h_no_fire_10':W_h_no_fire_10,
    'ws_h_no_fire_577':ws_h_no_fire_577, 'W_h_no_fire_577':W_h_no_fire_577,
    'West_ws_h_fire_533':West_ws_h_fire_533, 'West_W_h_fire_533':West_W_h_fire_533,
    'West_ws_h_no_fire_533':West_ws_h_no_fire_533, 'West_W_h_no_fire_533':West_W_h_no_fire_533,
    'south_ws_h_fire_533':south_ws_h_fire_533, 'south_W_h_fire_533':south_W_h_fire_533,
    'south_ws_h_no_fire_533':south_ws_h_no_fire_533, 'south_W_h_no_fire_533':south_W_h_no_fire_533,
    'east_ws_h_fire_528':east_ws_h_fire_528, 'east_W_h_fire_528':east_W_h_fire_528,
    'east_ws_h_no_fire_528':east_ws_h_no_fire_528, 'east_W_h_no_fire_528':east_W_h_no_fire_528,
    'ws_20':ws_20, 'ws_10':ws_10,'ws_6':ws_6, 'uz20':uz20, 'uz10':uz10, 'uz6':uz6,
    'wsw':wsw, 'ww':ww, 'wss':wss, 'ws':ws, 'wse':wse, 'we':we,
    'time_main':time_main, 'time_short':time_short} #put the other variables in here such as wsw and ww

    with open(out_path, 'wb') as f:
        pickle.dump(results, f)
else:
    with open(out_path, 'rb') as f:
        results = pickle.load(f)
    locals().update(results)

# %% Finding when the fire front passages occur to then use them to show on the graphs
df = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_cheyenne/fire_atms_1/wrfout_d01_2013-01-30_15:00:00')

print('Reading in Heat Fluxes')
f = df.variables['FGRNHFX'][:, :, :]
g = df.variables['GRNHFX'][:, :, :]
# Main Tower
FFP_Main = np.where(g[:, y_main, x_main] > 0)[0][0]
FFP_Main_sub = np.where(f[:, y_main_sub, x_main_sub] > 0)[0][0]

# South Tower
FFP_South = np.where(g[:, y_south, x_south] > 0)[0][0]
FFP_South_sub = np.where(f[:, y_south_sub, x_south_sub] > 0)[0][0]

# East Tower
FFP_East = np.where(g[:, y_east, x_east] > 0)[0][0]
FFP_East_sub = np.where(f[:, y_east_sub, x_east_sub] > 0)[0][0]

# West Tower
FFP_West = np.where(g[:, y_west, x_west] > 0)[0][0]
FFP_West_sub = np.where(f[:, y_west_sub, x_west_sub] > 0)[0][0]

time_main = np.arange(0, 720.01, .1)
# %% Creating plots with all the data

# Main Tower Plot
fig = plt.figure(figsize = (12, 8))

# 20 meter calculated fire wind
plt.plot(time_fire * 60, abs(ws_h_fire_20[0:774] - ws_h_no_fire_20[0:774]), color = 'red', label = '20 Meter Wind (m/s)')

# 10 Meter calculated fire wind
plt.plot(time_fire * 60, abs(ws_h_fire_10[0:774] - ws_h_no_fire_10[0:774]), color = 'blue', label = '10 Meter Wind (m/s)')

# 5.77 Meter calculated fire wind
plt.plot(time_fire * 60, abs(ws_h_fire_577[0:774] - ws_h_no_fire_577[0:774]), color = 'green', label = '5.77 Meter Wind (m/s)')

plt.axvline(x = FFP_Main, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
#Making the plot look nice
plt.xlabel('Time (seconds)', fontsize = 12, fontweight = 'bold')
plt.ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
plt.title('Simulated Fire Wind From FF2 Simulations', fontsize = 18, fontweight = 'bold')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

# %% Main tower plot with observations
fig, ax = plt.subplots(3, figsize = (12, 8))

# 20 Meter plot with observations
ax2 = ax[0].twinx()
#Main tower
ax1 = ax[0].plot(time_main, ws_20, color = 'blue', label = '20m Main Tower Winds (m/s)')
#wrfout file
ax3 = ax2.plot(time_fire * 60, abs(ws_h_fire_20[0:774] - ws_h_no_fire_20[0:774]), color = 'red', label = '20 Meter Fire Wind (m/s)')
# Making the plot look nice
ax[0].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax2.set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[0].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[0].set_title('20 Meter Observed Total Winds vs. Simulated Fire Winds', fontsize = 18, fontweight = 'bold')
ax[0].grid()
#ax[0].legend()
ax[0].axvline(x = FFP_Main, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
ax4 = ax[0].plot(FFP_Main, 2, color = 'black', label = 'Simulated Fire Front Passage')
label = ax1 + ax3 + ax4
labels = [i.get_label() for i in label]
ax[0].legend(label, labels, prop={'size': 8}, loc = 3)

# 10 Meter plot with observations
ax2 = ax[1].twinx()
#Main tower
ax1 = ax[1].plot(time_main, ws_10, color = 'blue', label = '10m Main Tower Winds (m/s)')
#wrfout file
ax3 = ax2.plot(time_fire * 60, abs(ws_h_fire_10[0:774] - ws_h_no_fire_10[0:774]), color = 'red', label = '10 Meter Fire Wind (m/s)')
# Making the plot look nice
ax[1].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax2.set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[1].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[1].set_title('10 Meter Observed Winds vs. Simulated Fire Winds', fontsize = 18, fontweight = 'bold')
ax[1].grid()
ax[1].legend()
ax[1].axvline(x = FFP_Main, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
ax4 = ax[1].plot(FFP_Main, 2, color = 'black', label = 'Simulated Fire Front Passage')

label = ax1 + ax3 + ax4
labels = [i.get_label() for i in label]
ax[1].legend(label, labels, prop={'size': 8}, loc = 3)

# 5.77 Meter plot with observations
ax2 = ax[2].twinx()
#Main tower
ax1 = ax[2].plot(time_main, ws_6, color = 'blue', label = '5.77m Main Tower Winds (m/s)')
#wrfout file
ax3 = ax2.plot(time_fire * 60, abs(ws_h_fire_577[0:774] - ws_h_no_fire_577[0:774]), color = 'red', label = '5.77 Meter Fire Wind (m/s)')
# Making the plot look nice
ax[2].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax2.set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[2].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[2].set_title('5.77 Meter Observed Winds vs. Simulated Fire Winds', fontsize = 18, fontweight = 'bold')
ax[2].grid()
ax[2].legend()
ax[2].axvline(x = FFP_Main, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
ax4 = ax[2].plot(FFP_Main, 2, color = 'black', label = 'Simulated Fire Front Passage')
label = ax1 + ax3 + ax4
labels = [i.get_label() for i in label]
ax[2].legend(label, labels, prop={'size': 8}, loc = 1)

plt.tight_layout()
plt.show()


# %% Plotting the short towers without observations
fig, ax = plt.subplots(3, figsize = (12, 8))
time_short = np.arange(0, 744)

# West Tower plot with observations
#wrfout file
ax[0].plot(time_fire * 60, abs(West_ws_h_fire_533[0:774] - West_ws_h_no_fire_533[0:774]), color = 'red', label = 'West Tower Fire Wind (m/s)')
# Making the plot look nice
ax[0].axvline(FFP_West, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')

ax[0].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
#ax2.set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[0].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[0].set_title('West Tower Simulated Fire Winds', fontsize = 18, fontweight = 'bold')
ax[0].grid()
ax[0].legend()


# South Tower
#wrfout file
ax1 = ax[1].plot(time_fire * 60, abs(south_ws_h_fire_533[0:774] - south_ws_h_no_fire_533[0:774]), color = 'red', label = 'South Tower Fire Wind (m/s)')
ax[1].axvline(FFP_South, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
# Making the plot look nice
ax[1].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[1].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[1].set_title('South Tower Simulated Fire Winds', fontsize = 18, fontweight = 'bold')
ax[1].grid()
ax[1].legend()


# East Tower
ax[2].plot(time_fire * 60, abs(east_ws_h_fire_528[0:774] - east_ws_h_no_fire_528[0:774]), color = 'red', label = 'East Tower Fire Wind (m/s)')
#ax2 = ax[2].plot(460, 2, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
ax[2].axvline(FFP_East, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
# Making the plot look nice
ax[2].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
#ax2.set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[2].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[2].set_title('East Tower Simulated Fire Winds', fontsize = 18, fontweight = 'bold')
ax[2].grid()
ax[2].legend()

plt.tight_layout()
plt.show()
# %% Plotting the short towers with observations
fig, ax = plt.subplots(3, figsize = (12, 8))
time_short = np.arange(0, 721)


# West Tower plot with observations
ax2 = ax[0].twinx()
#West tower
ax1 = ax[0].plot(time_short, wsw, color = 'blue', label = 'West Tower Winds (m/s)')
#wrfout file
ax3 = ax2.plot(time_fire * 60, abs(West_ws_h_fire_533[0:774] - West_ws_h_no_fire_533[0:774]), color = 'red', label = 'West Tower Fire Winds (m/s)')
ax[0].axvline(FFP_West, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
ax4 = ax[0].plot(FFP_West, 2, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
# Making the plot look nice
ax[0].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax2.set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[0].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[0].set_title('West Tower Observed Total Winds vs. Simulated Fire Winds', fontsize = 18, fontweight = 'bold')
ax[0].grid()
#ax[0].legend()
label = ax1 + ax3 + ax4
labels = [i.get_label() for i in label]
leg = ax[0].legend(label, labels, prop={'size': 8}, loc = 3)


# South Tower
ax2 = ax[1].twinx()
#south tower
ax1 = ax[1].plot(np.arange(0, 671), wss, color = 'blue', label = 'South Tower Winds (m/s)')
#wrfout file
ax3 = ax2.plot(time_fire * 60, abs(south_ws_h_fire_533[0:774] - south_ws_h_no_fire_533[0:774]), color = 'red', label = 'South Tower Fire Wind (m/s)')
ax[1].axvline(FFP_South, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
ax4 = ax[1].plot(FFP_South, 2, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
# Making the plot look nice
ax[1].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax2.set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[1].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[1].set_title('South Tower Observed Total Winds vs. Simulated Fire Winds', fontsize = 18, fontweight = 'bold')
ax[1].grid()
ax[1].legend()
label = ax1 + ax3 + ax4
labels = [i.get_label() for i in label]
leg = ax[1].legend(label, labels, prop={'size': 8})

# East Tower
ax2 = ax[2].twinx()
#east tower
ax1 = ax[2].plot(time_short, wse, color = 'blue', label = 'East Tower Winds (m/s)')
#wrfout file
ax3 = ax2.plot(time_fire * 60, abs(east_ws_h_fire_528[0:774] - east_ws_h_no_fire_528[0:774]), color = 'red', label = 'East Tower Fire Wind (m/s)')
ax[2].axvline(FFP_East, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
ax4 = ax[2].plot(FFP_East, 2, color = 'black', label = 'Simulated Fire Front Passage', linewidth = 3, linestyle = '--')
# Making the plot look nice
ax[2].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax2.set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[2].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[2].set_title('East Tower Observed Total Winds vs. Simulated Fire Winds', fontsize = 18, fontweight = 'bold')
ax[2].grid()
ax[2].legend()
label = ax1 + ax3 + ax4
labels = [i.get_label() for i in label]
leg = ax[2].legend(label, labels, prop={'size': 8}, loc = 3)

plt.tight_layout()
plt.show()
# %%
