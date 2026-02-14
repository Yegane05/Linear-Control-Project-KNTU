clc
clear
close all

%% ---------------------------
% پارامترهای سیستم
%% ---------------------------

A_tank = 1;      
Cd = 0.5;        
h_eq = 0.04;     
qin_eq = Cd*sqrt(h_eq);  

tspan = [0 1500];

%% ---------------------------
% پله کوچک (در ناحیه خطی)
%% ---------------------------

u_small = 0.01;                 % دامنه کوچک
qin_small = qin_eq + u_small;

f_small = @(t,h) (1/A_tank)*(qin_small - Cd*sqrt(max(h,0)));
[t_small, h_small] = ode45(f_small, tspan, h_eq);

%% ---------------------------
% پله بزرگ (خروج از ناحیه خطی)
%% ---------------------------

u_large = 0.2;                  % دامنه بزرگ
qin_large = qin_eq + u_large;

f_large = @(t,h) (1/A_tank)*(qin_large - Cd*sqrt(max(h,0)));
[t_large, h_large] = ode45(f_large, tspan, h_eq);

%% ---------------------------
% رسم نمودار
%% ---------------------------

figure
hold on
grid on

% رنگ‌ها
red_color = [1 0 0];
indigo_color = [0.29 0 0.51];

plot(t_small, h_small, 'Color', red_color, 'LineWidth', 2)
plot(t_large, h_large, 'Color', indigo_color, 'LineWidth', 2)

xlabel('Time (s)')
ylabel('Tank Height (m)')
title('Nonlinear System Response to Small and Large Step Inputs')

legend('Small Step (Linear Region)','Large Step (Nonlinear Region)')

