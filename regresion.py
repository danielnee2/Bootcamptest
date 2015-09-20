# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:23:27 2015

@author: niyuli
"""

# The workhorses
import numpy as np
#import pandas as pd

# We'll use scipy.optimize.curve_fit to do the nonlinear regression
import scipy.optimize

# Plotting modules
import matplotlib.pyplot as plt

# Seaborn makes plots pretty!
import seaborn as sns
sns.set()

plt.close('all')

df = pd.read_csv('bcd_gradient.csv', comment='#')
df.columns = ['x', 'I_bcd'] # rename the columns

#plt.plot(df.x, df.I_bcd, marker= '.', markersize =10, linestyle='')

def bcd_grad(x,log_a,log_b, log_lam):
    'fir func for bcd'
    a,b, lam =  np.exp(np.array([log_a, log_b, log_lam]))
    return a * np.exp(-x/ lam) +b
p0 = np.log(np.array([1,0.2,0.25]))    
log_p, _ = scipy.optimize.curve_fit(bcd_grad, df.x, df.I_bcd, p0 =p0)    

#make smoorht curve to plot
x_smooth = np.linspace(0,1,200)
y_smooth = bcd_grad(x_smooth, *tuple(log_p))
plt.plot(x_smooth, y_smooth, marker= '.', markersize=10, linestyle='')

plt.plot(df.x, df.I_bcd, marker= '.', markersize=10, linestyle='')

plt.draw()
plt.show()


