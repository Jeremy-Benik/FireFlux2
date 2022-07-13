import pandas as pd
import numpy as np



df_w1 = pd.read_csv('/home/jbenik/FireFlux2/Codes_and_Data/Data/Short_Tower_Data/Proc_FF2_1HzSTWdespikedrotated.csv')

df_w = df_w1.truncate(before= np.where(df_w1['TIMESTAMP'] == '1/30/2013 15:04')[0][0],
                    after=np.where(df_w1['TIMESTAMP'] == '1/30/2013 15:06')[0][0])
print(df_w)

time_short_tower_w = df_w['TIMESTAMP']
uw = df_w['u']
vw = df_w['v']
ww = df_w['w']
tw = df_w['t']
wsw = np.sqrt((uw ** 2) + (vw ** 2))
print(wsw)
