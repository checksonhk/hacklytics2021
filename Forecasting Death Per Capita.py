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

#import the data

df = pd.read_csv("all-states-history.csv")
df = df.sort_values('date')

party_map2 = {'AK' : 'red','AL' : 'red','AR' : 'red','AZ' : 'red', 
             'CA' : 'blue','CO' : 'blue','CT' : 'blue', 
             'DC' : 'blue','DE' : 'blue','FL' : 'red',
             'GA' : 'red', 'HI' : 'blue', 'IA' : 'red', 
             'ID' : 'red','IL' : 'blue', 'IN' : 'red',
             'KS' : 'blue', 'KY' : 'blue', 'LA' : 'blue', 
             'MA' : 'red', 'MD' : 'red','ME' : 'blue', 
             'MI' : 'blue', 'MN' : 'blue', 'MO' : 'red', 
             'MS' : 'red','MT' : 'red', 'NC' : 'blue', 
             'ND' : 'red', 'NE' : 'red','NH' : 'red', 
             'NJ' : 'blue', 'NM' : 'blue', 'NV' : 'blue', 
             'NY' : 'blue','OH' : 'red', 'OK' : 'red', 
             'OR' : 'blue','PA' : 'blue', 
             'RI' : 'blue','SC' : 'red', 'SD' : 'red', 
             'TN' : 'red', 'TX' : 'red', 'UT' : 'red',
             'VA' : 'blue','VT' : 'red', 'WA' : 'blue', 
             'WI' : 'blue', 'WV' : 'red', 'WY' : 'red'}

for k,v in party_map2.items():
    if v == 'red':
        party_map2[k] = 'tab:red'
    elif v == 'blue':
        party_map2[k] = 'tab:blue'
        
df['party'] = df['state'].map(party_map2)
df = df.dropna(subset=['party'])

#add demographic data to merge in population
dem = pd.read_csv('states_demographics.txt', header = 1)
relcols = ['Geographic Area Name', 'Estimate!!SEX AND AGE!!Total population']
dem = dem[relcols]
dem = dem.rename(columns={'Estimate!!SEX AND AGE!!Total population':'population'})

statecode_map = {'Alaska' : 'AK','Alabama' : 'AL','Arkansas' : 'AK','Arizona' : 'AZ', 
             'California' : 'CA','Colorado' : 'CO','Connecticut' : 'CT', 
             'Washington DC' : 'DC','Delaware' : 'DE','Florida' : 'FL',
             'Georgia' : 'GA', 'Hawaii' : 'HI', 'Iowa' : 'IA', 
             'Idaho' : 'ID','Illinois' : 'IL', 'Indiana' : 'IN',
             'Kansas' : 'KA', 'Kentucky' : 'KY', 'Louisiana' : 'LA', 
             'Massachusetts' : 'MA', 'Maryland' : 'MD','Maine' : 'ME', 
             'Michigan' : 'MI', 'Minnesota' : 'MN', 'Missouri' : 'MO', 
             'Mississippi' : 'MS','Montana' : 'MT', 'North Carolina' : 'NC', 
             'North Dakota' : 'ND', 'Nebraska' : 'NE','New Hampshire' : 'NH', 
             'New Jersey' : 'NJ', 'New Mexico' : 'NM', 'Nevada' : 'NV', 
             'New York' : 'NY','Ohio' : 'OH', 'Oklahoma' : 'OK', 
             'Oregon' : 'OR','Pennsylvania' : 'PA', 
             'Rhode Island' : 'RI','South Carolina' : 'SC', 'South Dakota' : 'SD', 
             'Tennessee' : 'TN', 'Texas' : 'TX', 'Utah' : 'UT',
             'Virginia' : 'VA','Vermont' : 'VT', 'Washington' : 'WA', 
             'Wisconsin' : 'WI', 'West Virginia' : 'WV', 'Wyoming' : 'WY'}

dem['code'] = dem['Geographic Area Name'].map(statecode_map)
dem = dem.dropna()

df2 = pd.merge(df, dem, left_on='state', right_on='code').drop(columns=['Geographic Area Name', 'code'])
df2 = df2.dropna(subset=['death'])
df2['death_per_cap'] = ( df2['death'] / df2['population'] ) * 100

def plot_deaths_per_cap(state):
    data = df2[df2['state'] == state]
    var = 'death_per_cap'
    col = data['party']
    data.plot(x='date', y=var, style='.',
          kind = 'line',
          legend = False, 
          title = state + "'s Death per Capita", 
          color = col,
          figsize = (12,6))
    plt.show()
    
    
# choose state on click and run plot_deaths_per_cap(state)

