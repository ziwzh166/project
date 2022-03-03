# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:51:07 2022

@author: zhao
"""

import signal_analysis as sa
import numpy as np

# Resample, resample function from scipy cannot fit in the case, 
# please run the matlab file resample to import data
x,t,Fs = sa.Resample('resampled_low_noise_data.mat').resampleSignal()
sa.Resample('resampled_low_noise_data.mat').PlotSignal()

#denoise
#denoise use the stft and istft
x1,t1 = sa.PreDenoise(x, t, Fs).stftDenoise()
#denoise use the stationary dwt,swt
t,x_a,_ = sa.PreDenoise(x, t, Fs).swtDenoise()
