import numpy as np
from scipy.optimize import root
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import scienceplots

plt.style.use(['science', 'no-latex'])

def pot(th, S0, w):
    th0, dth0, dph0 = S0
    p_ph = np.sin(th0)**2*dph0
    k = np.cos(th0)
    h = .5*(dth0**2+p_ph**2/np.sin(th0)**2)-w*np.cos(th0)
    return .5*p_ph**2/np.sin(th)**2-w*np.cos(th), h

def pot_root(S0, guess1, guess2, w):
    aux = lambda x: pot(x, S0, w)[0] - pot(x, S0, w)[1]
    root1, root2 = root(aux, guess1).x, root(aux, guess2).x
    return root1, root2

th = np.linspace(0, np.pi, 1000)
def myfigure():
    fig, ax = plt.subplots(1, 1, figsize = (8,6))
    plt.subplots_adjust(bottom=.18)
    ax.set_xlim(0, np.pi)
    ax.set_ylim(-10, 50)
    ax.set_title('Effective potential')
    ax.set_xlabel(r"$\theta$")
    ax_Thslid = plt.axes([.17, 0.07, .65, .03], facecolor='lightgoldenrodyellow')
    ax_dPhslid = plt.axes([.17, 0.04, .65, .03], facecolor='lightgoldenrodyellow')
    ax_wslid = plt.axes([.17, 0.01, .65, .03], facecolor='lightgoldenrodyellow')
    Thslid = Slider(ax_Thslid, label=r'$\theta_0$', valmin=.6, valmax = 2.6, valinit = 1)
    dPhslid = Slider(ax_dPhslid, label=r'$\dot{\phi}_0$', valmin=0.3, valmax = 2, valinit = 1)
    wslid = Slider(ax_wslid, label=r'$\omega^2$', valmin=5, valmax = 15, valinit = 9.81)
    return fig, ax, Thslid, dPhslid, wslid

def animate(fig, ax, Thslid, dPhslid, wslid):
    guess1, guess2 = 0.1, np.pi-0.1
    root1, root2 = pot_root(np.array([1, 0, 1]), guess1, guess2, 9.81)
    l1, = ax.plot(th, pot(th, np.array([1, 0, 1]), 9.81)[0], label=r'$V_{eff}(\theta)$')
    l2, = ax.plot(th, pot(th, np.array([1, 0, 1]), 9.81)[1]*np.ones(len(th)), '--', label=r'$h$')
    l3, = ax.plot(root1, pot(root1, np.array([1, 0, 1]), 9.81)[0], 'o', label=r'$root1$')
    l4, = ax.plot(root1, pot(root2, np.array([1, 0, 1]), 9.81)[0], 'o', label=r'$root2$')
    ax.legend(loc='upper right')
    plt.pause(0.005)
    while plt.fignum_exists(fig.number):
        Th = Thslid.val
        dPh = dPhslid.val
        w = wslid.val
        root1, root2 = pot_root(np.array([Th, 0, dPh]), guess1, guess2, w)
        guess1, guess2 = root1, root2
        l1.set_data(th, pot(th, np.array([Th, 0, dPh]), w)[0])
        l2.set_data(th, pot(th, np.array([Th, 0, dPh]), w)[1]*np.ones(len(th)))
        l3.set_data(root1, pot(root1, np.array([Th, 0, dPh]), w)[0])
        l4.set_data(root2, pot(root2, np.array([Th, 0, dPh]), w)[0])
        plt.pause(0.005)

fig, ax, Thslid, dPhslid, wslid = myfigure()
animate(fig, ax, Thslid, dPhslid, wslid)

plt.show()
