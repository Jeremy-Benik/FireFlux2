# %% Importing necessary Libraries
import netCDF4 as nc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import os.path as osp
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
# %% Reading in the pickle files to import the variables
no_fire_main = '/home/jbenik/FireFlux2/Codes_and_Data/Codes/Main_Tower_Codes/main_tower_winds_wrfout_no_fire_atms_new_vars_1.pkl'
fire_main = '/home/jbenik/FireFlux2/Codes_and_Data/Codes/Main_Tower_Codes/main_tower_winds_wrfout.pkl'
fire_short = '/home/jbenik/FireFlux2/Codes_and_Data/Codes/Short_Tower_code/short_tower_winds_wrfout_1.pkl'
no_fire_short = '/home/jbenik/FireFlux2/Codes_and_Data/Codes/Short_Tower_code/short_tower_winds_wrfout_no_fire.pkl'
with open(no_fire_main, 'rb') as a:
    results_no_fire = pickle.load(a)
locals().update(results_no_fire)

with open(fire_main, 'rb') as b:
    results_fire = pickle.load(b)
locals().update(results_fire)
time_towers = np.arange(240, 420.01, .1)

with open(fire_short, 'rb') as c:
    results_fire_short = pickle.load(c)
locals().update(results_fire_short)

with open(no_fire_short, 'rb') as d:
    results_no_fire_short = pickle.load(d)
locals().update(results_no_fire_short)


# %% All the variable names so I can find them and they are easier to work with
'''results = {'ws_h_20_no_fire':ws_h_20_no_fire, 'W_h_20_no_fire':W_h_20_no_fire, 
    'ws_h_10_no_fire':ws_h_10_no_fire, 'W_h_10_no_fire':W_h_10_no_fire,
    'ws_h_577_no_fire':ws_h_577_no_fire, 'W_h_577_no_fire':W_h_577_no_fire, 'ws_20':ws_20, 'ws_10':ws_10,
    'ws_6':ws_6, 'uz20':uz20, 'uz10':uz10, 'uz6':uz6, 'wrfout_time_no_fire':wrfout_time_no_fire}
        
    results = {'wsw_h_533':wsw_h_533, 'Ww_h_533':Ww_h_533, 'wse_h_528':wse_h_528, 
    'We_h_528':We_h_528, 'wss_h_533':wss_h_533, 'Ws_h_533':Ws_h_533, 'wsw':wsw, 
    'ww':ww, 'wss':wss, 'ws':ws, 'wse':wse, 'we':we, 'wrfout_time':wrfout_time} #put the other variables in here such as wsw and ww
'''
# %% Reading in the fire winds

