# PACKAGES
import math 
import numpy as np
import scipy.special as spe
from scipy.integrate import cumulative_trapezoid
from numpy.polynomial import polynomial as P

# PLANAR PENDULUM
def planpend(S, t, l=1, g=9.81):
   th0, ph0, dth0, dph0 = S
   w_2 = g/l
   h = .5*dth0**2 - w_2*np.cos(th0)
   if (th0 == 0 or th0 == np.pi) and dth0 == 0:
      th = th0*np.ones(len(t))
   else:
      if h == w_2:
         th = 2* np.arcsin(np.tanh(np.arctanh(np.sin(th0/2)) + math.copysign(1, dth0)*np.sqrt(w_2)*t))
      elif h < w_2:
         beta = np.arccos(-(h+1e-8)/w_2)
         k = np.sin(beta/2)
         K = spe.ellipkinc(np.arcsin(np.sin(th0/2)/k), k**2)
         sn = spe.ellipj(K+math.copysign(1, dth0)*np.sqrt(w_2)*t, k**2)[0]
         th = 2*np.arcsin(k*sn)
      elif h > w_2:
         m1 = 2*w_2/(h+w_2)
         K = spe.ellipkinc(th0/2, m1)
         sn, cn, dn, phJ = spe.ellipj(K + math.copysign(1, dth0)*np.sqrt((h + w_2)/2)*t,m1)
         th = 2*phJ
   ph = ph0*np.ones(len(t))
   return th, ph

# SPHERICAL PENDULUM

def sphpend(S0, t, l=1, g=9.81):
    th0, ph0, dth0, dph0 = S0
    p_ph = np.sin(th0)**2*dph0
    w_2 = g/l
    k = np.cos(th0)
    h = .5*(dth0**2 + p_ph**2/np.sin(th0)**2) - w_2*np.cos(th0)
    p = (.5*p_ph**2/w_2 - h/w_2, -1, h/w_2, 1)
    b3, b2, b1 = P.polyroots(p)
    lamba, m = .5*np.sqrt(b1 - b3), (b1 - b2)/(b1 - b3)
    if dth0 ==0:
        arg = spe.ellipk(m) - math.copysign(1, dth0)*lamba*np.sqrt(2*w_2)*t
    else:
        vph0 = np.arcsin(np.sqrt((k - b2)/m/(k - b3)))
        arg = spe.ellipkinc(vph0, m) - math.copysign(1, dth0)*lamba*np.sqrt(2*w_2)*t
    th = np.arccos((m*b3*spe.ellipj(arg,m)[0]**2 - b2)/(m*spe.ellipj(arg,m)[0]**2 - 1))
    fun = p_ph/np.sin(th)**2
    I = cumulative_trapezoid(fun, t)
    ph = np.concatenate((np.array([0]), ph0 + I))
    return th, ph
