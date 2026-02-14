import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ===== پارامترهای فیزیکی =====
A = 1.0      # سطح مقطع تانک
a = 0.5      # ضریب خروجی
g = 9.81     # گرانش

# ===== شرایط مسئله =====
h0 = 2.0
h_ref = 10.0

# ===== کنترلر P =====
Kp = 15.0

# ===== محدودیت شیر =====
q_min = 0.0
q_max = 100.0

# ===== معادله دینامیکی =====
def tank_dynamics(t, h):

    error = h_ref - h[0]
    q = Kp * error

    # اعمال اشباع شیر
    q = np.clip(q, q_min, q_max)

    dhdt = (1/A) * (q - a * np.sqrt(2*g*max(h[0],0)))
    return [dhdt]

# ===== حل ODE =====
t_span = (0, 20)
t_eval = np.linspace(0, 20, 500)

sol = solve_ivp(tank_dynamics, t_span, [h0], t_eval=t_eval)

t = sol.t
h = sol.y[0]

# ===== سیگنال کنترلی =====
q = np.clip(Kp*(h_ref - h), q_min, q_max)

# ===== محاسبه Overshoot =====
h_max = np.max(h)
OS = (h_max - h_ref) / h_ref * 100

# ===== Settling Time (2%) =====
upper = 1.02 * h_ref
lower = 0.98 * h_ref

within_band = np.where((h >= lower) & (h <= upper))[0]

if len(within_band) > 0:
    Ts = t[within_band[-1]]
else:
    Ts = np.nan

print(f"Overshoot = {OS:.2f} %")
print(f"Settling Time = {Ts:.2f} s")

# ===== رسم نمودار =====
plt.figure(figsize=(8,6))

plt.subplot(2,1,1)
plt.plot(t, h, linewidth=2)
plt.axhline(h_ref, linestyle='--')
plt.title("Nonlinear Tank Response with P Controller")
plt.ylabel("Height (m)")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(t, q, linewidth=2)
plt.title("Control Signal with Saturation")
plt.xlabel("Time (s)")
plt.ylabel("Valve Input (%)")
plt.grid(True)

plt.tight_layout()
plt.show()
