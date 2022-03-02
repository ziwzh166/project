# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:51:07 2022

@author: zhao
"""

import signal_analysis as sa
import numpy as np
x,t,Fs = sa.Resample('resampled_low_noise_data.mat').resampleSignal()
