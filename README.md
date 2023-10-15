# Spherical-Pendulum
Animation of a simple pendulum with free 3D motion

# Theoretical Frame
## Lagrange Formalism
The system to study consists on a point particle of mass $m$, attached to a pivot point by a massless rigid rod of length $l$. The position of the particle is then subject to the constraint $\vec{r}^2-l^2 = 0$. Then, we have 2 degrees of freedom (1 part, 3D, 1 const), so we require 2 generalized coordinates. It is convenient to use the polar (here, $wrt$ the negative z axis) and azimuthal angles from spherical coordinates: 
$$\vec{q} = (\theta, \phi) \ , \ \vec{r} = l(\sin(\theta)\cos(\phi), \sin(\theta)\sin(\phi), -\cos(\theta))$$

The forces acting on the particle are the gravitational pull, $\vec{F}_g = -mg\vec{e}_z$ and the string force, $\vec{F}_s$. For the first one, the force is conservative, with $\vec{F}_g = -\nabla V$, $V = mgz$. On the other hand, if we consider any virtual displacement $\vec{r}(u)$, it will be tangential to the circle of radius $l$, and the string force is assumed to be $\vec{F}_s = F_s \vec{e}_r$, so $\vec{F}_s \parallel \frac{d}{du}\vec{r}du$, so the Principle of Virtual Work is satisfied. Under these circumstances, the Lagrangian formalism can be applied, with a Lagrangian $L = T-V$.

$$T = \frac{1}{2}m\dot{\vec{r}}^2 = \frac{1}{2}ml^2\left[\dot{\theta}^2+sin^2(\theta)\dot{\phi}^2\right] \ ; \ V = mgz = -mglcos(\theta)$$
$$L(t, \vec{q}, \dot{\vec{q}}) = \frac{1}{2}\left[\dot{\theta}^2+sin^2(\theta)\dot{\phi}^2\right]+\omega_0^2cos(\theta)$$
 where we have divided by $ml^2$ (the E-L equations are invariant under multiplications by constants on $L$) and defined $\omega_0 = \sqrt{g/l}$.

 Let us present the canonical momenta: 
 $$\vec{p}= \frac{\partial L}{\partial \dot{\vec{q}}} \implies p_{\theta} = \frac{\partial L}{\partial \dot{\theta}} = \dot{\theta} \ , \  p_{\phi} = \frac{\partial L}{\partial \dot{\phi}} = sin^2(\theta)\dot{\phi}$$
 As $\frac{\partial L}{\partial \phi}= 0$, so then $p_{\phi}$ is a constant of motion.

 The Energy Integral (a.k.a Jacobi Integral) is defined as $h = \vec{p} \cdot \dot{\vec{q}}-L$. 

 $$ h(t, \vec{q}, \dot{\vec{q}}) = \frac{1}{2}\left[\dot{\theta}^2+\sin^2(\theta)\dot{\phi}^2\right]-\omega_0^2\cos(\theta)= \frac{1}{2}\left[\dot{\theta}^2+\frac{p_{\phi}^2}{\sin^2(\theta)}\right]-\omega_0^2\cos(\theta) = \frac{1}{2}\dot{\theta}^2+U(\theta)$$

 where $U(\theta) = \frac{p_{\phi}^2}{2sin^2(\theta)}-\omega_0^2cos(\theta)$ is the effective potential.

 Notice that $\frac{\partial L}{\partial t}=0$, then $\frac{dh}{dt} = 0$, so $h$ is also a constant of motion.

 ## Integrating the system
 We have obtained a system of ODE's:
 $$\dot{\phi} = \frac{p_{\phi}}{\sin^2(\theta)} \ , \ h = \frac{1}{2}\theta^2+U(\theta)$$

The second one is equivalent to a particle of unit mass under a 1D potential. We can solve the system by integrating the equation: 

$$ \int_{\theta_0}^\theta \frac{d \alpha}{\sqrt{h-U(\alpha)}} = \pm \sqrt{2}t$$

with $(\theta(0), \phi(0)) = (\theta_0, \phi_0)$. As $h$ is constant, we have $h = \frac{1}{2}\dot{\theta}_0^2+\frac{p_{\phi}^2}{2sin(\theta)}^2-\omega_0^2cos(\theta)$. Let us perform the change 

$$u = cos(\alpha)/k \ , \ k = cos(\alpha_0) \implies du = -sin(\alpha)/k d\alpha \ ; \ \alpha = \theta_0 \rightarrow u = 1 \ , \ \ \alpha = \theta_0 \rightarrow u = cos(\theta)/k = \eta(\theta)$$. 