out_path = 'fire_winds.pkl' #To change the file, change this name
if not osp.exists(out_path):
    wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_d01_2013-01-30_15:00:00', 'r')
    
    # Main Tower
    print("I am getting the u variable from the wrfout file")
    print('getting uf winds')
    uf_main = wrfout.variables['UF'][:, y_main_sub, x_main_sub]
    print('getting vf winds')
    vf_main = wrfout.variables['VF'][:, y_main_sub, x_main_sub]
    wind_fire_fire_main = np.sqrt((uf_main ** 2) + (vf_main ** 2))

    # East Tower
    # To get the variables from thw wrfout file, I am using the wrf library to get them so they won't be staggered in the grid
    print("I am getting the u variable from the wrfout file")
    print('getting uf winds for east tower')
    uf_e = wrfout.variables['UF'][:, y_east_sub, x_east_sub]
    print('getting vf winds for east tower')
    vf_e = wrfout.variables['VF'][:, y_east_sub, x_east_sub]
    wind_fire_fire_east = np.sqrt((uf_e ** 2) + (vf_e ** 2))

    # West Tower
    print('getting uf winds for west tower')
    uf_w = wrfout.variables['UF'][:, y_west_sub, x_west_sub]
    print('getting vf winds for west tower')
    vf_w = wrfout.variables['VF'][:, y_west_sub, x_west_sub]
    wind_fire_fire_west = np.sqrt((uf_w ** 2) + (vf_w ** 2))

    # south Tower
    print('getting uf winds for south tower')
    uf_s = wrfout.variables['UF'][:, y_south_sub, x_south_sub]
    print('getting vf winds for south tower')
    vf_s = wrfout.variables['VF'][:, y_south_sub, x_south_sub]
    wind_fire_fire_south = np.sqrt((uf_w ** 2) + (vf_w ** 2))

    # Short tower no fire winds
    wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_cheyenne/fire_atms_0/wrfout_d01_2013-01-30_15:00:00', 'r')
    # Change this file back to the old one since the new landuse tbl
    # Main Tower
    print("I am getting the u variable from the wrfout file")
    print('getting uf winds')
    uf_main = wrfout.variables['UF'][:, y_main_sub, x_main_sub]
    print('getting vf winds')
    vf_main = wrfout.variables['VF'][:, y_main_sub, x_main_sub]
    wind_fire_no_fire_main = np.sqrt((uf_main ** 2) + (vf_main ** 2))

    # East Tower
    # To get the variables from thw wrfout file, I am using the wrf library to get them so they won't be staggered in the grid
    print("I am getting the u variable from the wrfout file")
    print('getting uf winds for east tower')
    uf_e = wrfout.variables['UF'][:, y_east_sub, x_east_sub]
    print('getting vf winds for east tower')
    vf_e = wrfout.variables['VF'][:, y_east_sub, x_east_sub]
    wind_no_fire_east = np.sqrt((uf_e ** 2) + (vf_e ** 2))

    # West Tower
    print('getting uf winds for west tower')
    uf_w = wrfout.variables['UF'][:, y_west_sub, x_west_sub]
    print('getting vf winds for west tower')
    vf_w = wrfout.variables['VF'][:, y_west_sub, x_west_sub]
    wind_no_fire_west = np.sqrt((uf_w ** 2) + (vf_w ** 2))

    # south Tower
    print('getting uf winds for south tower')
    uf_s = wrfout.variables['UF'][:, y_south_sub, x_south_sub]
    print('getting vf winds for south tower')
    vf_s = wrfout.variables['VF'][:, y_south_sub, x_south_sub]
    wind_no_fire_south = np.sqrt((uf_w ** 2) + (vf_w ** 2))
    

    results = {'wind_fire_fire_main': wind_fire_fire_main, 'wind_fire_no_fire_main' : wind_fire_no_fire_main,
    'wind_fire_fire_east' : wind_fire_fire_east, 'wind_fire_fire_west' : wind_fire_fire_west, 'wind_fire_fire_south' : 
    wind_fire_fire_south, 'wind_fire_no_fire_main' : wind_fire_no_fire_main, 'wind_no_fire_east' : wind_no_fire_east, 
    'wind_no_fire_west' : wind_no_fire_west, 'wind_no_fire_south' : wind_no_fire_south } 



    with open(out_path, 'wb') as f:
        pickle.dump(results, f)
else:
    with open(out_path, 'rb') as f:
        results = pickle.load(f)
    locals().update(results)

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

