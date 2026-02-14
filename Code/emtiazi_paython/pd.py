import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# -----------------------
# پارامترهای تانک
# -----------------------
A = 1.0
a = 0.5

# -----------------------
# ضرایب PD (طراحی شده)
# -----------------------
Kp = 3.92
Kd = 1.0

# -----------------------
# شرایط مسئله
# -----------------------
h_ref = 10.0
h0 = 2.0

q_min = 0
q_max = 100

prev_error = 0

# -----------------------
# مدل غیرخطی با PD
# -----------------------
def tank_PD(t, h):

    global prev_error

    e = h_ref - h[0]

    de_dt = (e - prev_error) / dt
    prev_error = e

    q_in = Kp * e + Kd * de_dt
    q_in = np.clip(q_in, q_min, q_max)

    dhdt = (q_in - a*np.sqrt(max(h[0],0))) / A

    return [dhdt]

# -----------------------
# شبیه سازی
# -----------------------
t_span = (0, 10)
t_eval = np.linspace(0, 10, 400)
dt = t_eval[1] - t_eval[0]

sol = solve_ivp(tank_PD, t_span, [h0], t_eval=t_eval)

# -----------------------
# سیگنال کنترلی
# -----------------------
prev_error = 0
q_values = []

for h in sol.y[0]:

    e = h_ref - h
    de_dt = (e - prev_error) / dt
    prev_error = e

    q = Kp * e + Kd * de_dt
    q = np.clip(q, q_min, q_max)

    q_values.append(q)

# -----------------------
# رسم
# -----------------------
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(sol.t, sol.y[0], label='h(t)')
plt.axhline(h_ref, linestyle='--', label='Reference')
plt.title("Tank Level — PD Controller")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.legend()
plt.grid()

plt.subplot(1,2,2)
plt.plot(sol.t, q_values)
plt.title("Valve Opening")
plt.xlabel("Time (s)")
plt.ylabel("Valve (%)")
plt.grid()

plt.tight_layout()
plt.show()
