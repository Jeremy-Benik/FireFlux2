#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:10:46 2022

@author: Kathleen Clough
"""

# %% Importing libraries
import numpy as np
import netCDF4 as nc
import glob
import re
from datetime import datetime
import pandas as pd
import json
from wrf import ll_to_xy

#from wrf import getvar, interplevel
# %% importing the data using glob so I can read all the files at once
fc_path = r'/home/akochanski/scratch/Caldor/wfc-from-web-2021-08-21*/wrf/'
obs_path = r'/home/kclough/Caldor/PM_2.5_Data/'
fc_files = sorted(glob.glob(fc_path + "wrfout_d03*"))
obs_files = sorted(glob.glob(obs_path + "PM25_21*"))
data_keys = ['STID','LONGITUDE','LATITUDE','MNET_ID','datetime','PM_25']
data_dic = {key: [] for key in data_keys}
# %%
for obs_file in obs_files:
    js = json.load(open(obs_file))
    for stData in js['STATION']:
        data_dic['STID'] += [stData['STID']]*len(stData['OBSERVATIONS']['date_time'])
        data_dic['LONGITUDE'] += [stData['LONGITUDE']]*len(stData['OBSERVATIONS']['date_time'])
        data_dic['LATITUDE'] += [stData['LATITUDE']]*len(stData['OBSERVATIONS']['date_time'])
        data_dic['MNET_ID'] += [stData['MNET_ID']]*len(stData['OBSERVATIONS']['date_time'])
        data_dic['datetime'] += stData['OBSERVATIONS']['date_time']
        data_dic['PM_25'] += stData['OBSERVATIONS']['PM_25_concentration_set_1']

data = pd.DataFrame.from_dict(data_dic)
data.LONGITUDE = data.LONGITUDE.astype(float)
data.LATITUDE = data.LATITUDE.astype(float)
data['datetime'] = pd.to_datetime(data['datetime'])
data.to_csv('PM25_obs.csv', index=False)
# %%
ds = nc.Dataset(fc_files[0])
xlat = ds.variables['XLAT'][:]
xlon = ds.variables['XLONG'][:]
minlon = xlon.min()
maxlon = xlon.max()
minlat = xlat.min()
maxlat = xlat.max()
stats = data.groupby('STID').first()[['LONGITUDE','LATITUDE']]
mask = np.logical_and(stats.LONGITUDE  >= minlon, 
    np.logical_and(stats.LONGITUDE <= maxlon, 
        np.logical_and(stats.LATITUDE >= minlat, stats.LATITUDE <= maxlat)))
coords = stats[mask]
groups = {
    0: '12h',
    1: '24h',
    2: '36h',
    3: '48h'
}
fctime = [[], [], [], []]
wtime = [[], [], [], []]
wxlat = [[], [], [], []]
wxlon = [[], [], [], []]
oxlat = [[], [], [], []]
oxlon = [[], [], [], []]
wrf_pm25_data = [[], [], [], []]

for filename in fc_files:
    print(filename)
    m = re.match(r'.*-16-10-([0-9]{4})-([0-9]{2})-([0-9]{2})_([0-9]{2}):([0-9]{2}):([0-9]{2})-*',filename)
    if m:
        m = m.groups()
        fcstarttime = '{:04d}-{:02d}-{:02d}_{:02d}:{:02d}:{:02d}'.format(*[int(_) for _ in m])#converting strings into integers 
        with nc.Dataset(filename, 'r', format='NETCDF4') as ds:
            wrfout_time = ''.join([c.decode() for c in ds['Times'][0]])
            tr17_1 = ds.variables['tr17_1'][:]
            xlat = ds.variables['XLAT'][:]
            xlon = ds.variables['XLONG'][:]
            i_j = ll_to_xy(ds,coords.LATITUDE,coords.LONGITUDE)
        wrf_xlat= xlat[0,i_j[1,],i_j[0,]]
        wrf_xlon= xlon[0,i_j[1,],i_j[0,]]
        wrf_pm25= tr17_1[0,0,i_j[1,],i_j[0,]]  #extra 0 since tr17_1 is 3D and we just want first level
        ft_dt = datetime.strptime(fcstarttime,'%Y-%m-%d_%H:%M:%S')
        wt_dt = datetime.strptime(wrfout_time,'%Y-%m-%d_%H:%M:%S')
        offset_hours = abs(wt_dt-ft_dt).total_seconds()/3600.
        fcstarttime = [fcstarttime]*len(wrf_xlon)
        wrfout_time = [wrfout_time]*len(wrf_xlon)
        ## concatenate new data
        if offset_hours > 0 and offset_hours <= 12:
            fctime[0].append(fcstarttime)
            wtime[0].append(wrfout_time)
            wrf_pm25_data[0].append(wrf_pm25)
            wxlat[0].append(wrf_xlat)
            wxlon[0].append(wrf_xlon)
            oxlat[0].append(coords.LATITUDE.to_numpy())
            oxlon[0].append(coords.LONGITUDE.to_numpy())
        elif offset_hours > 0 and offset_hours <= 24:
            fctime[1].append(fcstarttime)
            wtime[1].append(wrfout_time)
            wrf_pm25_data[1].append(wrf_pm25)
            wxlat[1].append(wrf_xlat)
            wxlon[1].append(wrf_xlon)
            oxlat[1].append(coords.LATITUDE.to_numpy())
            oxlon[1].append(coords.LONGITUDE.to_numpy())
        elif offset_hours > 0 and offset_hours <= 36:
            fctime[2].append(fcstarttime) 
            wtime[2].append(wrfout_time)
            wrf_pm25_data[2].append(wrf_pm25)
            wxlat[2].append(wrf_xlat)
            wxlon[2].append(wrf_xlon)
            oxlat[2].append(coords.LATITUDE.to_numpy())
            oxlon[2].append(coords.LONGITUDE.to_numpy())           
        elif offset_hours > 0 and offset_hours <= 48:
            fctime[3].append(fcstarttime)
            wtime[3].append(wrfout_time)
            wrf_pm25_data[3].append(wrf_pm25)
            wxlat[3].append(wrf_xlat)
            wxlon[3].append(wrf_xlon)
            oxlat[3].append(coords.LATITUDE.to_numpy())
            oxlon[3].append(coords.LONGITUDE.to_numpy())
# %%
for g in range(len(fctime)):
    df = pd.DataFrame({'ftime':np.concatenate(fctime[g]), 'wtime':np.concatenate(wtime[g]), 'offset': groups[g], 'wrf_lat':np.concatenate(wxlat[g]), 'wrf_lon':np.concatenate(wxlon[g]), 'o_lat':np.concatenate(oxlat[g]), 'o_lon':np.concatenate(oxlon[g]),'wrf_pm25':np.concatenate(wrf_pm25_data[g])})
    df.to_csv('Caldor_WRF_PM25_{}.csv'.format(groups[g]),index=False)

# %%
