import pandas as pd
import plotly
import numpy as np

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

import csv
from urllib.request import urlopen
import urllib.request

# figures for graphs
from datamodel import df, cases, cases_melted

#make variables for subplots
percent_positive = list(cases.percent_positive)
percent_negative = list(cases.percent_negative)
percent_death = list(cases.percent_death)
percent_hospitalized = list(cases.percent_hospitalized)

negativeIncrease = list(cases.negativeIncrease)
positiveIncrease = list(cases.positiveIncrease)
deathIncrease = list(cases.deathIncrease)
hospitalizedIncrease = list(cases.hospitalizedIncrease)

totalTestResultsIncrease = list(cases.totalTestResultsIncrease)
total_cases_pct_change = list(cases.total_cases_pct_change)
positive_pct_change = list(cases.positive_pct_change)
negative_pct_change = list(cases.negative_pct_change)
death_pct_change = list(cases.death_pct_change)
hospitalized_pct_change = list(cases.hospitalized_pct_change)
date = list(cases.date)


percent_positive = list(cases.percent_positive)
percent_negative = list(cases.percent_negative)
date = list(cases.date)

cases_melt = pd.melt(cases, id_vars=['date'], value_vars=['negativeIncrease'
                                                              ,'positiveIncrease'
                                                              ,'totalTestResultsIncrease'
                                                             ]
                    )
fig0 = px.bar(df
             ,x="date"
             ,y="totalTestResults"
             ,hover_data=['totalTestResults']
             ,title="<b>Total Covid Tests (Cummulative)</b>")

# Add figure title
fig0.update_layout(
    template='plotly_dark'
)
# fig0.show()

fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1 = px.line(cases_melt, x='date', y='value', color='variable')

# Add traces
fig1.add_trace(
    go.Scatter(x=date, y=percent_negative, name="percent_negative"),
    secondary_y=False,
)

fig1.add_trace(
    go.Scatter(x=date, y=percent_positive, name="percent_positive"),
    secondary_y=False,
)

# Add fig2ure title
fig1.update_layout(
    title_text="<b>Daily Covid Cases with Percent Changes</b>"
    ,template='plotly_dark'
)

# Set x-axis title
fig1.update_xaxes(title_text="<b>Date</b>")

# Set y-axes titles
fig1.update_yaxes(title_text="<b>Count</b>", secondary_y=False)
# fig1.show()

print('graphs generated.......')