# PACKAGES
import numpy as np
from scipy.special import ellipk
from scipy.special import ellipj
import matplotlib.pyplot as plt
from matplotlib import animation
import webbrowser

# ODE FUNCTION
def pend(S, t, m=1, l=1, g=9.81):
    theta0, phi0 = S
    omega0 = np.sqrt(g/l)
    k = np.sin(theta0/2)
    K = ellipk(k**2)
    return 2*np.arcsin(k*ellipj(K-omega0*t,k**2)[0]), np.zeros(len(t))

def cartesian(theta, phi, l=1):
    return l*np.sin(theta)*np.cos(phi), l*np.sin(theta)*np.sin(phi), -l*np.cos(theta)

S0 = np.array([np.pi/4, 0])
tf = np.linspace(0, 30, 1000)
th, phi= pend(S0, tf)
x, y, z = cartesian(th, phi)

# ANIMATION
fig= plt.figure()
ln, = plt.plot([], [], 'o-', color='green', lw=2)
sombra, = plt.plot([], [], color='red', lw=.5)
limx = max(x)*1.1
limz = min(z)*1.1
plt.xlim(- limx, limx)
plt.ylim(limz, 0.02)
plt.title(r"Trayectoria con respecto a $S'$")
plt.xlabel("x'")
plt.ylabel("z'")
plt.grid()
n = len(tf)

def anime(i):
  trail = 4
  ln.set_data([0, x[i]], [0, z[i]])
  sombra.set_data(x[i-trail:i+1], z[i-trail:i+1])
  return ln, sombra

ani = animation.FuncAnimation(fig, anime, frames=len(tf), interval=40, blit=True)
ani.save('pendulum.gif', writer='pillow', fps=30)
webbrowser.open('pendulum.gif')
