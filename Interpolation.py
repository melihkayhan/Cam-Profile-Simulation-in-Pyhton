import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# Definitions
alpha = np.linspace(0,360, 361)
# print(alpha)
n_values = len(alpha)
T = 1
t = np.linspace(0,T, n_values)

R = 2
xmin = 20
hub = 10
xmax = xmin + hub
omega = 2*np.pi / T

# Define the angles
alpha1 = 80;
alpha2 = 100;
alpha3 = 140;
alpha4 = 180;

alphas = np.array([0, alpha1, alpha2, alpha3, alpha4, 360])
print(alphas)
x_werte = np.array([xmin, xmin, xmax, xmax, xmin, xmin])

# x_interp  = interp1d(x_werte, alphas, kind='linear')
x_interp  = np.interp(alpha, alphas, x_werte)
v_interp = np.gradient(x_interp, t)
a_interp = np.gradient(v_interp, t)

fig = plt.figure()

plt.subplot(4, 1, 1)
plt.plot(alpha, x_interp)
plt.title('x[mm] over angle [deg]')

plt.subplot(4, 1, 2)
plt.plot(t, x_interp)
plt.title('x[mm] over time [s]')

plt.subplot(4, 1, 3)
plt.plot(t, v_interp)
plt.title('v[mm/s] over time [s]')

plt.subplot(4, 1, 4)
plt.plot(t, a_interp)
plt.title('a[mm/s^2] over time [s]')

fig.tight_layout()
plt.show()

