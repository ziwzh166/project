close all;
clc;
clear all;
%% import the data
raw_data =importdata('Signal.txt');
data1 = raw_data.data;

%Ts = data1(2,1) - data1(1,1);
%% calculate the frequency of original data
diff_all = diff(data1(:,1));
Ts = mode(diff_all);
Fs = 1/Ts;
%% caluclate the amened time domain but incomplete
x = data1(:,2);
ts = data1(:,1) - data1(1,1);

%% Reasampling 
y = resample(x,ts,Fs);

ts2 = (0:(length(y)-1))*Ts;
%% Plot 
figure;
plot(ts(1:end-15),x(1:end-15)); hold on;
plot(ts2(1:end-15),y(1:end-15));
legend('raw data','resampled');

data = y(1:end-15);
%% save file
save('resampled_low_noise_data.mat','data','Fs');

