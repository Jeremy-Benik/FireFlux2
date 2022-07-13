#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:38:17 2022

@author: jeremybenik
"""

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('/Volumes/Data/FireFlux2-main/Data/ROS_Files/Balbi_sensitivity.xlsx', skiprows=[0, 1, 2, 3])

st = df['Stochiometric Factor (st)']
ros_st = df['ROS_st']
t_f_st = df['Flame Temp st']
u_0_st = df['U_0 st']
fig, ax = plt.subplots(3, figsize = (12, 12))
ax[0].plot(st, ros_st, color = 'red', label = 'Rate Of Spread')
ax[0].set_xlabel('Stochiometric Coefficient', fontsize = 12, fontweight = 'bold')
ax[0].set_ylabel('Rate of Spread (m/s)', fontsize = 12, fontweight = 'bold')
ax[0].set_title('Stochiometric Coefficient vs. ROS', fontsize = 18, fontweight = 'bold')
ax[0].grid()


ax[1].plot(st, t_f_st)
ax[1].set_ylabel('Flame Temperature (K)', fontsize = 12, fontweight = 'bold')
ax[1].set_title('Stochiometric Coefficient vs. Flame Temp', fontsize = 18, fontweight = 'bold')

ax[1].grid()
ax[1].set_xlabel('Stochiometric Coefficient', fontsize = 12, fontweight = 'bold')
ax[2].plot(st, u_0_st)
ax[2].set_ylabel('U_0 (Wind Speed (m/s))', fontsize = 12, fontweight = 'bold')
ax[2].grid()
ax[2].set_title('Stochiometric Coefficient vs. U_0', fontsize = 18, fontweight = 'bold')

ax[2].set_xlabel('Stochiometric Coefficient', fontsize = 12, fontweight = 'bold')

plt.tight_layout()
plt.show()


st = df['Air Density (rho_a)']
ros_st = df['ROS rho_a']
t_f_st = df['Flame Temp rho_a']
u_0_st = df['U_0 rho_a']


fig, ax = plt.subplots(3, figsize = (12, 12))
ax[0].plot(st, ros_st, color = 'red', label = 'Rate Of Spread')
ax[0].set_xlabel('Air Density (rho_a)', fontsize = 12, fontweight = 'bold')
ax[0].set_ylabel('Rate of Spread (m/s)', fontsize = 12, fontweight = 'bold')
ax[0].set_title('Air Density vs. ROS', fontsize = 18, fontweight = 'bold')
ax[0].grid()


ax[1].plot(st, t_f_st)
ax[1].set_ylabel('Flame Temperature (K)', fontsize = 12, fontweight = 'bold')
ax[1].set_title('Air Density vs. Flame Temp', fontsize = 18, fontweight = 'bold')

ax[1].grid()
ax[1].set_xlabel('Air Density', fontsize = 12, fontweight = 'bold')
ax[2].plot(st, u_0_st)

ax[2].set_ylabel('U_0 (Wind Speed (m/s))', fontsize = 12, fontweight = 'bold')
ax[2].grid()
ax[2].set_title('Air Density vs. U_0', fontsize = 18, fontweight = 'bold')

ax[2].set_xlabel('Air Density', fontsize = 12, fontweight = 'bold')

plt.tight_layout()
plt.show()

st = df['Air Temp (T_a)']
ros_st = df['ROS T_a']
t_f_st = df['Flame Temp T_a']
u_0_st = df['U_0 T_a']
fig, ax = plt.subplots(3, figsize = (12, 12))
ax[0].plot(st, ros_st, color = 'red', label = 'Rate Of Spread')
ax[0].set_xlabel('Air Temp (K)', fontsize = 12, fontweight = 'bold')
ax[0].set_ylabel('Rate of Spread (m/s)', fontsize = 12, fontweight = 'bold')
ax[0].set_title('Air Temp vs. ROS', fontsize = 18, fontweight = 'bold')
ax[0].grid()


ax[1].plot(st, t_f_st)
ax[1].set_ylabel('ir Temp (K)', fontsize = 12, fontweight = 'bold')
ax[1].set_title('Air Temp vs. Flame Temp', fontsize = 18, fontweight = 'bold')

ax[1].grid()
ax[1].set_xlabel('Air Temp ', fontsize = 12, fontweight = 'bold')
ax[2].plot(st, u_0_st)
ax[2].set_ylabel('U_0 (Wind Speed (m/s))', fontsize = 12, fontweight = 'bold')
ax[2].grid()
ax[2].set_title('Air Temp  vs. U_0', fontsize = 18, fontweight = 'bold')

ax[2].set_xlabel('Air Temp', fontsize = 12, fontweight = 'bold')

plt.tight_layout()
plt.show()


st = df['Ignition Line (W_0)']
ros_st = df['ROS W_0']
t_f_st = df['Flame Temp W_0']
u_0_st = df['U_0 W_0']


fig, ax = plt.subplots(3, figsize = (12, 12))
ax[0].plot(st, ros_st, color = 'red', label = 'Rate Of Spread')
ax[0].set_xlabel('Ignition Line Width (m)', fontsize = 12, fontweight = 'bold')
ax[0].set_ylabel('Rate of Spread (m/s)', fontsize = 12, fontweight = 'bold')
ax[0].set_title('Ignition Line Width (m) vs. ROS', fontsize = 18, fontweight = 'bold')
ax[0].grid()


ax[1].plot(st, t_f_st)
ax[1].set_ylabel('Flame Temperature (K)', fontsize = 12, fontweight = 'bold')
ax[1].set_title('Ignition Line Width (m) vs. Flame Temp', fontsize = 18, fontweight = 'bold')

ax[1].grid()
ax[1].set_xlabel('Ignition Line Width (m)', fontsize = 12, fontweight = 'bold')
ax[2].plot(st, u_0_st)

ax[2].set_ylabel('U_0 (Wind Speed (m/s))', fontsize = 12, fontweight = 'bold')
ax[2].grid()
ax[2].set_title('Ignition Line Width (m) vs. U_0', fontsize = 18, fontweight = 'bold')

ax[2].set_xlabel('Ignition Line Width (m)', fontsize = 12, fontweight = 'bold')

plt.tight_layout()
plt.show()