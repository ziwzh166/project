# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:14:26 2022

@author: zzw
"""

import numpy as np
import scipy.signal as signal
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt 

class PeakClustering():
    def __init__(self,x,t,Fs):
        self.x = x
        self.t = t
        self.Fs = Fs
        
    def FindPeaks(self):
        #generate a super smoothed data as trend line
        x_smoothed = gaussian_filter1d(self.x,500)
        # offest the trend
        x_offset = self.x - x_smoothed
        x_offset_r = - x_offset
        #change the height and width to filter more, here try to gain all the peaks
        peaks, peak_properties = signal.find_peaks(x_offset_r,
                                          height = np.array([0.3, 1.5]),
                                          width = 0)
        # width_peak = signal.peak_widths(x_offset_r, peaks, rel_height=1)
        Plot_peaks = input("If you want to see the curve with found peaks Y/n: ")
        if Plot_peaks == 'Y' or Plot_peaks == 'y':
            plt.plot(dpi = 600)
            plt.plot(self.t,self.x,label = "signal")
            plt.scatter(self.t[peaks], self.x[peaks], "x", label = 'peaks')
            plt.xlabel( 'Time [sec]')
            plt.ylabel ('Current [PA]')
            plt.legend()
            plt.show()
        return peaks,peak_properties
    
    def ClusteringPeaks(self):
        pass
        
        
        
