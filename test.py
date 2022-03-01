# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:51:07 2022

@author: zhao
"""
# import signal from matlab, the pandas resample function doesn't cannot perform 
# the case when there is only incomplete time domain and frequency rate
# =============================================================================
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import signal
# #import signal
# signal_read = pd.read_csv('Signal.txt',sep='\t', skiprows = 0)
# 
# #resampling data time domian is not even 
# Index = signal.columns
# sig_ori = signal.loc[:,Index[1]].to_numpy()
# t_ori = signal.loc[:,Index[0]].to_numpy()
# #original smaple rate
# Fs = 1/(np.diff(t_ori).mean())
# # rebuilt time domain
# ts = t_ori - t_ori[0]
# #resample the signal on ts with rate Fs
# signal_rebuilt = signal.resample_poly(sig_ori,ts,Fs )
# 
# =============================================================================
import signal_analysis as sa
import numpy as np
x = sa.Resample('resampled_low_noise_data.mat').resampleSignal()
