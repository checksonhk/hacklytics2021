# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly
import numpy as np

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/python-visualization/folium/master/tests/us-states.json') as response:
  map_states = json.load(response)

# import csv
# from urllib.request import urlopen
# import urllib.request
from helpers import format_us_state, format_card_header, format_number

from datamodel import df, cases


bgcolors = {
    'background': '#13263a',
    'text': '#FFFFFF'
}

# ------------------------------
# external JavaScript files
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    },
]

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    },
    {
        'href': 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf',
        'crossorigin': 'anonymous'
    },
    dbc.themes.DARKLY
]

# -------------------------------------------------------------------------------
# app stuff
app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)


# -------------------------------------------------------------
# run app layout things
# import required figures
available_selectors = list(cases.columns)[1:]
available_states = df['state'].unique()


def generate_icon(icon_name):
  return html.Span(
      style=({'width': '5rem', 'height': '5rem'}),
      children=html.I(className=f"{icon_name} fa-3x"))


cards = [("new-cases", "fas fa-globe-americas"), ("new-deaths", 'fas fa-skull-crossbones'),
         ("new-hospitalized", "fas fa-procedures"), ("total-recovered", "fas fa-heartbeat")]


def generate_card(header, icon):
  return dbc.Card(
      [
          dbc.CardBody(
              [html.Div(className='row',
                        children=[
                            html.Div(className='col', children=[html.H5(format_card_header(header), className='card-title text-nowrap'),
                                                                html.H2(className="card-stats",
                                                                        id=f"{header}-data")]),
                            html.Div(html.P(generate_icon(icon)),
                                     className='col auto')
                        ])
               ]
          )
      ],
      style=({"border-radius": '1rem'}),
  )


state_selection = html.Div(className='d-flex justify-content-between mb-2', children=[
    html.Label(html.H3("Selected State"), style={"font-weight": "bold"}),
    dcc.Dropdown(
        id='state-selection',
        options=[{'label': format_us_state(
            i), 'value': i} for i in available_states],
        value='AK')
])

y_axis_selection = html.Div(className='d-flex', children=[
    dcc.Dropdown(
        id='figure1-yaxis-column',
        options=[{'label': i, 'value': i}
                 for i in available_selectors],
        value='totalTestResultsIncrease')
])

date_picker = html.Div(className='d-flex justify-content-between mb-2', children=[
    html.Label(html.H3("Date Range"), style={"font-weight": "bold"}),
    dcc.DatePickerRange(
        id='figure1-xaxis--datepicker',
        min_date_allowed=min(df['date']),
        max_date_allowed=max(df['date']),
        initial_visible_month=max(df['date']),
        start_date=min(df['date']),
        end_date=max(df['date'])
    )])

app.layout = html.Div(className='p-5', children=[
    html.H1(children='A Deeper Look into the Analytics of Covid-19'),
    html.Br(),
    html.Div(children='''
        The purpose of this page is to provide a more in-depth analysis of \
        the Covid-19 outbreak. The charts on this page offer a range of \
        analytical views. From daily percent changes and trends for each \
        day of the week, to the slope and moving averages for each outcome.\
        '''),
    html.Div(
        className='row align-items-baseline',
        children=[html.Div(className='col-sm-5', children=[html.Div(className='filters d-flex flex-column', children=[state_selection, date_picker])]),
                  html.Div(className='col-sm-7', children=[html.Div(className='d-flex justify-content-around my-4',
                                                                    children=[generate_card(header, icon) for header, icon in cards])]),

                  ]),
    html.Div(
        className='row',
        children=[
            # LEFT SIDE
            html.Div(
                className='col-sm-9',
                children=[dcc.Graph(id="map")]
            ),
            # RIGHT SIDE
            html.Div(
                className='col-sm-3 d-flex flex-column pt-3',
                children=[]
            )]
    ),
    html.Br(),

    html.Div(children='''
        The data used for this analysis comes from Our World in Data \
        "https://covidtracking.com/api/v1/us/daily.csv". A more detailed \
        description of the data can be found here:
        https://ourworldindata.org/coronavirus-data
        '''), html.Br(),

    html.Div(children='''
        The charts below provide analysis for the United States.
        '''), html.Br(),

    html.Div([
        html.Div([
            y_axis_selection,
            html.H2("Figure 1"),
            dcc.Graph(id='figure1-bar')
        ], className="six columns", style={'padding-left': '5%', 'padding-right': '5%'}), html.Br(),

        html.Div([
            html.H2("Figure 2"),
            dcc.Checklist(id="label-select", options=[
                {'label': 'Negative Increase', 'value': 'negativeIncrease'},
                {'label': 'Positive Increase', 'value': 'positiveIncrease'},
                {'label': 'Total Test Results Increase',
                 'value': 'totalTestResultsIncrease'},
                {'label': 'Percent Negative', 'value': 'percent_negative'},
                {'label': 'Percent Positive', 'value': 'percent_positive'},
            ], value=['negativeIncrease', 'positiveIncrease', 'totalTestResultsIncrease', 'percent_negative', 'percent_positive']),
            dcc.Graph(id="selectable-labels"),
        ], className="six columns", style={'padding-left': '5%', 'padding-right': '5%'})

    ], className="row"),

])


