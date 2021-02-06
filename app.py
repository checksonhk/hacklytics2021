# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly
import numpy as np
# import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import csv
from urllib.request import urlopen
import urllib.request

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

url = "https://covidtracking.com/api/v1/us/daily.csv"
df = pd.read_csv(url)

#make new date column
df['year'] = df.date.astype(str).str[:4]
df['month_day'] = df.date.astype(str).str[-4:]
df['day'] = df.date.astype(str).str[-2:]
df['month'] = df.month_day.astype(str).str[:2]
df['date_new'] = df['year'] + "-" + df['month'] + "-" + df['day']



df['date_new'] = df['date_new'].astype('datetime64')
df.dtypes

# create new df for test result
cases = df[['date_new', 'totalTestResultsIncrease', 'negativeIncrease', 'positiveIncrease', 'deathIncrease', 'hospitalizedIncrease']]
# cases.head(20).style.background_gradient(cmap='Pastel1')


#create percent columns
cases['percent_positive'] = cases['positiveIncrease']/cases['totalTestResultsIncrease']
cases['percent_negative'] = cases['negativeIncrease']/cases['totalTestResultsIncrease']
cases['percent_death'] = cases['deathIncrease']/cases['totalTestResultsIncrease']
cases['percent_hospitalized'] = cases['hospitalizedIncrease']/cases['totalTestResultsIncrease']
# cases.head(20)


# create percentage change columns for cases.df
cases['positive_pct_change'] = cases['percent_positive'].pct_change()
cases['negative_pct_change'] = cases['percent_negative'].pct_change()
cases['total_cases_pct_change'] = cases['totalTestResultsIncrease'].pct_change()
cases['death_pct_change'] = cases['percent_death'].pct_change()
cases['hospitalized_pct_change'] = cases['percent_hospitalized'].pct_change()
cases


# filter out old dates
cases = cases[cases['date_new'] > '2020-03-20']
# cases.head(20).style.background_gradient(cmap="Blues")

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
date = list(cases.date_new)

# melt daily percent change columns into one dataframe
positive_pct_melt = pd.melt(cases, id_vars=['date_new'],value_vars=['positive_pct_change'])
negative_pct_melt = pd.melt(cases, id_vars=['date_new'],value_vars=['negative_pct_change'])
death_pct_melt = pd.melt(cases, id_vars=['date_new'],value_vars=['death_pct_change'])
hospitalized_pct_melt = pd.melt(cases, id_vars=['date_new'],value_vars=['hospitalized_pct_change'])
total_cases_pct_melt = pd.melt(cases, id_vars=['date_new'],value_vars=['total_cases_pct_change'])


cases_melted1 = positive_pct_melt.append(negative_pct_melt,ignore_index=True)
cases_melted2 = cases_melted1.append(death_pct_melt,ignore_index=True)
cases_melted3 = cases_melted2.append(hospitalized_pct_melt,ignore_index=True)
cases_melted = cases_melted3.append(total_cases_pct_melt,ignore_index=True)
cases_melted.head()
cases_melted.variable.value_counts()




app.layout = html.Div([
        html.H2("Dataframe"),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns],
            data=df.to_dict('records'),
            style_cell = {
                    'font-family': 'sans-serif',
                    'font-size': '14px',
                    'text-align': 'center'
                },
            editable=True,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_selectable="multi",
            row_deletable=True,
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 10,
            style_table={'overflowX': 'scroll'}
            )
        ],style={'padding-left': '2%', 'padding-right': '2%'})





if __name__ == '__main__':
    app.run_server(debug=True)