import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ===============================
# پارامترهای تانک
# ===============================
A = 1.0
a = 0.5

# ===============================
# ضرایب PID طراحی‌شده
# ===============================
Kp = 3.04
Ki = 6.0
Kd = 0.5

# ===============================
# شرایط مسئله
# ===============================
h_ref = 10.0
h0 = 2.0

q_min = 0
q_max = 100

# متغیرهای PID
integral_error = 0
prev_error = 0

# ===============================
# مدل غیرخطی + PID
# ===============================
def tank_PID(t, h):

    global integral_error, prev_error

    e = h_ref - h[0]

    # انتگرال خطا
    integral_error += e * dt

    # مشتق خطا
    de_dt = (e - prev_error) / dt
    prev_error = e

    # قانون PID
    q_in = Kp*e + Ki*integral_error + Kd*de_dt

    # محدودیت شیر
    q_in = np.clip(q_in, q_min, q_max)

    # معادله دینامیکی تانک
    dhdt = (q_in - a*np.sqrt(max(h[0],0))) / A

    return [dhdt]

# ===============================
# شبیه سازی
# ===============================
t_span = (0, 10)
t_eval = np.linspace(0, 10, 500)
dt = t_eval[1] - t_eval[0]

sol = solve_ivp(tank_PID, t_span, [h0], t_eval=t_eval)

# ===============================
# سیگنال کنترلی
# ===============================
integral_error = 0
prev_error = 0
q_values = []

for h in sol.y[0]:

    e = h_ref - h
    integral_error += e * dt
    de_dt = (e - prev_error) / dt
    prev_error = e

    q = Kp*e + Ki*integral_error + Kd*de_dt
    q = np.clip(q, q_min, q_max)

    q_values.append(q)

# ===============================
# رسم نتایج
# ===============================
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(sol.t, sol.y[0], label='Height')
plt.axhline(h_ref, linestyle='--', label='Reference')
plt.title("Tank Level — PID Controller")
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
