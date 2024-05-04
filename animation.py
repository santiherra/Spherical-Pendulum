from exactsol import planpend
from exactsol import sphpend
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scienceplots

plt.style.use(['science', 'no-latex'])

'''INITIALIZATION'''
tf = float(input('Simulation time: '))  # SUGGESTION: more than 10
Nt = int(input('Time steps: '))         # SUGGESTION: around 500 or 1000
t = np.linspace(0, tf, Nt)
dth0 = float(input('Initial polar velocity: '))
dph0 = float(input('Initial azimuth. velocity: '))
if int(dph0) == 0:
    ph0 = 0
    planar = True
else:
    ph0 = float(input('Initial azimuth. angle: '))
    planar = False
th0 = float(input('Initial polar angle: '))
S0 = np.array([th0, ph0, dth0, dph0])

adjust = str(input('Adjust parameters?: '))
if adjust == 'Yes' or adjust == 'yes':
    l = float(input('Pendulum length: '))
    g = float(input('Gravity constant: '))
elif adjust == 'No' or adjust == 'no':
    l, g = 1, 9.81
    print('Default values: l = ' + str(l) + ' , g = ' + str(g))

def Cartesian(th, ph, l = 1):
    return l*np.sin(th)*np.cos(ph), l*np.sin(th)*np.sin(ph), -l*np.cos(th)


'''PLOTS AND ANIMATIONS'''
def planar_plot():
    fig, ax = plt.subplots(1, 1, figsize = (5, 5))
    shadow, = ax.plot([], [], color='green', lw=2, alpha=.4)
    line, = ax.plot([], [], 'o-', color='green', lw=1, markersize=4)
    lim = 1.1*l
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_xlabel('x')
    ax.set_ylabel('z')
    ax.set_title('Planar case')
    timer = ax.text(.7*l, .7*l, '', bbox=dict(facecolor='white', edgecolor='black'))
    return fig, ax, shadow, line, timer

def sph_plot():
    fig, ax = plt.subplots(figsize = (5,5), subplot_kw={'projection':'3d'})
    shadow, = ax.plot([], [], [-l*1.1], color='red', lw=.5)
    line, = ax.plot([], [], [], 'o-', lw=1, markersize=4)
    lim = 1.1*l
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Spherical case')
    timer = ax.text(.7*l, .7*l, .7*l, '', bbox=dict(facecolor='white', edgecolor='black'))
    return fig, ax, shadow, line, timer

if planar == True:
    S = planpend(S0, t, l, g)
    X, Y, Z = Cartesian(S[0], S[1], l)
    fig, ax, shadow, line, timer= planar_plot()
    trail = int(input('Trail : '))
    def anime(i):
        shadow.set_data(X[i-trail:i+1], Z[i-trail:i+1])
        line.set_data([0, X[i]], [0, Z[i]])
        timer.set_text("t = " + str(round(t[i], 2)))
        return shadow, line, timer
else: 
    S = sphpend(S0, t, l, g)
    X, Y, Z = Cartesian(S[0], S[1], l)
    fig, ax, shadow, line, timer = sph_plot()
    def anime(i):
        shadow.set_data(X[:i+1], Y[:i+1])
        shadow.set_3d_properties(-l*1.1)
        line.set_data([0, X[i]], [0, Y[i]])
        line.set_3d_properties([0, Z[i]])
        timer.set_text("t = " + str(round(t[i], 2)))
        return shadow, line, timer
    
ani = FuncAnimation(fig, anime, frames=len(t), interval=20, blit=True)

plt.show()
