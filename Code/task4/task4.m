0
clc
clear
close all

%% پارامترها
A = 1;
a = 0.5;
g = 9.81;
h0 = 1;

alpha = (a*sqrt(2*g))/(2*A*sqrt(h0));
beta  = 1/A;

G = tf(beta,[1 alpha]);

%% نمودار بود
figure
margin(G)   % هم Bode میده هم Gain/Phase Margin
grid on
title('Bode Diagram of Linearized Tank System')

%% استخراج عددی حاشیه‌ها
[GM,PM,Wcg,Wcp] = margin(G);

fprintf('Gain Margin = %.2f dB\n',20*log10(GM));
fprintf('Phase Margin = %.2f deg\n',PM);
fprintf('Gain crossover freq = %.2f rad/s\n',Wcg);
fprintf('Phase crossover freq = %.2f rad/s\n',Wcp);
figure
nyquist(G)
grid on
title('Nyquist Diagram of Linearized Tank System')
