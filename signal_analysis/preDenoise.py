# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:23:16 2022

@author: zhao
"""
import numpy as np
from scipy import signal
import pywt
import matplotlib.pyplot as plt

class PreDenoise:
    def __init__(self,x,t,Fs):
        self.x = x
        self.t = t
        self.Fs = Fs
    def stftDenoise(self):
        #stft
        f, ts, Zxx = signal.stft(self.x, self.Fs)
        #plot session
        Plot_Stft = input("If you want to see the mesh plot Y/n: ")
        if Plot_Stft == 'Y' or Plot_Stft == 'y':
            plt.figure()
            #plot Stft graph                        
            #mesh plot
            cmap = 'Spectral'
            ax1 = plt.pcolormesh(ts, f, np.abs(Zxx),cmap = cmap, shading='gouraud')
            plt.ylim([f[1], f[1]*5])
            plt.title('STFT Magnitude')
            plt.ylabel('Frequency [Hz]')
            plt.xlabel('Time [sec]')
            plt.colorbar(ax1)
            plt.show()
            
        
        #istft on the bandwith, low frequency is the signal
        bandwith_high = input("the high boundary frequency to perform istft: ")
        fs = np.where(f <= bandwith_high, f, 0)
        t_stft, xrec_stft = signal.istft(Zxx, fs)
        #cancel the shift caused by istft
        t_stft = t_stft[:-1-150]
        xrec_stft = xrec_stft[:-1-150] 
        return t_stft,xrec_stft 

    def swtDenoise(self):
        #select the mother wave 
        wave = input('input the name mother wave to decompose, eg.db1: ')
        if wave == '':
            wave = 'sym4'
        level = input('input the level for composation, a scala: ')
        if level == "":
            level = 3
        #even value for inputing in swt
        if len(self.x%2) == 0:
            #directly canoot output the array
            x = self.x[:-1-len(self.x)%2+1]
            
        #swt Denoise somehow the level cannot be input directly over 2 have to write in the loop
        x_D = np.zeros((len(x),level))
        x_A = np.zeros((len(x),level))
        for i in range(level):
            coff = pywt.swt(x, wave)
            x = coff[0][0]
            x_D[:,i] = coff[0][1]
            x_A[:,i] = coff[0][0]
        if len(x) == len(self.t):
            t = self.t[:len(x)]
        Plot_swt = input("If you want to see the denoised plot Y/n: ")
        if Plot_swt == 'Y' or Plot_swt == 'y':
            True
            
            
        
        
        
        
        
        
            
            
            
        
        
        
        
        
        
            
        
    