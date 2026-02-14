clc;
clear;
close all;

%% پارامترهای سیستم (از مدل خطی شده)
K = 1;        % بهره سیستم
tau = 15.86;  % ثابت زمانی

%% تابع تبدیل
num = K;
den = [tau 1];

G = tf(num, den);

%% نمایش تابع تبدیل
disp('Transfer Function G(s) = ');
G

%% رسم نقشه قطب-صفر
figure;
pzmap(G);
grid on;
title('Pole-Zero Map of the Linearized Tank System');

%% نمایش مقادیر قطب‌ها و صفرها
p = pole(G);
z = zero(G);

disp('Poles = ');
disp(p);

disp('Zeros = ');
disp(z);

%% بررسی پایداری
if all(real(p) < 0)
    disp('System is stable (all poles in Left Half Plane)');
else
    disp('System is NOT stable');
end
