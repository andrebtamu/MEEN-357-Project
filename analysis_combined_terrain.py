import numpy as np
from subfunctions import *
#from Lab3_DefineRover import *
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

rover, planet = define_rover_1()
slope_list_deg = np.linspace(-10,35,25)
Crr_list = np.linspace(0.01,0.4,25)
omega_max = np.zeros(len(slope_list_deg), dtype = float)
omega_nl = rover['wheel_assembly']['motor']['speed_noload']

# find where F_net == 0
for i in range(len(slope_list_deg)):
    fun = lambda omega: F_net(omega, float(slope_list_deg[i]), rover, planet, Crr_list[i])
    if (slope_list_deg[i] < 0) and (Crr_list[i] < 0.177):
        omega_max[i] = "NaN"
        continue
    else:
        sol = root_scalar(fun, method='bisect', bracket=[0, omega_nl])
        omega_max[i] = sol.root 

Crr, Slope = np.meshgrid (Crr_list, slope_list_deg)
VMAX = np.zeros(np.shape(Crr), dtype = float)
N = np.shape(Crr)[0]

for i in range(N):
    for j in range(N):
        Crr_sample = float(Crr[i,j])
        slope_sample = float(Slope[i,j])
        fun = lambda omega: F_net(omega, float(Crr_sample), rover, planet, slope_sample)
        if (slope_list_deg[i] < 0) and (Crr_list[i] < 0.177):
            omega_max[i] = "NaN"
            continue
        else:
            sol = root_scalar(fun, method='bisect', bracket=[0, omega_nl])
            VMAX[i,j] = sol.root
        
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(Crr, Slope, VMAX)
ax.set_title("Max Rover Speed:Varying Terrain angles and Rolling Resistances")
ax.set_xlabel('Crr')
ax.set_ylabel('Terrain Angle [deg]')
ax.set_zlabel('Max Rover Speed [m/s]')
