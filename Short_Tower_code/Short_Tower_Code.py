# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 09:22:29 2021

@author: Jeremy Benik
"""
# %% Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import metpy.calc
from metpy.units import units
import statistics as st
import math
# %% importing the data using glob so I can read all the files at once
path = r'D:/Fireflux2/Website_Docs/Short_Tower_Data/'
filenames = glob.glob(path + "/*.csv")
# %% making a for loop to iterate through all the files and make plots of them all at once
n = 5 #this is a 5 second average of the data
for filename in filenames:
    df1 = pd.read_csv((filename), parse_dates = ['TIMESTAMP'])
    df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][3], 
                        after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:34:00')[0][3])
    time = df['TIMESTAMP']
    u = df['u']
    v = df['v']
    w = df['w']
    t = df['t']
    time2 = np.arange(0, len(time)) / 60
    fig, ax = plt.subplots(4, 1, figsize = (15, 10))
    plt.suptitle(f"Short tower plots for the {filename[-20]} Tower", fontsize = 18, fontweight = 'bold')
    ax[0].plot(time2, u, 'blue', label = 'U wind')
    ax[0].plot(time2, u.rolling(window = n).mean(), 'black', label = 'Avg. U winds', linestyle = '-')
    ax[0].legend(prop={'size': 6})
    ax[0].set_title(f"U wind for the {filename[-20]} Tower", fontsize = 16, fontweight = 'bold')
    ax[0].set_xlim(0, 30)
    ax[0].set_xlabel('Time (Minutes)', fontsize = 16, fontweight = 'bold')
    ax[0].set_ylabel('U wind (m/s)', fontsize = 16, fontweight = 'bold')
    ax[1].plot(time2, v, 'green', label = 'V wind')
    ax[1].plot(time2, v.rolling(window = n).mean(), 'black', label = 'Avg. V winds', linestyle = '-')
    ax[1].legend(prop={'size': 6})
    ax[1].set_title(f"V wind for the {filename[-20]} Tower", fontsize = 16, fontweight = 'bold')
    ax[1].set_xlim(0, 30)
    ax[1].set_xlabel('Time (Minutes)', fontsize = 16, fontweight = 'bold')
    ax[1].set_ylabel('V wind (m/s)', fontsize = 16, fontweight = 'bold')
    ax[2].plot(time2, w, 'red', label = 'W wind')
    ax[2].plot(time2, w.rolling(window = n).mean(), 'black', label = 'Avg. W winds', linestyle = '-')
    ax[2].legend(prop={'size': 6})
    ax[2].set_title(f"W wind for the {filename[-20]} Tower", fontsize = 16, fontweight = 'bold')
    ax[2].set_xlim(0, 30)
    ax[2].set_xlabel('Time (Minutes)', fontsize = 16, fontweight = 'bold')
    ax[2].set_ylabel('W wind (m/s)', fontsize = 16, fontweight = 'bold')
    ax[3].plot(time2, t, 'green', label = 'Temperature$^\circ$C')
    ax[3].plot(time2, t.rolling(window = n).mean(), 'black', label = 'Avg. Temperature', linestyle = '-')
    ax[3].legend(prop={'size': 6})
    ax[3].set_title(f"Temperature for the {filename[-20]} Tower", fontsize = 16, fontweight = 'bold')
    ax[3].set_xlim(0, 30)
    ax[3].set_xlabel('Time (Minutes)', fontsize = 16, fontweight = 'bold')
    ax[3].set_ylabel('Temperature$^\circ$C', fontsize = 16, fontweight = 'bold')
    plt.tight_layout()
    plt.show()
    