# %% Creating the plot with all the lines on it
no_fire_time = wrfout_time_no_fire[240:420] * 60
fire_time = wrfout_time[240:420] * 60
n = 10
fig, ax = plt.subplots(2, 3, figsize = (24, 14))
plt.suptitle('Main Tower Winds Compared to a Coupled and Uncoupled WRF-SFIRE Winds From The FireFlux2 Simulation', fontsize = 18, fontweight = 'bold')
# Plotting the 20 Meter Wind Speed
ax[0, 0].plot(time_towers, ws_20, color = 'blue', label = 'Main Tower Wind (m/s)')
ax[0, 0].plot(time_towers, ws_20.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[0, 0].plot(no_fire_time, ws_h_20_no_fire[240:420], color = 'red', label = 'Uncoupled Wind (m/s)')
ax[0, 0].plot(fire_time, ws_h_20[240:420], color = 'green', label = 'Coupled Wind (m/s)')
ax[0, 0].set_xlim(240, 420)
ax[0, 0].set_xlabel('Time (s)', fontsize = 12, fontweight = 'bold')
ax[0, 0].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[0, 0].set_title('20 Meter Wind Speeds From Main tower and wrfout files', fontsize = 12, fontweight = 'bold')
ax[0, 0].grid()
ax[0, 0].legend()

# Plotting the 10 Meter Wind Speed
ax[0, 1].plot(time_towers, ws_10, color = 'blue', label = 'Main Tower Wind (m/s)')
ax[0, 1].plot(time_towers, ws_10.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[0, 1].plot(no_fire_time, ws_h_10_no_fire[240:420], color = 'red', label = 'Uncoupled Wind (m/s)')
ax[0, 1].plot(fire_time, ws_h_10[240:420], color = 'green', label = 'Coupled Wind (m/s)')
ax[0, 1].set_xlim(240, 410)
ax[0, 1].set_xlabel('Time (s)', fontsize = 12, fontweight = 'bold')
ax[0, 1].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[0, 1].set_title('10 Meter Wind Speeds From Main tower and wrfout files', fontsize = 12, fontweight = 'bold')
ax[0, 1].grid()
ax[0, 1].legend()

# Plotting the 5.77 Meter Wind Speed
ax[0, 2].plot(time_towers, ws_6, color = 'blue', label = 'Main Tower Wind (m/s)')
ax[0, 2].plot(time_towers, ws_6.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[0, 2].plot(no_fire_time, ws_h_577_no_fire[240:420], color = 'red', label = 'Uncoupled Wind (m/s)')
ax[0, 2].plot(fire_time, ws_h_577[240:420], color = 'green', label = 'Coupled Wind (m/s)')
ax[0, 2].set_xlim(240, 420)
ax[0, 2].set_xlabel('Time (s)', fontsize = 12, fontweight = 'bold')
ax[0, 2].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[0, 2].set_title('5.77 Meter Wind Speeds From Main tower and wrfout files', fontsize = 12, fontweight = 'bold')
ax[0, 2].grid()
ax[0, 2].legend()

# Plotting the 20 Meter W Wind Speed
ax[1, 0].plot(time_towers, uz20, color = 'blue', label = 'Main Tower Wind (m/s)')
ax[1, 0].plot(time_towers, uz20.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[1, 0].plot(no_fire_time, W_h_20_no_fire[240:420], color = 'red', label = 'Uncoupled Wind (m/s)')
ax[1, 0].plot(fire_time, W_h_20[240:420], color = 'green', label = 'Coupled Wind (m/s)')
ax[1, 0].set_xlim(240, 420)
ax[1, 0].set_xlabel('Time (s)', fontsize = 12, fontweight = 'bold')
ax[1, 0].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[1, 0].set_title('20 Meter W Wind From Main tower and wrfout files', fontsize = 12, fontweight = 'bold')
ax[1, 0].grid()
ax[1, 0].legend()

# Plotting the 10 Meter W Wind Speed
ax[1, 1].plot(time_towers, uz10, color = 'blue', label = 'Main Tower Wind (m/s)')
ax[1, 1].plot(time_towers, uz10.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[1, 1].plot(no_fire_time, W_h_10_no_fire[240:420], color = 'red', label = 'Uncoupled Wind (m/s)')
ax[1, 1].plot(fire_time, W_h_10[240:420], color = 'green', label = 'Coupled Wind (m/s)')
ax[1, 1].set_xlim(240, 420)
ax[1, 1].set_xlabel('Time (s)', fontsize = 12, fontweight = 'bold')
ax[1, 1].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[1, 1].set_title('10 Meter W Wind From Main tower and wrfout files', fontsize = 12, fontweight = 'bold')
ax[1, 1].grid()
ax[1, 1].legend()

# Plotting the 5.77 Meter W Wind Speed
ax[1, 2].plot(time_towers, uz6, color = 'blue', label = 'Main Tower Wind (m/s)')
ax[1, 2].plot(time_towers, uz6.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--')
ax[1, 2].plot(no_fire_time, W_h_577_no_fire[240:420], color = 'red', label = 'Uncoupled Wind (m/s)')
ax[1, 2].plot(fire_time, W_h_577[240:420], color = 'green', label = 'Coupled Wind (m/s)')
ax[1, 2].set_xlim(240, 420)
ax[1, 2].set_xlabel('Time (s)', fontsize = 12, fontweight = 'bold')
ax[1, 2].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[1, 2].set_title('5.77 Meter W Wind From Main tower and wrfout files', fontsize = 12, fontweight = 'bold')
ax[1, 2].grid()
ax[1, 2].legend()

plt.tight_layout()
plt.show()









# %% Creating a figure just for the fire wind
fig, ax = plt.subplots(figsize = (15, 10))
ax2 = ax.twinx()
ax1 = ax.plot(time_towers, ws_6, color = 'blue', label = 'Main Tower Wind Speed', linewidth = 2)
ax3 = ax.plot(time_towers, ws_6.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--', linewidth = 2)
ax4 = ax.plot(no_fire_time, ws_h_577_no_fire[240:420], color = 'red', label = 'Uncoupled Wind', linewidth = 2.5)
ax5 = ax.plot(fire_time, ws_h_577[240:420], color = 'green', label = 'Coupled Wind', linewidth = 2.5)
ax6 = ax2.plot(fire_time, wind_fire_fire_main[240:420], color = 'orange', label = 'Fire Wind Coupled Run', linewidth = 2.5)

ax.grid()
ax.set_xlabel('Time(s)', fontsize = 18, fontweight = 'bold')
ax.set_ylabel('Wind Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax2.set_ylabel('Fire Wind (m/s)', fontsize = 18, fontweight = 'bold')
ax2.set_ylim(0)
plt.tight_layout()
ax.set_xlim(240, 420)
ax.tick_params(axis='x', labelsize=20)
ax2.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.set_title('5.77m Main Tower Wind vs. Coupled and Uncoupled FF2 Simulations With Fire Wind Comparison', fontsize = 18, fontweight = 'bold')
label = ax1 + ax3 + ax4 + ax5 + ax6
labels = [i.get_label() for i in label]
leg = ax.legend(label, labels, prop={'size': 12})


plt.tight_layout()
plt.show()


# %% Creating a plot of the 5.77m main tower vs fire wind with separate axis

fig, ax = plt.subplots(figsize = (15, 10))
ax2 = ax.twinx()
ax1 = ax.plot(wrfout_time * 60, abs(ws_h_20[0:911] - ws_h_20_no_fire[0:911]))







#ignore the fire winds. ignore the winds on the fire mesh. They are meaningless.
# Subtract ws_h_20 - ws_h_20_no_fire 
#ax1 = ax.plot(np.arange(0, 911.1, .1), ws_6, color = 'blue', label = 'Main Tower Wind Speed', linewidth = 2)
#ax3 = ax.plot(np.arange(0, 911.1, .1), ws_6.rolling(window = n).mean(), color = 'black', label = 'Rolling Average', linestyle = '--', linewidth = 2)
#ax5 = ax.plot(fire_time, ws_577_wrfout, color = 'green', label = 'Wrfout Wind', linewidth = 2.5)
#ax6 = ax2.plot(fire_time, wind_fire_fire_main[240:420], color = 'red', label = 'Fire Wind Coupled Run', linewidth = 2.5)
ax7 = ax2.plot(wrfout_time[0:911] * 60, abs(ws_h_20[0:911] - ws_h_20_no_fire[0:911]), color = 'green', label = 'Calculated Fire Wind')
# Line 303 is how I am supposed to do it
#Make some plots of just the time series without the tower data, make a point where the fire passage is
#Start at time 0. Plot the whole time series
ax.grid()
ax.set_xlabel('Time(s)', fontsize = 18, fontweight = 'bold')
ax.set_ylabel('Wind Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax2.set_ylabel('Fire Wind (m/s)', fontsize = 18, fontweight = 'bold')
plt.tight_layout()
ax2.set_ylim(0)
#ax.set_xlim(240, 420)
ax.tick_params(axis='x', labelsize=20)
ax2.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.set_title('5.77m Main Tower Wind vs. Fire Wind', fontsize = 18, fontweight = 'bold')
label = ax7
labels = [i.get_label() for i in label]
leg = ax.legend(label, labels, prop={'size': 12})


plt.tight_layout()
plt.show()

# %% Creating the short tower plots
'''results = {'wsw_h_533':wsw_h_533, 'Ww_h_533':Ww_h_533, 'wse_h_528':wse_h_528, 
    'We_h_528':We_h_528, 'wss_h_533':wss_h_533, 'Ws_h_533':Ws_h_533, 'wsw':wsw, 
    'ww':ww, 'wss':wss, 'ws':ws, 'wse':wse, 'we':we, 'wrfout_time':wrfout_time} #put the other variables in here such as wsw and ww '''
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
short_tower_time = np.arange(240, 421)
n = 5
fig, ax = plt.subplots(3, figsize = (15, 10))

# Plotting the East tower Winds
ax2 = ax[0].twinx()
ax1 = ax[0].plot(short_tower_time, wse[240:421], color = 'blue', label = 'Wind Speed', linewidth = 2)
ax3 = ax[0].plot(short_tower_time, wse[240:421].rolling(window = n).mean(), color = 'black', linestyle = '--', label = '5s Rolling Average') #plotting the rolling average from the west tower wind speed
ax4 = ax2.plot(fire_time, wind_fire_fire_east[240:420], color = 'red', label = 'Coupled Fire Wind', linewidth = 2)
ax5 = ax2.plot(no_fire_time, wind_no_fire_east[240:420], color = 'green', label = 'Uncoupled Fire Wind', linewidth = 2)
#ax6 = ax2.plot(no_fire_time, abs(wind_fire_fire_east[240:420] - wind_no_fire_east[240:420]), color = 'black')

ax[0].grid()
ax[0].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[0].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[0].set_xlim(240, 420)
ax2.set_ylim(0)
label = ax1 + ax3 + ax4 + ax5
labels = [i.get_label() for i in label]
ax[0].legend(label, labels, prop={'size': 6})
ax[0].set_title('Fire Wind vs. Observations for East Tower', fontsize = 12, fontweight = 'bold')
# Plotting the West tower Winds
ax2 = ax[1].twinx()
ax6 = ax[1].plot(short_tower_time, wsw[240:421], color = 'blue', label = 'Wind Speed', linewidth = 2)
ax7 = ax[1].plot(short_tower_time, wsw[240:421].rolling(window = n).mean(), color = 'black', linestyle = '--', label = '5s Rolling Average') #plotting the rolling average from the west tower wind speed)
ax8 = ax2.plot(fire_time, wind_fire_fire_west[240:420], color = 'red', label = 'Coupled Fire Wind', linewidth = 2)
ax9 = ax2.plot(no_fire_time, wind_no_fire_west[240:420], color = 'green', label = 'Uncoupled Fire Wind', linewidth = 2)

ax[1].grid()
ax[1].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[1].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[1].set_xlim(240, 420)
ax2.set_ylim(0)
label = ax6 + ax7 + ax8 + ax9
labels = [i.get_label() for i in label]
ax[1].legend(label, labels, prop={'size': 10}, loc = 4)
ax[1].set_title('Fire Wind vs. Observations for West Tower', fontsize = 12, fontweight = 'bold')

# Plotting the South tower Winds
ax2 = ax[2].twinx()
ax10 = ax[2].plot(short_tower_time, wss[240:421], color = 'blue', label = 'Wind Speed', linewidth = 2)
ax11 = ax[2].plot(short_tower_time, wss[240:421].rolling(window = n).mean(), color = 'black', linestyle = '--', label = '5s Rolling Average') #plotting the rolling average from the south tower wind speed)
ax12 = ax2.plot(fire_time, wind_fire_fire_south[240:420], color = 'red', label = 'Coupled Fire Wind', linewidth = 2)
ax13 = ax2.plot(no_fire_time, wind_no_fire_south[240:420], color = 'green', label = 'Uncoupled Fire Wind', linewidth = 2)

ax[2].grid()
ax[2].set_xlabel('Time (Seconds)', fontsize = 12, fontweight = 'bold')
ax[2].set_ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
ax[2].set_xlim(240, 420)
ax2.set_ylim(0)
label = ax10 + ax11 + ax12 + ax13
labels = [i.get_label() for i in label]
ax[2].legend(label, labels, prop={'size': 10}, loc = 4)
ax[2].set_title('Fire Wind vs. Observations for South Tower', fontsize = 12, fontweight = 'bold')

plt.tight_layout()
plt.show()

# %% Creating a plot of just the fire wind with time
fig = plt.figure(figsize = (12, 8))
plt.plot(wrfout_time_no_fire, wind_fire_fire_main[0:911], label = 'Fire Wind', color = 'blue')
plt.xlabel('Time (minutes)')
plt.ylabel('Wind Speed (m/s)')
plt.title('Fire Wind (m/s) From Coupled Simulation vs. Time', fontsize = 18, fontweight = 'bold')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()



# %%
