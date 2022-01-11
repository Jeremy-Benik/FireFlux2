# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:29:00 2021

@author: Rubix
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st
import glob
df1 = pd.read_csv('/media/jeremy/Data/Fireflux2/Website_Docs/Main_Tower_Data/Proc_FF2_10HzMTdespiked_rotated.csv', parse_dates=['TIMESTAMP'], skiprows = (0, 2, 3))
#this reads in the dataframe and parses the dates. I also skip unecessary rows. This csv is modified by removing the record column and 
#moving the other columns over
# Calculating the time for 4 minutes before the fire start so I can average them all
df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][80], 
                    after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:19:00')[0][80])
time = df['TIMESTAMP']
ux20 = df['Ux_20m']
uy20 = df['Uy_20m']
uz20 = df['Uz_20m']
ts20 = df['Ts_20m']
ux10 = df['Ux_10m']
uy10 = df['Uy_10m']
uz10 = df['Uz_10m']
ts10 = df['Ts_10m']
ux6 = df['Ux_6m']
uy6 = df['Uy_6m']
uz6 = df['Uz_6m']
ts6 = df['Ts_6m']
varlist = ['ux20', 'uy20', 'uz20', 'ts20', 'ux10', 'uy10', 'uz10', 'ts10', 'ux6', 'uy6', 'uz6', 'ts6']
for var in varlist:
    print('The Average of {} 4 minutes before and 4 minutes after the fire start is: {:.2f}'.format(var, st.mean(vars()[var])))

# %% importing the data using glob so I can read all the files at once
path = r'/media/jeremy/Data/Fireflux2/Website_Docs/Short_Tower_Data'
filenames = glob.glob(path + "/*.csv")
# %% making a for loop to iterate through all the files and make plots of them all at once
n = 5 #this is a 5 second average of the data
t_all = []
for filename in filenames:
    df1 = pd.read_csv((filename), parse_dates = ['TIMESTAMP'])
    df = df1.truncate(before= np.where(df1['TIMESTAMP'] == '1/30/2013  15:04:00')[0][3], 
                        after=np.where(df1['TIMESTAMP'] == '1/30/2013  15:19:00')[0][3])
    time = df['TIMESTAMP']
    u = df['u']
    v = df['v']
    w = df['w']
    t = df['t']
    varlist = ['t']
    for var in varlist:
        #print('The Average of {} 4 minutes before and 4 minutes after the fire start is: {:.2f}'.format(var, st.mean(vars()[var])))
        t_all.append(st.mean(vars()[var]))
print('Mean of the temperatures from the short towers at specified time is:' st.mean(t_all))