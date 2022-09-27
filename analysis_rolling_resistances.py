import numpy as np
from subfunctions import *
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

Slope = 0 
rover, planet = define_rover_1()
Crr_list = np.linspace(0.01,0.4,25)
omega_max = np.zeros(len(Crr_list), dtype = float)
omega_nl = rover['wheel_assembly']['motor']['speed_noload']

# find where F_net == 0
for i in range(len(Crr_list)):
    fun = lambda omega: F_net(omega, Slope, rover, planet,  float(Crr_list[i]))
    sol = root_scalar(fun, method='bisect', bracket=[0, omega_nl])
    omega_max[i] = sol.root #list of omega_max at each slope

plt.plot(Crr_list,omega_max)
plt.xlabel('Rolling Resistance Coefficient')
plt.ylabel('Max Rover Speed [m/s]')
