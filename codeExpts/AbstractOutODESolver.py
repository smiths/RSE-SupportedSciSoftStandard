import numpy as np
from scipy.integrate import solve_ivp

# Parameters
T_C = 20.0
T_init = 80.0
tau_W = 10.0
dt = 0.1
t_end = 50.0

def dT_W_dt(t, T_W, T_C, tau_W):
    return (T_C - T_W) / tau_W

# Bind the parameters of our particular ODE
def derivative(t, T_W):
    return dT_W_dt(t, T_W, T_C, tau_W)

t_eval = np.arange(0, t_end + dt, dt)

solution = solve_ivp(
    derivative,
    (0, t_end),
    [T_init],
    t_eval=t_eval,
    method="RK45"
)

# Display results
for ti, Ti in zip(solution.t, solution.y[0]):
    print(f"{ti:6.2f}  {Ti:8.3f}")