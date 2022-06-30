import netCDF4 as nc
import xarray as xr
wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00', 'r')
wrfout_xr = xr.open_dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_d01_2013-01-30_15:00:00')

print(wrfout_xr)
time = wrfout.variables['XTIME'][:]
print(time)
print(len(time))
'''        float32 FIRE_AREA(Time, south_north_subgrid, west_east_subgrid) ;
                FIRE_AREA:FieldType = 104 ;
                FIRE_AREA:MemoryOrder = XY  ;
                FIRE_AREA:description = fraction of cell area on fire ;
                FIRE_AREA:units = 1 ;
                FIRE_AREA:stagger = Z ;'''
#fire_area = wrfout.variables['FIRE_AREA'][:, :, :]
#print(wrfout_xr.info())