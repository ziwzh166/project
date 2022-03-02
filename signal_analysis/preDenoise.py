# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:23:16 2022

@author: zhao
"""
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

class PreDenoise:
    def __init__(self,x,t,Fs):
        self.x = x
        self.t = t
        self.Fs = Fs
    def stftDenoise(self):
        #stft
        f, t, Zxx = signal.stft(self.x, self.Fs)
        plt.figure()
        #plot Stft graph
        # Define two plots
        
        #color bar
        levels = plt.MaxNLocator(nbins=15).tick_values(Zxx.min(), Zxx.max())
        
        #mesh plot
        cmap = 'Spectral'
        plt.pcolormesh(t, f, np.abs(Zxx),cmap = cmap, shading='gouraud')
        plt.ylim([f[1], f.mean()])
        plt.title('STFT Magnitude')
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.yscale('log')
        plt.show()
        #istft on the bandwith
        bandwith = input("")
        
            
        
    