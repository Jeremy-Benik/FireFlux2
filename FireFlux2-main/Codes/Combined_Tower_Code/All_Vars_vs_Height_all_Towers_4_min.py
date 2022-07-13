#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 12:27:43 2022

@author: jeremy
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/temperature_averages.csv')
fig, ax = plt.subplots(2, 2, figsize = (12, 12))
ax[0, 0].plot(df['Temperature(C)'], df['Height(m)'], color = 'red', label = 'Temperature$^\circ$C')
ax[0, 0].set_xlabel('Temperature$^\circ$C', fontsize = 18, fontweight = 'bold')
ax[0, 0].set_ylabel('Height (m)', fontsize = 18, fontweight = 'bold')
ax[0, 0].set_title('Temperature vs Height', fontsize = 18, fontweight = 'bold')
ax[0, 0].legend()

ax[0, 1].plot(df['U'], df['Height(m)'], color = 'blue', label = 'U Wind (m/s)')
ax[0, 1].set_xlabel('U Wind (m/s)', fontsize = 18, fontweight = 'bold')
ax[0, 1].set_ylabel('Height (m)', fontsize = 18, fontweight = 'bold')
ax[0, 1].set_title('U Wind vs Height', fontsize = 18, fontweight = 'bold')
ax[0, 1].legend()

ax[1, 0].plot(df['V'], df['Height(m)'], color = 'purple', label = 'V Wind (m/s)')
ax[1, 0].set_xlabel('V Wind (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_ylabel('Height (m)', fontsize = 18, fontweight = 'bold')
ax[1, 0].set_title('V Wind vs Height', fontsize = 18, fontweight = 'bold')
ax[1, 0].legend()

ax[1, 1].plot(df['Wind_Speed'], df['Height(m)'], color = 'green', label = 'Wind Speed (m/s)')
ax[1, 1].set_xlabel('Wind Speed (m/s)', fontsize = 18, fontweight = 'bold')
ax[1, 1].set_ylabel('Height (m)', fontsize = 18, fontweight = 'bold')
ax[1, 1].set_title('Wind Speed vs Height', fontsize = 18, fontweight = 'bold')
ax[1, 1].legend()

plt.tight_layout()
plt.show()