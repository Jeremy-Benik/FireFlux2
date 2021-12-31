# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:54:21 2021

@author: Jeremy Benik
"""

'''The purpose of this program is to go through the csv files and
take the time the fire started, and 30 minutes after the fire started and create a new file'''
#10 measurements per second and I want 8 seconds in
#the fire starts at 15:04:08 CST
# %% Libraries needed for going through the data
import pandas as pd
import numpy as np
import statistics as st
# %% Reading in the data as df
df = pd.read_csv('F:/Fireflux2/Website_Docs/Proc_FF2_10HzMTdespiked_rotated.csv', skiprows = (0, 2, 3))
#reading in the data and skipping the rows so it will read in properly
# %% Finding where the date is to index to
# The data I need to index to is: 15:04:08 CST
df['times'] = pd.to_datetime(df['TIMESTAMP']) #converting the datetime to a more usuable value, not sure if this is
#completely necessary but the code works so I won't mess with it
x = np.where(df['times'] == '1/30/2013  15:00:00')[0][0] #this line finds where times = the start time and indexes to 
#the time at which the data is at so in this case 15:04:08 CST is now assigned to x
# 10 measurements per second and I want 8 seconds in
y = np.where(df['times'] == '1/30/2013  15:04:00')[0][80] #this is finding the index for 30 min after the burn occurred
# and setting it to s y variable

# %% clipping the data so I only have the 30 minutes
newdf = df.truncate(before= x, after=y) #creating a newdf variable and assigning the data to be between the two times
# of x and y
newdf.to_csv('F:/Fireflux2/Website_Docs/other_Clipped_to_35_minutes_Proc_FF2_10HzMTdespiked_rotated.csv')
#using the newdf variable with all the data from the start to 30 minutes after thew fire burned, and creating
# a new csv file to start using. Since the file is created, I will likely not use this code much more, but It'll be
#useful for the other datasets as well. 






