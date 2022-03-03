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
        #plot the meshgraph for stft
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
                       
        # istft filter the signal by power
        # initially i would like filter by frequency 
        # but the istft seems not offer the aruguments in scipy
        power_high = input("the high boundary power to perform istft,defaulted 15: ")
        if power_high == '':
            power_high = 15
        power_high = float(power_high)
        Zxx = np.where(Zxx <= power_high, Zxx, 0)
        t_stft, xrec_stft = signal.istft(Zxx, fs = self.Fs)
        #cancel the shift caused by istft
        t_stft = t_stft[:-1-150]
        xrec_stft = xrec_stft[:-1-150] 
        
        Plot_stft = input("If you want to see the denoised plot Y/n: ")
        if Plot_stft == 'Y' or Plot_stft == 'y':
            fig, (axs1,axs2) = plt.subplots(2,sharex=True,dpi=600)
            fig.suptitle('Plots for resampled signal with stft filtered')
            axs1.plot(self.t,self.x)
            plt.set_xlabel='Time [sec]'
            plt.set_ylabel='Current [PA]'
            axs2.plot(t_stft,xrec_stft)
            plt.set_xlabel='Time [sec]'
            plt.set_ylabel='Current [PA]'
            fig.tight_layout()
            plt.show()
        return t_stft,xrec_stft 

    def swtDenoise(self):
        #select the mother wave 
        wave = input('input the name mother wave to decompose, eg.db1,default sym4: ')
        if wave == '':
            wave = 'sym4'
        level = input('input the level for composation, a scala: ')
        if level == "":
            level = 3
        #even value for inputing in swt
        if len(self.x%2) != 0:
            #without putting -1 cannot output the array
            x1 = self.x[:-1-len(self.x)%2+1]
        else:
            x1 = self.x
            
        #swt Denoise somehow the level cannot be input directly over 2 have to write in the loop
        x_D = np.zeros((len(x1),level))
        x_A = np.zeros((len(x1),level))
        for i in range(level):
            coff = pywt.swt(x1, wave)
            x1 = coff[0][0]
            x_D[:,i] = coff[0][1]
            x_A[:,i] = coff[0][0]
        #cancel the error caused by swt
        x_A = x_A[:-1-150,:]
        if len(x1) != len(self.t):
            t1 = self.t[:len(x_A)]
        else:
            t1 = self.t
        Plot_swt = input("If you want to see the denoised plot Y/n: ")
        if Plot_swt == 'Y' or Plot_swt == 'y':
            fig, axs = plt.subplots(level, sharex=True,dpi=600)
            for i in range (level):
                axs[i].plot(t1, x_A[:,i])
            fig.suptitle('Plots for different approximations')
            plt.setp(axs, xlabel='Time [sec]')
            plt.setp(axs, ylabel='Current [PA]')
            fig.tight_layout()
        return t1,x_A,x_D
            
            
                
            
            
           
            
            
        
        
        
        
        
        
            
            
            
        
        
        
        
        
        
            
        
    