@ app.callback(
    Output(component_id='new-cases-data', component_property='children'),
    Input("state-selection", 'value'),
    Input('figure1-xaxis--datepicker',  component_property='start_date'),
    Input('figure1-xaxis--datepicker',  component_property='end_date')
)
def update_new_cases(state, start_date, end_date):
  dfff = df[(df['state'] == state) & (
      df['date'] > start_date) & (df['date'] < end_date)]
  new_cases = dfff['positiveIncrease'].sum()

  return format_number(new_cases)


@ app.callback(
    Output(component_id='new-deaths-data', component_property='children'),
    Input("state-selection", 'value'),
    Input('figure1-xaxis--datepicker',  component_property='start_date'),
    Input('figure1-xaxis--datepicker',  component_property='end_date')
)
def update_new_deaths(state, start_date, end_date):
  dfff = df[(df['state'] == state) & (
      df['date'] > start_date) & (df['date'] < end_date)]
  new_cases = dfff['deathIncrease'].sum()

  return format_number(new_cases)


@ app.callback(
    Output(component_id='new-hospitalized-data',
           component_property='children'),
    Input("state-selection", 'value'),
    Input('figure1-xaxis--datepicker',  component_property='start_date'),
    Input('figure1-xaxis--datepicker',  component_property='end_date')
)
def update_total_test_results(state, start_date, end_date):
  dfff = df[(df['state'] == state) & (
      df['date'] > start_date) & (df['date'] < end_date)]
  new_cases = dfff['hospitalizedIncrease'].sum()

  return format_number(new_cases)


@ app.callback(
    Output(component_id='total-recovered-data',
           component_property='children'),
    Input("state-selection", 'value'),
    Input('figure1-xaxis--datepicker',  component_property='start_date'),
    Input('figure1-xaxis--datepicker',  component_property='end_date')
)
def update_total_recovered(state, start_date, end_date):
  dfff = df[(df['state'] == state) & (df['date'] == end_date)]
  total_recovered = dfff['recovered']

  return format_number(int(total_recovered))


@ app.callback(
    Output('figure1-bar', 'figure'),
    [
        Input("state-selection", 'value'),
        Input('figure1-yaxis-column', 'value'),
        Input('figure1-xaxis--datepicker',  component_property='start_date'),
        Input('figure1-xaxis--datepicker',  component_property='end_date')
    ])
def update_graph(state, yaxis_column_name, start_date, end_date):
  dff = df[df['state'] == state]
  dfff = dff[(df['date'] > start_date) & (df['date'] < end_date)]
  fig = px.bar(dfff, x="date", y=yaxis_column_name, hover_data=[
      'totalTestResults'], title="<b>Total Covid Tests (Cummulative)</b>")

  fig.update_layout(
      template='plotly_dark'
  )
  return fig


@ app.callback(Output('state-selection', 'value'),
               Input('map', 'clickData'))
def update_state(clickData):
  return clickData['points'][0]['location']


@ app.callback(
    Output('selectable-labels', 'figure'),
    [Input('label-select', 'value')]
)
def update_graph(value):

  fig_test = make_subplots(specs=[[{"secondary_y": True}]])
  possible_vals = ['negativeIncrease', 'positiveIncrease',
                   'totalTestResultsIncrease', 'percent_negative', 'percent_positive']
  for val in possible_vals:
    if val in value:
      visibility = True
    else:
      visibility = "legendonly"
    fig_test.add_trace(go.Scatter(
        x=cases['date'], y=cases[val], name=val, visible=visibility), )

  fig_test.update_layout(
      title_text="<b>Daily Covid Cases with Percent Changes</b>", template='plotly_dark'
  )

  # Set x-axis title
  fig_test.update_xaxes(title_text="<b>Date</b>")

  return fig_test


@ app.callback(
    Output("map", "figure"),
    [
        Input('figure1-xaxis--datepicker',  component_property='start_date'),
        Input('figure1-xaxis--datepicker',  component_property='end_date')
    ])
def display_map(start_date, end_date):
  map_select = df[(df['date'] > start_date) & (df['date'] < end_date)]
  map_selected_sum = map_select.groupby(
      ["state"]).positiveIncrease.sum().reset_index()
  fig_map = px.choropleth_mapbox(map_selected_sum, geojson=map_states, locations=map_selected_sum['state'], color='positiveIncrease',
                                 color_continuous_scale="reds",
                                 mapbox_style="carto-positron",
                                 zoom=3, center={"lat": 39.0902, "lon": -99},
                                 opacity=0.5,
                                 labels={'positiveIncrease': 'Positive Cases'}
                                 )
  fig_map.update_layout(
      margin={"r": 0, "t": 0, "l": 0, "b": 0}
  )

  return fig_map


if __name__ == '__main__':
  app.run_server(debug=True, port='4000')
