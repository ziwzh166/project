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
        # import signal from matlab, the scipy resample function cannot perform 
        # in the case when there is only incomplete time domain and frequency rate
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
        mat = scipy.io.loadmat(self.filename)
        t =np.arange(len(mat['data']))*(1/mat['Fs'])
        t = t.T
        signal = np.array(mat['data'])
        Fs = np.array(mat['Fs']).reshape(1,)
        Fs = Fs[0]
        signal = signal[:,0]
        t = t[:,0]
        return signal,t,Fs
        
    def PlotSignal(self):
        signal,t,_ = self.resampleSignal()
        plt.plot(dpi = 600)
        plt.plot(t,signal)
        plt.xlabel('Time/s')
        plt.ylabel('Current/PA')
        plt.title('Raw data')