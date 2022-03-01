# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:51:07 2022

@author: zhao
"""


import numpy as np
import scipy.io
import matplotlib.pyplot as plt
class Resample:
    #import signal from matlab 
    def __init__(self,filename):
        self.filename = filename
    
    def resampleSignal(self):        
        # import signal from matlab, the scipy resample function doesn't cannot perform 
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
        mat = scipy.io.loadmat('resampled_low_noise_data.mat')
        t =np.arange(len(mat['data']))*(1/mat['Fs'])
        t = t.T
        signal = np.array(mat['data'])
        Fs = np.array(mat['Fs'])
        return signal,t,Fs
        
    def PlotSignal(self):
        fig1,ax1 = plt.plot()
        plt.plot(self.t,self.signal)
        plt.set_xlabel('Time/s')
        plt.set_ylabel('Current/PA')
        plt.set_title('Raw data')