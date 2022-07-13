#Code: changing_levels.py
#Author: Jeremy Benik

# %% Importing necessary libraries
import netCDF4 as nc #This library is used to open the netCDF files
import xarray as xr #This library was used to open the netCDF files in a different way to better view them
import matplotlib.pyplot as plt #This library is used to plot the data to better visualize it as see if the changes
#that I made to the variables are accurate
import numpy as np 
import pandas as pd 
from wrf import vinterp, getvar #These are used to read in the wrf variables and to interpolate the variables at a list of heights. 
# %% Calling in the files and defining them
wrfin_ideal = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfinput_ideal_modified', 'r', format='NETCDF4')
#This wrfin file has a modified namelist.input and I changed the levels to 160 from 80 to match with the wrffdda
#i can change the amount of vertical levels in the wrfinput file using namelist.input
wrfin_real = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfin_adam_real', 'r', format='NETCDF4')
#wrfin_real is the wrfinput file from the real case from Dr. Kochanski's directory.
#Here is his directory on the ember cluster: /home/akochanski/WRF-SFIRE_4.2_new/test/em_ff2_real2/
#wrfin_mod = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrfinput_d01_modified', 'a', format='NETCDF4')
#This is the wrfin file that I plan to modify, hence reading it in as append mode
wrffdda_mod = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01_mod', 'a', format='NETCDF4')
wrffdda = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01', 'r', format='NETCDF4')
wrffdda_xr = xr.open_dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01')
wrffdda2 = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d02', 'r', format='NETCDF4')
# %% wrfin variables
U_ideal = getvar(wrfin_ideal, "ua", None, units = "m/s") #Defining U from the ideal wrfin file. I used getvar to not have the variable staggered
V_ideal = getvar(wrfin_ideal, "va", None, units = "m/s") #Defining V from the ideal wrfin file. I used getvar to not have the variable staggered
T_ideal = getvar(wrfin_ideal, "temp", None, units = 'K')
ph_ideal = getvar(wrfin_ideal, "geopt", None) #Note, this is different from PH since I used getvar instead of .variables
Q_ideal = wrfin_ideal.variables['QVAPOR'][:, :, :, :] #defining water vapor mixing ratio as Q_ideal
PH_ideal = wrfin_ideal.variables['PH'][:, :, :, :] #Defining PH to calculate height
PHB_ideal = wrfin_ideal.variables['PHB'][:, :, :, :] #Defining the height pertubation which will then be used to calculate height
height_ideal = 0.5*(PHB_ideal[:,:-1] + PH_ideal[:,:-1] + PHB_ideal[: , 1:] + PH_ideal[:, 1:])/9.81 #calculating height and doing it in a way where it isn't staggered
height_ideal /= 1000
#this formula can be found at INSERT WEBSITE HERE
#wrfin heights are always the same everywhere. 
# %% wrfin real variables
U_real = getvar(wrfin_real, "ua", None, units = "m/s")

