clc
clear
close all

%% -------------------------
% پارامترهای فیزیکی سیستم
%% -------------------------
A_tank = 1;          % سطح مقطع مخزن
Cd = 0.5;            % ضریب تخلیه
h_eq = 0.04;         % نقطه کار

% دبی تعادل
qin_eq = Cd*sqrt(h_eq);

tspan = [0 2000];

%% =====================================================
% پاسخ ضربه (تقریب ضربه با پالس باریک)
%% =====================================================

amp = 5;          % دامنه بزرگ
width = 1;        % عرض بسیار کوچک → تقریب ضربه

qin_impulse = @(t) qin_eq + amp*(t<=width);

f_impulse = @(t,h) (1/A_tank)*( qin_impulse(t) - Cd*sqrt(max(h,0)) );

[t_imp, h_imp] = ode45(f_impulse, tspan, h_eq);

figure
plot(t_imp,h_imp,'r','LineWidth',2)
grid on
title('Nonlinear Impulse Response (Physical Model)')
xlabel('Time (s)')
ylabel('Tank Height (m)')


%% =====================================================
% پاسخ رمپ
%% =====================================================

ramp_slope = 0.00005;   % شیب کوچک برای جلوگیری از سرریز

qin_ramp = @(t) qin_eq + ramp_slope*t;

f_ramp = @(t,h) (1/A_tank)*( qin_ramp(t) - Cd*sqrt(max(h,0)) );

[t_ramp, h_ramp] = ode45(f_ramp, tspan, h_eq);

figure
plot(t_ramp,h_ramp,'b','LineWidth',2)
grid on
title('Nonlinear Ramp Response (Physical Model)')
xlabel('Time (s)')
ylabel('Tank Height (m)')
