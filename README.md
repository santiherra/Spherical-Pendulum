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

with $(\theta(0), \phi(0)) = (\theta_0, \phi_0)$.
 ### Planar case

 ### General case
Now, we confront a more general system, where $\dot{\phi}(0) = \dot{\phi}_0 \neq 0$. Let us perform the change 

$$u = \frac{cos(\alpha)}{\kappa} \ , \ \kappa = cos(\alpha_0) \implies du = -\frac{sin(\alpha)}{\kappa} d\alpha \ ; \ \alpha = \theta_0 \rightarrow u = 1 \ , \ \ \alpha = \theta_0 \rightarrow u = \frac{cos(\theta)}{\kappa} = \eta(\theta)$$

$$ \int_{1}^{\eta(\theta)}\frac{du}{\sqrt{P(u)}} = \mp \sqrt{\frac{2}{\kappa^2}}t \ ; \ P(u) = \left(h-\frac{p_{\phi}^2}{2}\right)+\omega_0^2\kappa u-h\kappa^2 u^2-\omega_0^2 \kappa^3 u^3$$

Let us denote $\beta_1>\beta_2>\beta_3$ ($\beta_1, \beta_2, \beta_3 \in \mathbb{R}$) the roots of $P(u)$. We are now ready to perform a reduction of the integral to Incomplete Elliptic Integrals of the First Kind, following the instructions by Abramowitz \& Stegun (pg. 597, 17.4.62):

$$ \int_{1}^{\eta(\theta)}\frac{du}{\sqrt{P(u)}} = \int_{\beta_1}^{\eta(\theta)}\frac{du}{\sqrt{P(u)}}-\int_{\beta_1}^{1}\frac{du}{\sqrt{P(u)}} = \frac{1}{\lambda}\left[F(\varphi \ ; \ m)-F(\varphi_0 \ ; \ m)\right]$$

$$\lambda = \frac{1}{2}\sqrt{\beta_1-\beta_3} \ ; \ m = \frac{\beta_2-\beta_3}{\beta_1-\beta_3} \ ; \ sin^2(\phi) = \frac{\eta(\theta)-\beta_3}{\beta_2-\beta_3} \ ; \ \varphi_0 = \sin^{-1}\left(\sqrt{\frac{1-\beta_3}{\beta_2-\beta_3}}\right)$$

with $F(\phi \ ; \ m)$ is the Incomplete Elliptic Integral of the First Kind. We are then left with

$$ F(\varphi \ ; \ m) = F(\varphi_0 \ ; \ m)\mp \lambda \sqrt{\frac{2}{\kappa^2}}t \implies sin^2(\varphi) = sn^2\left(F(\varphi_0 \ ; \ m)\mp \lambda \sqrt{\frac{2}{\kappa^2}}t \ ; \ m \right)  $$

$$ \implies \theta(t) = cos^{-1}\left[\kappa \beta_2 sn^2\left(F(\varphi_0 \ ; \ m)\mp \lambda \sqrt{\frac{2}{\kappa^2}}t \ ; \ m \right)+ \kappa \beta_3 cn^2\left(F(\varphi_0 \ ; \ m)\mp \lambda \sqrt{\frac{2}{\kappa^2}}t \ ; \ m \right)\right]$$

In order to obtain $\phi (t)$, we need to recall: $\dot(\phi) = \frac{p_{\phi}}{sin^2(\theta)}$. Integrating:

$$ \phi (t) = \phi_0+p_{\phi}\int_{0}^t\frac{d\tau}{sin^2(\theta(\tau))} $$


