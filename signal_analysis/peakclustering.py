# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:14:26 2022

@author: zhao
"""

import numpy as np
import scipy.signal as signal
from scipy.ndimage import gaussian_filter1d
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
import matplotlib.cm as cm

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
        return peaks,peak_properties,x_smoothed,x_offset
    
    def ClusteringPeaks(self):
        #define features
        peaks,peak_properties,_,_ = self.FindPeaks()
        peak_height = peak_properties['peak_heights']
        peak_width = peak_properties['widths']
        peaks_feature = np.zeros((len(peak_height),2))
        peaks_feature[:,0] = peak_height
        peaks_feature[:,1] = peak_width
        #plot the distribution 
        Plot_peaks_b = input("If you want to see the distribution of peaks Y/n: ")
        if Plot_peaks_b == 'Y' or Plot_peaks_b == 'y':
            plt.plot(dpi = 600)
            plt.scatter(peaks_feature[:,0],peaks_feature[:,1],label = "undefined signal")
            plt.xlabel( 'Peak height')
            plt.ylabel ('peak width')
            plt.legend()
            plt.show()
        #elbow curve define the clusters 
        intertia = []
        K = range(1,15)
        for k in K:
            km = KMeans(n_clusters=k)
            km = km.fit(peaks_feature)
            intertia.append(km.inertia_)
        #plot 15 iterations of clustering interia
        plt.plot(K, intertia, marker= "x")
        plt.xlabel('k')
        plt.xticks(np.arange(15))
        plt.ylabel('Intertia')
        plt.title('Elbow Curve')
        plt.show()
        #define the clustering numbers according to the curve
        cluster_num = input('Input at which cluster numbers according to the curve: ')
        if cluster_num == '':
            cluster_num = 5
        km = KMeans(n_clusters = cluster_num, n_init = cluster_num, 
                    init = "random", random_state = 50)
        km.fit(peaks_feature)
        Cluster_pred = km.predict(peaks_feature)
        colors = cm.rainbow(np.linspace(0, 1, cluster_num))
        
        #plot the cluster distribution
        plt.plot(dpi = 600)
        for (i,color) in zip(range(cluster_num),colors):
            m = np.where(Cluster_pred == i)
            plt.scatter(peaks_feature[:,0][m],peaks_feature[:,1][m],
                        label = i, color = color)
        plt.xlabel( 'Peak height')
        plt.ylabel ('peak width')
        plt.legend()
        plt.show()
        #plot the original peaks on the signal plot
        #need to be debugged
        plt.plot(dpi = 600)
        plt.plot(self.t,self.x,label = "signal")
        for (i,color) in zip(range(cluster_num),colors):
            m = np.where(Cluster_pred == i)
            plt.scatter(self.t[peaks[m]], self.x[peaks[m]], "x",
                        label = 'peaks'+''+str(i), color = color)
        plt.xlabel( 'Peak height')
        plt.ylabel ('peak width')
        plt.legend()
        plt.show()
        
        
        
        
        
        
        
                        
            
            
        
            
        
            
        
        
        
        
        
        
        
        
