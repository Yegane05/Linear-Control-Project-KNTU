clc
clear
close all

%% ضرایب مدل خطی (همان مقادیر قبلی شما)
A = -0.005806;
B = 0.004606;
C = 101.3525;
D = 0;

num = C*B;
den = [1 -A];     % s - A
G = tf(num,den);

%% -------------------------
% پاسخ ضربه
%% -------------------------
figure
impulse(G)
grid on
title('Impulse Response')
xlabel('Time (s)')
ylabel('Amplitude')

%% -------------------------
% پاسخ رمپ
%% -------------------------

t = 0:1:2000;        % بازه زمانی
u_ramp = t;          % رمپ واحد

[y_ramp,t_out] = lsim(G,u_ramp,t);

figure
plot(t_out,y_ramp,'LineWidth',2)
grid on
title('Ramp Response')
xlabel('Time (s)')
ylabel('Output')
