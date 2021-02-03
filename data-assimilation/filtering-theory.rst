################
Filtering theory
################

Assume a dynamical system that is governed by a stochastic difference equation:

.. math::

   dx_t = f(x_t, t)+G(x_t,t)d \beta_t

for all times, :math:`t \geq 0`. Observations occur at discrete times:

.. math::

   y_k=h(x_k,t_k)+\nu_k

where :math:`k=1,2,...;` and :math:`t_{k+1} > t_k \geq t_0`.

The observational error is white in time and is Gaussian (this latter
assumption is not essential).

.. math::

   \nu_k \rightarrow N(0,R_k)

The complete history of observations is:

.. math::

   Y_\tau=\{y_l;t_l \leq \tau\}

Our goal is to find the probability distribution for the state at time
:math:`t`.

.. math::

   p(x,t|Y_t)

The state between observation times is obtained from the difference equation.
We need to update the state given new observations:

.. math::

   p(x,t_k | Y_{t_k}) = p(x,t_k |y_k, Y_{t_{k-1}})


We do so by applying Bayes' rule:

.. math::

   p(x,t_k | Y_{t_k}) = \frac{p(y_k |x_k, Y_{t_{k-1}}) p(x,t_k | Y_{t_{k-1}})}{p(y_k, Y_{t_{k-1}})}

Since the error is white in time:

.. math::

   p(y_k | x_k, Y_{t_{k-1}})=p(y_k|x_k)

We integrate the numerator to obtain a normalizing denominator:

.. math::

      p(y_k | x_k, Y_{t_{k-1}})= \int p(y_k|x) p(x,t_k |Y_{t_{k-1}})dx

This allows us to update the probability after a new observation:

.. math::

   p(x,t_k | Y_{t_k}) = \frac{p(y_k|x) p(x,t_k |Y_{t_{k-1}})}{\int p(y_k|\xi) p(\xi,t_k |Y_{t_{k-1}})d\xi}