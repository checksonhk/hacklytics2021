#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import time
from scipy.optimize import curve_fit

#import data
df = pd.read_csv("all-states-history.csv")
relcols = ['date', 'state', 'deathIncrease', 'positiveIncrease']
df2 = df2[relcols]

#create function that makes predictions based on fitting 4 types of curves to the state's data

# adapted from a notebook on kaggle
# https://www.kaggle.com/malekzadeh/simple-curve-fitting

def plot_and_predict(more_days, state):    
    def avg_err(pcov):
        return np.round(np.sqrt(np.diag(pcov)).mean(), 2)
    
    cmd = df2[df2['state'] == state].copy() 
    cmd_grp = cmd.groupby('date')[['positiveIncrease', 'deathIncrease']].sum().reset_index()
    y = cmd_grp['positiveIncrease']
    x = np.arange(len(y))

    def f_poly(x, a, b, c, d, e):
        return a * x**4 + b*x**3 + c*x**2 + d*x**1 + e

    def f_pow(x, a, b, c):
        return b*(x)**a + c
        
    def f_exp(x, a, b, c):
        return a * np.exp(-b * x) + c
    
    def f_sigmoid(x, a, b, c, d):
        return c / (1 + np.exp(-b*(x-a)))+d

    popt_poly, pcov_poly = curve_fit(f_poly, x, y)
    popt_pow, pcov_pow = curve_fit(f_pow, x, y, maxfev=100000)
    popt_exp, pcov_exp = curve_fit(f_exp, x, y, p0=(1, 1e-6, 1), maxfev=100000)
    popt_sig, pcov_sig = curve_fit(f_sigmoid,x, y, method='dogbox', 
                                   bounds=([10., 0.001, y.mean(), 10],[100, 1., 10*y.mean(), 100]), 
                                   maxfev=200000)

    x_m = np.arange(len(y)+more_days)
    
    y_m = f_poly(x_m, *popt_poly)    
    pred_poly_c = y_m[-more_days:]
    
    y_m = f_exp(x_m, *popt_exp)
    pred_exp_c = y_m[-more_days:]

    y_m = f_pow(x_m, *popt_pow)
    pred_pow_c = y_m[-more_days:]

    # sigmoid curve should be the best, but the bounds need to be chosen correctly
    # https://www.youtube.com/watch?v=Kas0tIxDvrg&feature=youtu.be
    y_m = f_sigmoid(x_m, *popt_sig)
    pred_sig_c = y_m[-more_days:]
    
    # turn prediction arrays into dataframes with date, state, positiveIncrease, deathIncrease
    poly = pd.DataFrame(pred_poly_c, columns = ['positiveIncrease'])
    exp = pd.DataFrame(pred_exp_c, columns = ['positiveIncrease'])
    power = pd.DataFrame(pred_pow_c, columns = ['positiveIncrease'])
    sigmoid = pd.DataFrame(pred_sig_c, columns = ['positiveIncrease'])
    
    dates = [pd.to_datetime(df2['date'].max()) + datetime.timedelta(days=1)]
    states = [state]
    for i in range(1, more_days):
        dates.append(dates[-1] + datetime.timedelta(days=1))
        states.append(state)
    
    poly.insert(0, "date", dates, True)
    exp.insert(0, "date", dates, True)
    power.insert(0, "date", dates, True)
    sigmoid.insert(0, "date", dates, True)
    
    poly.insert(1, "state", states, True)
    exp.insert(1, "state", states, True)
    power.insert(1, "state", states, True)
    sigmoid.insert(1, "state", states, True)
    
    #repeat curve fitting to make death predictions and add to the dataframes
    cmd = df2[df2['state'] == state].copy() 
    cmd_grp = cmd.groupby('date')[['positiveIncrease', 'deathIncrease']].sum().reset_index()
    y = cmd_grp['deathIncrease']
    x = np.arange(len(y))

    popt_poly, pcov_poly = curve_fit(f_poly, x, y)
    popt_pow, pcov_pow = curve_fit(f_pow, x, y, maxfev=100000)
    popt_exp, pcov_exp = curve_fit(f_exp, x, y, p0=(1, 1e-6, 1), maxfev=100000)
    popt_sig, pcov_sig = curve_fit(f_sigmoid,x, y, method='dogbox', 
                                   bounds=([10., 0.001, y.mean(), 10],[100, 1., 10*y.mean(), 100]), 
                                   maxfev=200000)
    
    x_m = np.arange(len(y)+more_days)
    
    y_m = f_poly(x_m, *popt_poly)    
    pred_poly_d = y_m[-more_days:]
    
    y_m = f_exp(x_m, *popt_exp)
    pred_exp_d = y_m[-more_days:]

    y_m = f_pow(x_m, *popt_pow)
    pred_pow_d = y_m[-more_days:]

    y_m = f_sigmoid(x_m, *popt_sig)
    pred_sig_d = y_m[-more_days:]
        
    poly.insert(3, "deathIncrease", pred_poly_d, True)
    exp.insert(3, "deathIncrease", pred_exp_d, True)
    power.insert(3, "deathIncrease", pred_pow_d, True)
    sigmoid.insert(3, "deathIncrease", pred_sig_d, True)
    
    
#on a click
#run plot_and_predict(more_days, state)

