# Parameters
T_C = 20.0
T_init = 80.0
tau_W = 10.0
dt = 0.1
t_end = 50.0

t = [0.0]
T_W = [T_init]

while t[-1] < t_end:
    T = T_W[-1]

    # Euler update
    T_new = T + dt * (T_C - T) / tau_W
    t_new = t[-1] + dt

    t.append(t_new)
    T_W.append(T_new)

# Display results
for ti, Ti in zip(t, T_W):
    print(f"{ti:6.2f}  {Ti:8.3f}")