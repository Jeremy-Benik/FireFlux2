# %% Importing necessary Libraries
import netCDF4 as nc
import pickle
import os.path as osp
import wrf
# %% Getting the variables from the modified wrfout_file
#out_path = 'main_tower_winds_wrfout.pkl' #To change the file, change this name
out_path = 'main_tower_wrfout_coupled_uf_vf_wind_speed.pkl' #this is the no fire run, comment this out or the line above out
if not osp.exists(out_path):
    # %% Assigning tower coords
    #These values can be found in the code titled finding_towers_ideal.py. 
    # these values are not on the subgrid
    print('Setting indices for the towers')
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
    # %% Reading in the data
    # Wrfout file 
    print("Reading in the wrfout file from the ideal case")
    wrfout = nc.Dataset('/home/jbenik/FireFlux2/Codes_and_Data/Data/wrf_files/wrfout_files/wrfout_d01_2013-01-30_15:00:00', 'r')
    # %%
    # To get the variables from thw wrfout file, I am using the wrf library to get them so they won't be staggered in the grid
    print("I am getting the u variable from the wrfout file")
    print('getting uf winds')
    uf = wrfout.variables['UF'][:, y_main_sub, x_main_sub]
    print('getting vf winds')
    vf = wrfout.variables['VF'][:, y_main_sub, x_main_sub]
    print('getting heights')
    ht = wrf.getvar(wrfout, "z", units="m", msl = False)[:, y_main, x_main]
    # %%
    # 20 meters
    print("Interpolating heights")
    print("Interpolating U at 20 meters")
    Uf_h_20 = wrf.interplevel(uf, ht, 20) # Run this for all time
    print("Interpolating V at 20 meters")
    Vf_h_20 = wrf.interplevel(vf, ht, 20)
    print("Calculating Wind Speed")
    wsf_h_20_fire = np.sqrt((Uf_h_20 ** 2) + (Vf_h_20 ** 2))

    # 10 meters
    print("Interpolating U at 10 meters")
    Uf_h_10 = wrf.interplevel(uf, ht, 10) # Run this for all time
    print("Interpolating V at 20 meters")
    Vf_h_10 = wrf.interplevel(v_f, ht, 10)
    print("Calculating Wind Speed")
    wsf_h_10_fire = np.sqrt((Uf_h_10 ** 2) + (Vf_h_10 ** 2))

    # 5.77 meters
    print("Interpolating U at 5.77 meters")
    Uf_h_577 = wrf.interplevel(uf, ht, 5.77) # Run this for all time
    print("Interpolating V at 20 meters")
    Vf_h_577 = wrf.interplevel(v_f, ht, 5.77)
    print("Calculating Wind Speed")
    wsf_h_577_fire = np.sqrt((Uf_h_577 ** 2) + (Vf_h_577 ** 2))

    wrfout_time_no_fire = wrfout.variables['XTIME'][:]
    # %% Saving the results into new file
    
    results = {'wsf_h_20_fire': wsf_h_20_fire, 'wsf_h_10_fire':wsf_h_10_fire,
    'wsf_h_577_fire':wsf_h_577_fire} #put the other variables in here such as wsw and ww

    with open(out_path, 'wb') as f:
        pickle.dump(results, f)
else:
    with open(out_path, 'rb') as f:
        results = pickle.load(f)
    locals().update(results)
# %% Making a new plot of just the wrfout to se