V_real = getvar(wrfin_real, 'va', None, units = "m/s")
PH_real = wrfin_real.variables['PH'][:, :, :, :]
PHB_real = wrfin_real.variables['PHB'][:, :, :, :]
height_real = 0.5*(PHB_real[:,:-1] + PH_real[:,:-1] + PHB_real[: , 1:] + PH_real[:, 1:])/9.81
height_real /= 1000
# %% wrffdda variables
print("Assigning wrffdda variables")
times = wrffdda.variables['Times'][:]
U_old = wrffdda.variables['U_NDG_OLD'][0, :, :, :]
U_new = wrffdda.variables['U_NDG_NEW'][0, :, :, :]
V_old = wrffdda.variables['V_NDG_OLD'][0, :, :, :]
V_new = wrffdda.variables['V_NDG_NEW'][0, :, :, :]
T_old = wrffdda.variables['T_NDG_OLD'][0, :, :, :]
T_new = wrffdda.variables['T_NDG_NEW'][0, :, :, :]
Q_old = wrffdda.variables['Q_NDG_OLD'][0, :, :, :]
Q_new = wrffdda.variables['Q_NDG_NEW'][0, :, :, :]
PH_old = wrffdda.variables['PH_NDG_OLD'][0, :, :, :]
PH_new = wrffdda.variables['PH_NDG_NEW'][0, :, :, :]
MU_new = wrffdda.variables['MU_NDG_NEW'][0, :, :, :]
MU_old = wrffdda.variables['MU_NDG_OLD'][0, :, :, :]
# %% Here I will interpolate the heights of the wrffdda to the heights of the wrfinput
print("Interpolating the heights from the wrfin_real")
wrffdda_u_old_height = vinterp(wrfin_real, U_old, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_v_old_height = vinterp(wrfin_real, V_old, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_t_old_height = vinterp(wrfin_real, T_old, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_q_old_height = vinterp(wrfin_real, Q_old, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_u_new_height = vinterp(wrfin_real, U_new, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_v_new_height = vinterp(wrfin_real, V_new, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_t_new_height = vinterp(wrfin_real, T_new, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
wrffdda_q_new_height = vinterp(wrfin_real, Q_new, 'ght_agl', height_real[0, :, 0, 0], extrapolate = True)
#what this line does is it interpolates the heights from the wrfin file, and attaches those
#heights to the U_old variable. Note, this is in KM not meters so there will need to be 
#another conversion.
print("Interpolating the heights from the wrfin_ideal")
wrfin_u = vinterp(wrfin_ideal, wrffdda_u_old_height, 'ght_agl', height_ideal[0, :, 0, 0], extrapolate = True)
wrfin_v = vinterp(wrfin_ideal, wrffdda_v_old_height, 'ght_agl', height_ideal[0, :, 0, 0], extrapolate = True)
wrfin_q = vinterp(wrfin_ideal, wrffdda_q_old_height, 'ght_agl', height_ideal[0, :, 0, 0], extrapolate = True)
wrfin_t = vinterp(wrfin_ideal, wrffdda_t_old_height, 'ght_agl', height_ideal[0, :, 0, 0], extrapolate = True)
# %% Writing to the file
print("I am now writing to the file")
ncfile = nc.Dataset('/home/jbenik/FirefluxII/Codes_and_Data/Data/wrf_files/wrffdda_d01_test5', mode = 'w', format = 'NETCDF4_CLASSIC')
time = ncfile.createDimension('Time', 2) #Time
bottom_top = ncfile.createDimension('bottom_top', 159) #bottom_top def
one_stag = ncfile.createDimension('one_stag', 1) #one stag
south_north = ncfile.createDimension('south_north', 319)
west_east = ncfile.createDimension('west_east', 199)
for dim in ncfile.dimensions.items():
    print(dim)
ncfile.subtitle = 'My model data subtitle'
ncfile.anything = 'WRITE ANYTHIBNG'
print(ncfile.subtitle)
print(ncfile)
print(ncfile.anything)

# %% Creating the old variables in the wrffdda file
print("Creating the variables")
Times = ncfile.createVariable('Times', np.dtype('|S1'), ('Time'))

U_NDG_OLD = ncfile.createVariable('U_NDG_OLD', np.float32, ('Time', 'bottom_top', 'south_north', 'west_east'))
U_NDG_OLD.FieldType = 104
U_NDG_OLD.MemoryOrder = 'XYZ'
U_NDG_OLD.description = 'OLD X WIND FOR FDDA GRID NUDGING'
U_NDG_OLD.units = 'm s-1'
U_NDG_OLD.stagger = ''
U_NDG_OLD.coordinates = 'XLONG XLAT XTIME'

V_NDG_OLD = ncfile.createVariable('V_NDG_OLD', np.float32, ('Time', 'bottom_top', 'south_north', 'west_east'))
V_NDG_OLD.FieldType = 104
V_NDG_OLD.MemoryOrder = 'XYZ'
V_NDG_OLD.description = 'OLD Y WIND FOR FDDA GRID NUDGING'
V_NDG_OLD.units = 'm s-1'
V_NDG_OLD.stagger = ''
V_NDG_OLD.coordinates = 'XLONG XLAT XTIME'

T_NDG_OLD = ncfile.createVariable('T_NDG_OLD', np.float32, ('Time', 'bottom_top', 'south_north', 'west_east'))
T_NDG_OLD.FieldType = 104
T_NDG_OLD.MemoryOrder = 'XYZ'
T_NDG_OLD.description = 'OLD PERT POT TEMP FOR FDDA GRID NUDGING'
T_NDG_OLD.units = 'K'
T_NDG_OLD.stagger = ''
T_NDG_OLD.coordinates = 'XLONG XLAT XTIME'

Q_NDG_OLD = ncfile.createVariable('Q_NDG_OLD', np.float32, ('Time', 'bottom_top', 'south_north', 'west_east'))
Q_NDG_OLD.FieldType = 104
Q_NDG_OLD.MemoryOrder = 'XYZ'
Q_NDG_OLD.description = 'OLD WATER VAPOR MIX RATIO FOR FDDA GRID NUDGING'
Q_NDG_OLD.units = 'kg/kg'
Q_NDG_OLD.stagger = ''
Q_NDG_OLD.coordinates = 'XLONG XLAT XTIME'

PH_NDG_OLD = ncfile.createVariable('PH_NDG_OLD', np.float32, ('Time', 'bottom_top', 'south_north', 'west_east'))
PH_NDG_OLD.FieldType = 104
PH_NDG_OLD.MemoryOrder = 'XYZ'
PH_NDG_OLD.description = 'OLD PERT GEOPOTENTIAL FOR FDDA GRID NUDGING'
PH_NDG_OLD.units = 'kg/kg'
PH_NDG_OLD.stagger = ''
PH_NDG_OLD.coordinates = 'XLONG XLAT XTIME'

# %%Creating the new variables in the file
print("Creating the new variables")
U_NDG_NEW = ncfile.createVariable('U_NDG_NEW', np.float32, ('Time', 'bottom_top', 'south_north', 'west_east'))
U_NDG_NEW.FieldType = 104
U_NDG_NEW.MemoryOrder = 'XYZ'
U_NDG_NEW.description = 'NEW X WIND FOR FDDA GRID NUDGING'
U_NDG_NEW.units = 'm s-1'
U_NDG_NEW.stagger = ''
U_NDG_NEW.coordinates = 'XLONG XLAT XTIME'

V_NDG_NEW = ncfile.createVariable('V_NDG_NEW', np.float32, ('Time', 'bottom_top', 'south_north', 'west_east'))
V_NDG_NEW.FieldType = 104
V_NDG_NEW.MemoryOrder = 'XYZ'
V_NDG_NEW.description = 'NEW Y WIND FOR FDDA GRID NUDGING'
V_NDG_NEW.units = 'm s-1'
V_NDG_NEW.stagger = ''
V_NDG_NEW.coordinates = 'XLONG XLAT XTIME'

T_NDG_NEW = ncfile.createVariable('T_NDG_NEW', np.float32, ('Time', 'bottom_top', 'south_north', 'west_east'))
T_NDG_NEW.FieldType = 104
T_NDG_NEW.MemoryOrder = 'XYZ'
T_NDG_NEW.description = 'NEW PERT POT TEMP FOR FDDA GRID NUDGING'
T_NDG_NEW.units = 'K'
T_NDG_NEW.stagger = ''
T_NDG_NEW.coordinates = 'XLONG XLAT XTIME'

Q_NDG_NEW = ncfile.createVariable('Q_NDG_NEW', np.float32, ('Time', 'bottom_top', 'south_north', 'west_east'))
Q_NDG_NEW.FieldType = 104
Q_NDG_NEW.MemoryOrder = 'XYZ'
Q_NDG_NEW.description = 'NEW WATER VAPOR MIX RATIO FOR FDDA GRID NUDGING'
Q_NDG_NEW.units = 'kg/kg'
Q_NDG_NEW.stagger = ''
Q_NDG_NEW.coordinates = 'XLONG XLAT XTIME'

PH_NDG_NEW = ncfile.createVariable('PH_NDG_NEW', np.float32, ('Time', 'bottom_top', 'south_north', 'west_east'))
PH_NDG_NEW.FieldType = 104
PH_NDG_NEW.MemoryOrder = 'XYZ'
PH_NDG_NEW.description = 'NEW PERT GEOPOTENTIAL FOR FDDA GRID NUDGING'
PH_NDG_NEW.units = 'kg/kg'
PH_NDG_NEW.stagger = ''
PH_NDG_NEW.coordinates = 'XLONG XLAT XTIME'

MU_NDG_OLD = ncfile.createVariable('MU_NDG_OLD', np.float32, ('Time', 'one_stag', 'south_north', 'west_east'))
MU_NDG_OLD.FieldType = 104
MU_NDG_OLD.MemoryOrder = 'XYZ'
MU_NDG_OLD.description = 'OLD PERT COLUMN DRY MASS FOR FDDA GRID NUDGING'
MU_NDG_OLD.units = 'Pa'
MU_NDG_OLD.stagger = 'Z'
MU_NDG_OLD.coordinates = 'XLONG XLAT XTIME'

MU_NDG_NEW = ncfile.createVariable('MU_NDG_NEW', np.float32, ('Time', 'one_stag', 'south_north', 'west_east'))
MU_NDG_NEW.FieldType = 104
MU_NDG_NEW.MemoryOrder = 'XYZ'
MU_NDG_NEW.description = 'NEW PERT COLUMN DRY MASS FOR FDDA GRID NUDGING'
MU_NDG_NEW.units = 'Pa'
MU_NDG_NEW.stagger = 'Z'
MU_NDG_NEW.coordinates = 'XLONG XLAT XTIME'

print("Assigning the variables")
Times[:] = time
print("Assigning the variables at the first timestep (timestep 0)")
U_NDG_OLD[0, :, :, :] = wrfin_u
V_NDG_OLD[0, :, :, :] = wrfin_v
T_NDG_OLD[0, :, :, :] = wrfin_t
Q_NDG_OLD[0, :, :, :] = wrfin_q
PH_NDG_OLD[0, :, :, :] = PH_old
MU_NDG_OLD[0, :, :, :] = MU_old

U_NDG_NEW[0, :, :, :] = wrfin_u
V_NDG_NEW[0, :, :, :] = wrfin_v
T_NDG_NEW[0, :, :, :] = wrfin_t
Q_NDG_NEW[0, :, :, :] = wrfin_q
PH_NDG_NEW[0, :, :, :] = PH_new
MU_NDG_NEW[0, :, :, :] = MU_new
print("Assigning the variables at the second timestep (timestep 1)")
U_NDG_OLD[1, :, :, :] = wrfin_u
V_NDG_OLD[1, :, :, :] = wrfin_v
T_NDG_OLD[1, :, :, :] = wrfin_t
Q_NDG_OLD[1, :, :, :] = wrfin_q
PH_NDG_OLD[1, :, :, :] = PH_old
MU_NDG_OLD[1, :, :, :] = MU_old

U_NDG_NEW[1, :, :, :] = wrfin_u
V_NDG_NEW[1, :, :, :] = wrfin_v
T_NDG_NEW[1, :, :, :] = wrfin_t
Q_NDG_NEW[1, :, :, :] = wrfin_q
PH_NDG_NEW[1, :, :, :] = PH_new
MU_NDG_NEW[1, :, :, :] = MU_new
ncfile.close(); print('Dataset is closed!')