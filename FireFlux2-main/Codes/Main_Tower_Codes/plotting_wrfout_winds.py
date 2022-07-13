# %% Importing necessary libraries
import pickle
import matplotlib.pyplot as plt
# %% Opening the pickle file
with open('main_tower_winds_wrfout.pkl', 'rb') as f:
    results = pickle.load(f)

# %% Plotting 20 m wind

plt.plot(results['ws_h_20'], label = '20m Wind Speed', color = 'blue')
plt.xlabel('Time (s)', fontsize = 12, fontweight = 'bold')
plt.ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
plt.title('20 Meter Wind Speed From Wrfout file', fontsize = 18, fontweight = 'bold')
plt.legend()
plt.grid()
plt.show()
# %% Plotting 10 m wind

plt.plot(results['ws_h_10'], label = '10m Wind Speed', color = 'green')
plt.xlabel('Time (s)', fontsize = 12, fontweight = 'bold')
plt.ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
plt.title('10 Meter Wind Speed From Wrfout file', fontsize = 18, fontweight = 'bold')
plt.legend()
plt.grid()
plt.show()

# %% Plotting 5.77 m wind
plt.plot(results['ws_h_577'], label = '5.77m Wind Speed', color = 'red')
plt.xlabel('Time (s)', fontsize = 12, fontweight = 'bold')
plt.ylabel('Wind Speed (m/s)', fontsize = 12, fontweight = 'bold')
plt.title('5.77 Meter Wind Speed From Wrfout file', fontsize = 18, fontweight = 'bold')
plt.legend()
plt.grid()
plt.show()
