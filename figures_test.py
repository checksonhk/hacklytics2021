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

# make variables for subplots
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

cases_melt = pd.melt(cases, id_vars=['date'], value_vars=['negativeIncrease', 'positiveIncrease', 'totalTestResultsIncrease'
                                                          ]
                     )

# Create fig2ure with secondary y-axis

fig0 = px.bar(df, x="date", y="totalTestResults", hover_data=[
              'totalTestResults'], title="<b>Total Covid Tests (Cummulative)</b>")

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
    title_text="<b>Daily Covid Cases with Percent Changes</b>", template='plotly_dark'
)

# Set x-axis title
fig1.update_xaxes(title_text="<b>Date</b>")

# Set y-axes titles
fig1.update_yaxes(title_text="<b>Count</b>", secondary_y=False)
# fig2.show()


fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(
    go.Scatter(x=date, y=percent_negative, name="percent_negative",
               marker_color=px.colors.qualitative.Plotly[2]),
    secondary_y=True,
)
fig2.add_trace(
    go.Scatter(x=date, y=percent_positive, name="percent_positive",
               marker_color=px.colors.qualitative.D3[3]),
    secondary_y=True,
)

# Add figure title
fig2.update_layout(
    title_text="<b>Daily Pos/Neg Percent of Covid Tests</b>"
)

# Set x-axis title
fig2.update_xaxes(title_text="<b>Date</b>")

# Set y-axes titles
fig2.update_yaxes(title_text="<b>Percent</b>", secondary_y=True)

# Change the bar mode
fig2.update_layout(barmode='stack')

# Customize aspect
fig2.update_traces(marker_line_width=.01)

# update legend
fig2.update_layout(
    template='plotly_dark', legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
# fig2.show()


fig3 = make_subplots(specs=[[{"secondary_y": True}]])

fig3.add_trace(
    go.Bar(x=date, y=negativeIncrease, name="negativeIncrease",
           marker_color=px.colors.qualitative.Pastel1[3]),
    secondary_y=False,
)
fig3.add_trace(
    go.Bar(x=date, y=positiveIncrease, name="positiveIncrease"),
    secondary_y=False,
)
fig3.add_trace(
    go.Scatter(x=date, y=totalTestResultsIncrease, opacity=.7, name="totalTestResultsIncrease",
               mode="markers", marker_color=px.colors.qualitative.Plotly[3]),
    secondary_y=False,
)

# Add fig3ure title
fig3.update_layout(
    title_text="<b>Daily Pos/Neg and Total Tests</b>"
)

# Set x-axis title
fig3.update_xaxes(title_text="<b>Date</b>")

# Set y-axes titles
fig3.update_yaxes(title_text="<b>Count Cases</b>", secondary_y=False)

# Change the bar mode
fig3.update_layout(barmode='stack')

# Customize aspect
fig3.update_traces(marker_line_width=.01)

# update legend
fig3.update_layout(
    template='plotly_dark', legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
# fig3.show()


# fig4 = make_subplots(specs=[[{"secondary_y": True}]])

# fig4.add_trace(
#     go.Scatter(x=date
#                ,y=positive_pct_change
#                ,name="positive_pct_change"
#                ,mode="lines+markers"
#                ,marker_color=px.colors.qualitative.T10[2]),
#     secondary_y=False,
# )
# fig4.add_trace(
#     go.Scatter(x=date
#                ,y=negative_pct_change
#                ,name="negative_pct_change"
#                ,mode="markers"
#                ,marker_color=px.colors.qualitative.Plotly[5]),
#     secondary_y=True,
# )
# fig4.add_trace(
#     go.Scatter(x=date
#                ,y=total_cases_pct_change
#                ,name="total_cases_pct_change"
#                ,mode="lines+markers"
#                ,marker_color=px.colors.qualitative.Plotly[3]),
#     secondary_y=False,
# )


# # Add fig4ure title
# fig4.update_layout(
#     title_text="<b>Daily Percent Changes of Covid Positive Tests and Total Tests</b>"
# )

# # Set x-axis title
# fig4.update_xaxes(title_text="<b>Date</b>")

# # Set y-axes titles
# fig4.update_yaxes(title_text="<b>Percent Change</b>", secondary_y=False)

# # Change the bar mode
# fig4.update_layout(barmode='stack')

# # Customize aspect
# fig4.update_traces(marker_line_width=.01)

# #update legend
# fig4.update_layout(
#     template='plotly_dark'
#     ,legend=dict(
#     orientation="h",
#     yanchor="bottom",
#     y=1.02,
#     xanchor="right",
#     x=1
# ))
# # fig4.show()


# fig5 = make_subplots(specs=[[{"secondary_y": True}]])

# fill_colors = ['none', 'tozeroy', 'tozerox', 'tonexty', 'tonextx', 'toself', 'tonext']

# #negative
# fig5.add_trace(
#     go.Scatter(x=date
#            ,y=negativeIncrease
#            ,name="negativeIncrease"
#            ,line=dict(width=0.5, color='rgb(111, 231, 219)')
#            ,stackgroup='one'
#             ),
#     secondary_y=False,
# )
# #positive
# fig5.add_trace(
#     go.Scatter(x=date
#            ,y=positiveIncrease
#            ,fill=fill_colors[1]
#            ,mode="markers+lines"
#            ,name="positiveIncrease"),
#     secondary_y=False,
# )
# #total
# fig5.add_trace(
#     go.Scatter(x=date
#                ,y=totalTestResultsIncrease
#                ,opacity=.7
#                ,name="totalTestResultsIncrease"
#                ,line=dict(width=0.5, color='rgb(131, 90, 241)')
#                ,stackgroup='one'),
#     secondary_y=False,
# )

# # Add fig5ure title
# fig5.update_layout(
#     title_text="<b>Daily Pos/Neg and Total Tests</b>"
# )

# # Set x-axis title
# fig5.update_xaxes(title_text="<b>Date</b>")

# # Set y-axes titles
# fig5.update_yaxes(title_text="<b>Count Cases</b>", secondary_y=False)

# # Change the bar mode
# fig5.update_layout(barmode='stack')

# # Customize aspect
# fig5.update_traces(marker_line_width=.01)

# #update legend
# fig5.update_layout(
#     template='plotly_dark'
#     ,legend=dict(
#     orientation="h",
#     yanchor="bottom",
#     y=1.02,
#     xanchor="right",
#     x=1
# ))
# fig5.show()


# In[156]:


# fig6 = make_subplots(specs=[[{"secondary_y": True}]])

# fig6.add_trace(
#     go.Scatter(x=date
#                ,y=positive_pct_change
#                ,name="positive_pct_change"
#                ,marker_color=px.colors.qualitative.T10[2]
#                ,yaxis="y1")
# #     secondary_y=False,
# )
# fig6.add_trace(
#     go.Scatter(x=date
#                ,y=negative_pct_change
#                ,name="negative_pct_change"
#                ,marker_color=px.colors.qualitative.T10[4]
#                ,yaxis="y2")
# #     secondary_y=False,
# )
# fig6.add_trace(
#     go.Scatter(x=date
#                ,y=total_cases_pct_change
#                ,name="total_cases_pct_change"
#                ,marker_color=px.colors.qualitative.Plotly[3]
#                ,yaxis="y3")
# #     secondary_y=False,
# )

# Create axis objects
# fig6.update_layout(
# #     xaxis=date,
#     yaxis1=dict(
#         title="positive_pct_change",
#         titlefont=dict(
#             color="#663399"
#         ),
#         tickfont=dict(
#             color="#663399"
#         )
#     ),
#     yaxis2=dict(
#         title="negative_pct_change",
#         titlefont=dict(
#             color="#006600"
#         ),
#         tickfont=dict(
#             color="#006600"
#         ),
#         anchor="free",
#         overlaying="y",
#         side="right",
#         position=1
#     ),
#     yaxis3=dict(
#         title="total_cases_pct_change",
#         titlefont=dict(
#             color="#d62728"
#         ),
#         tickfont=dict(
#             color="#d62728"
#         ),
#         anchor="x",
#         overlaying="y",
#         side="right"
#     )
# )

# # Add fig6ure title
# fig6.update_layout(
#     title_text="<b>Daily Percent Changes of Covid Pos/Neg Tests and Total Tests</b>"
# )

# # Set x-axis title
# fig6.update_xaxes(title_text="<b>Date</b>")

# # Set y-axes titles
# fig6.update_yaxes(title_text="<b>Percent Change</b>", secondary_y=False)

# # Change the bar mode
# fig6.update_layout(barmode='stack')

# # Customize aspect
# fig6.update_traces(marker_line_width=.01)

# #update legend
# fig6.update_layout(legend=dict(
#     orientation="h",
#     yanchor="bottom",
#     y=1.02,
#     xanchor="right",
#     x=1
# ))

# fig6.update_layout(
#     # width=1200
#     template='plotly_dark'
# )
# fig6.show()


# second fig7ure
# fig7 = make_subplots(specs=[[{"secondary_y": True}]])

# fig7.add_trace(
#     go.Scatter(x=date
#                ,y=death_pct_change
#                ,name="death_pct_change"
#                ,marker_color=px.colors.qualitative.T10[0]),
#     secondary_y=False,
# )
# fig7.add_trace(
#     go.Scatter(x=date
#                ,y=hospitalized_pct_change
#                ,name="hospitalized_pct_change"
#                ,marker_color=px.colors.qualitative.T10[6]),
#     secondary_y=False,
# )

# # Add fig7ure title
# fig7.update_layout(
#     title_text="<b>Daily Percent Changes of Covid Death/Hospitalized</b>"
# )

# # Set x-axis title
# fig7.update_xaxes(title_text="<b>Date</b>")

# # Set y-axes titles
# fig7.update_yaxes(title_text="<b>Percent Change</b>", secondary_y=False)
# # fig7.update_yaxes(title_text="<b>% Change</b>", secondary_y=True)

# # Change the bar mode
# fig7.update_layout(barmode='stack')

# # Customize aspect
# fig7.update_traces(
# #                   marker_color='rgb(158,202,225)'
# #                   , marker_line_color='rgb(8,48,107)',
#                   marker_line_width=.1)
# #                   ,opacity=0.6)

# #update legend
# fig7.update_layout(legend=dict(
#     orientation="h",
#     yanchor="bottom",
#     y=1.02,
#     xanchor="right",
#     x=1,
# ))

# fig7.update_layout(
#     # width=1200
#     template='plotly_dark'
# )
# fig7.show()


fig8 = px.scatter(cases, x="date", y="positive_pct_change", trendline="lowess", color_continuous_scale=px.colors.sequential.Inferno
                  )
fig8.update_layout(
    height=800, template='plotly_dark')

fig8.add_trace(
    go.Scatter(x=date, y=negative_pct_change, name="negative_pct_change", mode="lines+markers", marker_color=px.colors.qualitative.T10[1]
               )
    #     secondary_y=False,
),
fig8.add_trace(
    go.Scatter(x=date, y=death_pct_change, name="death_pct_change", mode="lines+markers", marker_color=px.colors.qualitative.T10[2]
               )
    #     secondary_y=False,
),
fig8.add_trace(
    go.Scatter(x=date, y=hospitalized_pct_change, name="hospitalized_pct_change", mode="lines+markers", marker_color=px.colors.qualitative.T10[3]
               )
    #     secondary_y=False,
),
fig8.add_trace(
    go.Scatter(x=date, y=total_cases_pct_change, name="total_cases_pct_change", mode="lines+markers", marker_color=px.colors.qualitative.T10[4]
               )
    #     secondary_y=False,
)
# fig8.show()


fig9 = px.scatter(cases, x="date", y="positive_pct_change", trendline="lowess", title="positive_pct_change"  # , color_continuous_scale="icefire"
                  , color="positive_pct_change", color_continuous_scale=px.colors.sequential.Inferno, marginal_y="histogram", marginal_x="violin")
fig9.update_layout(
    height=400, template='plotly_dark')
# fig9.show()

fig10 = px.scatter(cases, x="date", y="negative_pct_change", color="negative_pct_change", trendline="lowess",
                   title="negative_pct_change", color_continuous_scale=px.colors.sequential.Inferno, marginal_y="histogram", marginal_x="violin")
fig10.update_layout(
    height=400, template='plotly_dark')
# fig10.show()

fig11 = px.scatter(cases, x="date", y="death_pct_change", color="death_pct_change", trendline="lowess", title="death_pct_change",
                   color_continuous_scale=px.colors.sequential.Inferno, marginal_y="histogram", marginal_x="violin")
fig11.update_layout(
    height=400, template='plotly_dark')
# fig11.show()

fig12 = px.scatter(cases, x="date", y="hospitalized_pct_change", color="hospitalized_pct_change", trendline="lowess",
                   title="hospitalized_pct_change", color_continuous_scale=px.colors.sequential.Inferno, marginal_y="histogram", marginal_x="violin")
fig12.update_layout(
    height=400, template='plotly_dark')
# fig12.show()

fig13 = px.scatter(cases, x="date", y="total_cases_pct_change", color="total_cases_pct_change", trendline="lowess",
                   title="total_cases_pct_change", color_continuous_scale=px.colors.sequential.Inferno, marginal_y="histogram", marginal_x="violin")
fig13.update_layout(
    height=400, template='plotly_dark')
# fig13.show()

# add traces
trace1 = fig9['data'][0]
trace2 = fig10['data'][0]
trace3 = fig11['data'][0]
trace4 = fig12['data'][0]
trace5 = fig13['data'][0]

fig14 = make_subplots(rows=3, cols=2, shared_xaxes=False, row_heights=[9., 9., 9.], column_widths=[.1, .1], shared_yaxes=False, vertical_spacing=0.10, subplot_titles=['<b>positive_pct_change</b>', '<b>negative_pct_change</b>', '<b>death_pct_change</b>', '<b>hospitalized_pct_change</b>', '<b>total_cases_pct_change</b>'
                                                                                                                                                                       ], x_title="<b>date</b>", y_title="<b>percent_change</b>"
                      )

fig14.add_trace(trace1, row=1, col=1)
fig14.add_trace(trace2, row=1, col=2)
fig14.add_trace(trace3, row=2, col=1)
fig14.add_trace(trace4, row=2, col=2)
fig14.add_trace(trace5, row=3, col=1)

fig14['layout'].update(height=800                       # , width=1200
                       , title='<b>Covid Test Outcome Trends</b>', template='plotly_dark')
# fig14.show()


# cases_melted.head()
cases_melted.variable.value_counts()
values_list = list(cases_melted.value)

fig15 = px.scatter(cases_melted, x="date", y="value", color="variable", facet_col="variable", trendline="lowess", trendline_color_override="white",
                   color_continuous_scale=px.colors.sequential.Inferno, marginal_y="bar", marginal_x="box", labels=['test', 'test', 'test', 'test', 'test'])

fig15['layout'].update(height=800                       # , width=1200
                       , title='<b>Covid Test Outcome Trends</b>', template='plotly_dark')
fig15.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
# fig15.show()


# make variables for subplots
percent_positive = list(cases.percent_positive)
percent_negative = list(cases.percent_negative)
negativeIncrease = list(cases.negativeIncrease)
positiveIncrease = list(cases.positiveIncrease)
totalTestResultsIncrease = list(cases.totalTestResultsIncrease)
total_cases_pct_change = list(cases.total_cases_pct_change)
positive_pct_change = list(cases.positive_pct_change)
date = list(cases.date)

# Create fig16ure with secondary y-axis
# fig16 = make_subplots(specs=[[{"secondary_y": True}]])

# # Add traces
# fig16.add_trace(
#     go.Bar(x=date
#            ,y=negativeIncrease
#            ,name="negativeIncrease"
#            ,marker_color=px.colors.qualitative.Pastel1[3]),
#     secondary_y=False,
# )
# fig16.add_trace(
#     go.Bar(x=date, y=positiveIncrease, name="positiveIncrease"),
#     secondary_y=False,
# )
# fig16.add_trace(
#     go.Scatter(x=date
#                ,y=totalTestResultsIncrease
#                ,opacity=.7
#                ,name="totalTestResultsIncrease"
#                ,mode="markers"
#                ,marker_color=px.colors.qualitative.Plotly[3]),
#     secondary_y=False,
# )
# fig16.add_trace(
#     go.Scatter(x=date
#                ,y=percent_negative
#                ,name="percent_negative"
#                ,marker_color=px.colors.qualitative.Plotly[2]),
#     secondary_y=True,
# )
# fig16.add_trace(
#     go.Scatter(x=date
#                ,y=percent_positive
#                ,name="percent_positive"
#                ,marker_color=px.colors.qualitative.D3[3]),
#     secondary_y=True,
# )
# fig16.add_trace(
#     go.Scatter(x=date
#                ,y=positive_pct_change
#                ,name="positive_pct_change"
#                ,marker_color=px.colors.qualitative.T10[2]),
#     secondary_y=True,
# )
# fig16.add_trace(
#     go.Scatter(x=date
#                ,y=negative_pct_change
#                ,name="negative_pct_change"
#                ,marker_color=px.colors.qualitative.Plotly[5]),
#     secondary_y=True,
# )
# fig16.add_trace(
#     go.Scatter(x=date
#                ,y=total_cases_pct_change
#                ,name="total_cases_pct_change"
#                ,marker_color=px.colors.qualitative.Plotly[3]),
#     secondary_y=True,
# )


# # Add fig16ure title
# fig16.update_layout(
#     title_text="<b>Daily Covid Cases</b>"
#     ,height=800
#     # ,width=1200
# )

# # Set x-axis title
# fig16.update_xaxes(title_text="<b>Date</b>")

# # Set y-axes titles
# fig16.update_yaxes(title_text="<b>Count Cases</b>", secondary_y=False)
# fig16.update_yaxes(title_text="<b>% Change</b>", secondary_y=True)

# # Change the bar mode
# fig16.update_layout(barmode='stack')

# # Customize aspect
# fig16.update_traces(marker_line_width=.01)

# #update legend
# fig16.update_layout(
#     template='plotly_dark'
#     ,legend=dict(
#     orientation="h",
#     yanchor="bottom",
#     y=1.02,
#     xanchor="right",
#     x=1
# ))
# fig16.show()


# create a day of week column
s = pd.date_range(min(df.date), max(df.date), freq='D').to_series()
s = s.dt.dayofweek.tolist()
df['day_of_week'] = s


def day_of_week(df):
    if df['day_of_week'] == 0:
        return "Tuesday"
    elif df['day_of_week'] == 1:
        return "Monday"
    elif df['day_of_week'] == 2:
        return "Sunday"
    elif df['day_of_week'] == 3:
        return "Saturday"
    elif df['day_of_week'] == 4:
        return "Friday"
    elif df['day_of_week'] == 5:
        return "Thursday"
    elif df['day_of_week'] == 6:
        return "Wednesday"
    else:
        return ""


df['dayofweek'] = df.apply(day_of_week, axis=1)
# df.head(30)


# create min and max variables
y_min = min(df.totalTestResultsIncrease)
y_max = max(df.totalTestResultsIncrease)
# x_min = min(df.index)
# x_max = max(df.index)
x_min = min(df.month)
x_max = max(df.month)
x_range = [x_min, x_max]
y_range = [y_min, y_max]

# print('y_min:',y_min)
# print('y_max:',y_max)
# print('x_min:',x_min)
# print('x_max:',x_max)
# print('x_range:',x_range)
# print('y_range:',y_range)


# create total pos/neg/total variables by day
total_pos_increase_grp_day = df.groupby(
    ['dayofweek'])['positiveIncrease'].sum()
avg_total_pos_increase_grp_day = df.groupby(
    ['dayofweek'])['positiveIncrease'].mean()

total_neg_increase_grp_day = df.groupby(
    ['dayofweek'])['negativeIncrease'].sum()
avg_total_neg_increase_grp_day = df.groupby(
    ['dayofweek'])['negativeIncrease'].mean()

total_increase_grp_day = df.groupby(
    ['dayofweek'])['totalTestResultsIncrease'].sum()
avg_total_increase_grp_day = df.groupby(
    ['dayofweek'])['totalTestResultsIncrease'].mean()

avg_total_per_week = avg_total_increase_grp_day/7
avg_pos_per_week = avg_total_pos_increase_grp_day/7
avg_neg_per_week = avg_total_neg_increase_grp_day/7


# print('total_pos_increase_grp_day:',total_pos_increase_grp_day)
# print("")
# print('total_neg_increase_grp_day:',total_neg_increase_grp_day)
# print("")
# print('total_increase_grp_day:',total_increase_grp_day)
# print("")
# print("")
# print('avg_total_pos_increase_grp_day:',avg_total_pos_increase_grp_day)
# print("")
# print('avg_total_neg_increase_grp_day:',avg_total_neg_increase_grp_day)
# print("")
# print('avg_total_increase_grp_day:',avg_total_increase_grp_day)
# print("")
# print("")
# print('avg_pos_per_week:',avg_pos_per_week)
# print("")
# print('avg_neg_per_week:',avg_neg_per_week)
# print("")
# print('avg_total_per_week:',avg_total_per_week)

# put totals in a list for labeling later on
total_totals = list(total_increase_grp_day)
pos_totals = list(total_pos_increase_grp_day)
neg_totals = list(total_neg_increase_grp_day)

# print('total_totals:', total_totals)
# print('pos_totals:', pos_totals)
# print('neg_totals:', neg_totals)

# make day list
x_labels = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
# print('x_labels:', x_labels)


# plots by day
fig17 = px.bar(df, x='dayofweek', y='positiveIncrease', text='positiveIncrease', color='dayofweek', height=500, hover_data=[
               'negativeIncrease', 'positiveIncrease', 'totalTestResultsIncrease'], hover_name="positiveIncrease")
fig1.update_traces(texttemplate='%{text:.2s}', textposition='top center')
fig1.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', title_text="<b>Covid Tests Outcome</b>", template='plotly_dark',
                   xaxis={'categoryorder': 'array', 'categoryarray': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']})

# Set x-axis title
fig17.update_xaxes(title_text="<b>Date</b>")

fig17.add_shape(  # add a horizontal "target" line
    type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=avg_total_increase_grp_day, y1=avg_total_increase_grp_day, yref="y"
)

fig17.add_annotation(  # add a text callout with arrow
    text="Woah...!", x="Friday", y=300, arrowhead=1, showarrow=True
)

total_labels = [{"x": x, "y": pos_totals*1.3, "text": str(
    pos_totals), "showarrow": False} for x, pos_totals in zip(x_labels, pos_totals)]

fig17.update_layout(uniformtext_minsize=8, uniformtext_mode='hide'                    # ,width=1200
                    , title_text="<b>Total Covid Tests Grouped by Day</b>", template='plotly_dark', xaxis={'categoryorder': 'array', 'categoryarray': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}, annotations=total_labels)
# fig17.show()


fig18 = px.bar(df, x='dayofweek', y='negativeIncrease', text='negativeIncrease', color='dayofweek', height=500, hover_data=[
               'negativeIncrease', 'positiveIncrease', 'totalTestResultsIncrease'], hover_name="negativeIncrease")
fig18.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig18.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', template='plotly_dark', title_text="<b>Neagtive Covid Tests Grouped by Day</b>",
                    xaxis={'categoryorder': 'array', 'categoryarray': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']})

# Set x-axis title
fig18.update_xaxes(title_text="<b>Date</b>")

fig18.add_shape(  # add a horizontal "target" line
    type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=avg_total_increase_grp_day, y1=avg_total_increase_grp_day, yref="y"
)

fig18.add_annotation(  # add a text callout with arrow
    text="Woah...!", x="Friday", y=300, arrowhead=1, showarrow=True
)

total_labels = [{"x": x, "y": neg_totals*1.25, "text": str(
    neg_totals), "showarrow": False} for x, neg_totals in zip(x_labels, neg_totals)]

fig18.update_layout(uniformtext_minsize=8, uniformtext_mode='hide'                    # ,width=1200
                    , title_text="<b>Total Covid Tests Grouped by Day</b>", template='plotly_dark', xaxis={'categoryorder': 'array', 'categoryarray': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}, annotations=total_labels)
# fig18.show()


fig19 = px.bar(df, x='dayofweek', y='totalTestResultsIncrease', text='totalTestResultsIncrease', color='dayofweek', height=500,
               hover_data=['negativeIncrease', 'positiveIncrease', 'totalTestResultsIncrease'], hover_name="totalTestResultsIncrease")
fig19.update_traces(texttemplate='%{text:.2s}', textposition='outside')

# Set x-axis title
fig19.update_xaxes(title_text="<b>Date</b>")

fig19.add_shape(  # add a horizontal "target" line
    type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=avg_total_increase_grp_day, y1=avg_total_increase_grp_day, yref="y"
)

fig19.add_annotation(  # add a text callout with arrow
    text="Woah...!", x="Friday", y=300, arrowhead=1, showarrow=True
)

total_labels = [{"x": x, "y": total_totals*.95, "text": str(
    total_totals), "showarrow": True} for x, total_totals in zip(x_labels, total_totals)]

fig19.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', title_text="<b>Total Covid Tests Grouped by Day</b>", template='plotly_dark'                    # ,width=1200
                    , xaxis={'categoryorder': 'array', 'categoryarray': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}, annotations=total_labels)
# fig19.show()


# deaths
fig20 = px.bar(df, x='dayofweek', y='deathIncrease', text='deathIncrease', color='dayofweek', height=500, hover_data=[
               'negativeIncrease', 'positiveIncrease', 'totalTestResultsIncrease', 'deathIncrease'], hover_name="deathIncrease")
fig20.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig20.update_layout(uniformtext_minsize=8, uniformtext_mode='hide'                    # ,width=1200
                    , title_text="<b>Death Covid Tests Grouped by Day</b>", template='plotly_dark', xaxis={'categoryorder': 'array', 'categoryarray': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']})

# Set x-axis title
fig20.update_xaxes(title_text="<b>Date</b>")

fig20.add_shape(  # add a horizontal "target" line
    type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=avg_total_increase_grp_day, y1=avg_total_increase_grp_day, yref="y"
)


fig20.update_layout(uniformtext_minsize=8, uniformtext_mode='hide'                    # ,width=1200
                    , title_text="<b>Total Covid Deaths Grouped by Day</b>", template='plotly_dark', xaxis={'categoryorder': 'array', 'categoryarray': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']})
#                  ,annotations=total_labels)
# fig20.show()


fig21 = px.bar(df, x='dayofweek', y='hospitalizedIncrease', text='hospitalizedIncrease', color='dayofweek', height=500, hover_data=[
               'negativeIncrease', 'positiveIncrease', 'totalTestResultsIncrease', 'deathIncrease', 'hospitalizedIncrease'], hover_name="hospitalizedIncrease")
fig21.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig21.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', title_text="<b>Hospitalized Covid Tests Grouped by Day</b>", template='plotly_dark'                    # ,width=1200
                    , xaxis={'categoryorder': 'array', 'categoryarray': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']})

# Set x-axis title
fig21.update_xaxes(title_text="<b>Date</b>")

fig21.add_shape(  # add a horizontal "target" line
    type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=avg_total_increase_grp_day, y1=avg_total_increase_grp_day, yref="y"
)

fig21.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', title_text="<b>Total Hospitalized Covid Deaths Grouped by Day</b>", template='plotly_dark',
                    xaxis={'categoryorder': 'array', 'categoryarray': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']})
# fig21.show()


# map day of week column to cases_melted dataframe
mapping = df[['date', 'dayofweek']]
# mapping
cases_melted = pd.merge(cases_melted, mapping, how='left', on=['date', 'date'])


fig22 = px.scatter(cases_melted, x="date", y="value", color="variable", facet_row="variable", facet_col="dayofweek", trendline="lowess",
                   trendline_color_override="white", color_continuous_scale=px.colors.sequential.Inferno, marginal_y="bar", marginal_x="box")

fig22['layout'].update(height=1000                       # , width=1200
                       , title='<b>Covid Test Outcome Trends</b>', template='plotly_dark')
fig22.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
# fig22.show()

fig23 = px.bar(cases_melted, x="date", y="value", color="variable", facet_row="variable",
               facet_col="dayofweek", color_continuous_scale=px.colors.sequential.Inferno)

fig23['layout'].update(height=1000                       # , width=1200
                       , title='<b>Covid Test Outcome Trends</b>', template='plotly_dark')
fig23.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
# fig23.show()


# cases_melted = cases_melted.drop(['dayofweek_x', 'dayofweek_y'], axis=1)
# cases_melted.style.background_gradient(cmap='Blues')


cases_melted['rank_value'] = cases_melted['value'].rank(method="max")
# print(cases_melted.head(30).sort_values(by='rank_value'))
# print(cases_melted.tail(30).sort_values(by='rank_value'))


# sum percent changes by day
# sundays have the highest positive percent changes
# tuesdays have the highest negative percent changes
cases_day = cases_melted[['dayofweek', 'value']]
cases_day = cases_day.groupby('dayofweek').sum().reset_index()
# cases_day.head(10).style.background_gradient(cmap='inferno')

fig24 = px.bar(cases_day, x="dayofweek", y="value", color="dayofweek", text="value",
               color_continuous_scale=px.colors.sequential.Inferno, template="plotly_dark")

fig24['layout'].update(height=800                       # , width=1200
                       , title='<b>Sum of Covid Test Daily Perent Changes per Day Of Week</b>', template='plotly_dark', yaxis_title="Sum of % Change", xaxis_title="Day of Week", legend_title="Day of Week", xaxis={'categoryorder': 'array', 'categoryarray': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
                       )
# fig24.show()


fig = px.bar(cases_melted, x="dayofweek", y="value", color="variable", hover_name="value",
             range_y=[-2, 2], animation_group="dayofweek", animation_frame=cases_melted.index)


fig['layout'].update(height=500                     # , width=1200
                     , title='<b>Covid Test Outcome Trends</b>', template='plotly_dark')
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
# fig.show()


fig25 = px.bar(cases_melted, x="date", y="value", color="variable",
               color_continuous_scale=px.colors.sequential.Inferno)

fig25['layout'].update(height=500                       # , width=1200
                       , title='<b>Sum of Covid Test Daily Percent Changes by Outcome</b>', yaxis_title="Sum of Daily % Changes", xaxis_title="Date", legend_title="Sum of Daily % Changes", template='plotly_dark')
fig25.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
# fig25.show()

fig26 = px.bar(cases_melted, x="date", y="value", color="dayofweek",
               color_continuous_scale=px.colors.sequential.Inferno)


fig26['layout'].update(height=500                       # , width=1200
                       , title='<b>Sum of Covid Test Daily Percent Changes by Outcome</b>', yaxis_title="Sum of Daily % Changes", xaxis_title="Date", legend_title="Day of Week", template='plotly_dark')
fig26.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
# fig26.show()

fig27 = px.bar(cases_melted, x="date", y="value", color="dayofweek",
               facet_col="dayofweek", color_continuous_scale=px.colors.sequential.Inferno)
#                  , facet_col_wrap=3)
#                  , size=cases_melted.index)

fig27['layout'].update(height=500                       # , width=1200
                       , title='<b>Covid Test Outcome Trends Grouped by Day Of Week</b>', template='plotly_dark', yaxis_title="Sum of Daily % Changes", xaxis_title="Day of Week", legend_title="Sum of Daily % Changes")
fig27.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
# fig27.show()

fig28 = px.bar(cases_melted, x="dayofweek", y="value", color="value",
               color_continuous_scale=px.colors.sequential.Inferno)
#                  , facet_col_wrap=3)
#                  , size=cases_melted.index)

fig28['layout'].update(height=500                       # , width=1200
                       , title='<b>Covid Test Outcome Trends Grouped by Day Of Week</b>', template='plotly_dark', yaxis_title="Sum of Daily % Changes", xaxis_title="Day of Week", legend_title="Sum of Daily % Changes")
fig28.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
# fig28.show()

fig29 = px.bar(cases_melted, x="variable", y="value", color="dayofweek",
               color_continuous_scale=px.colors.sequential.Inferno)
#                  , facet_col_wrap=3)
#                  , size=cases_melted.index)

fig29['layout'].update(height=500                       # , width=1200
                       , title='<b>Covid Test Outcome Trends Grouped by Day Of Week</b>', template='plotly_dark', yaxis_title="Sum of Daily % Changes", xaxis_title="Outcome", legend_title="Sum of Daily % Changes")
fig29.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
# fig29.show()

# create rounded columns and df
cases['total_rounded'] = cases.totalTestResultsIncrease.round(-4)
cases['percent_positive_rounded'] = cases.percent_positive.round(2)
cases['percent_negative_rounded'] = cases.percent_negative.round(2)
cases['percent_death_rounded'] = cases.percent_death.round(2)
cases['percent_hospitalized_rounded'] = cases.percent_hospitalized.round(2)

cases_rounded = cases[['date', 'total_rounded', 'percent_positive_rounded',
                       'percent_negative_rounded', 'percent_death_rounded', 'percent_hospitalized_rounded']]

# add 5 day moving average columns
cases_rounded['percent_pos_5d_avg'] = cases_rounded.rolling(
    window=5)['percent_positive_rounded'].mean()
cases_rounded['total_rounded_5d_avg'] = cases_rounded.rolling(window=5)[
    'total_rounded'].mean()
cases_rounded['percent_neg_5d_avg'] = cases_rounded.rolling(
    window=5)['percent_negative_rounded'].mean()
cases_rounded['percent_death_5d_avg'] = cases_rounded.rolling(
    window=5)['percent_death_rounded'].mean()
cases_rounded['percent_hospitalized_5d_avg'] = cases_rounded.rolling(
    window=5)['percent_hospitalized_rounded'].mean()

# create slope cols
cases_rounded['percent_pos_5d_avg_slope'] = cases_rounded.percent_pos_5d_avg.diff(
).fillna(0)
cases_rounded['total_rounded_5d_avg_slope'] = cases_rounded.total_rounded_5d_avg.diff(
).fillna(0)
cases_rounded['percent_neg_5d_avg_slope'] = cases_rounded.percent_neg_5d_avg.diff(
).fillna(0)
cases_rounded['percent_death_5d_avg_slope'] = cases_rounded.percent_death_5d_avg.diff(
).fillna(0)
cases_rounded['percent_hospitalized_5d_avg_slope'] = cases_rounded.percent_hospitalized_5d_avg.diff().fillna(0)

# convert lists
# rounded lists
total_rounded = list(cases_rounded.total_rounded)
percent_positive_rounded = list(cases_rounded.percent_positive_rounded)
percent_negative_rounded = list(cases_rounded.percent_negative_rounded)
percent_death_rounded = list(cases_rounded.percent_death_rounded)
percent_hospitalized_rounded = list(cases_rounded.percent_hospitalized_rounded)

# 5d avg lists
percent_pos_5d_avg = list(cases_rounded.percent_pos_5d_avg)
total_rounded_5d_avg = list(cases_rounded.total_rounded_5d_avg)
percent_neg_5d_avg = list(cases_rounded.percent_neg_5d_avg)
percent_death_5d_avg = list(cases_rounded.percent_death_5d_avg)
percent_hospitalized_5d_avg = list(cases_rounded.percent_hospitalized_5d_avg)

# slope lists
percent_pos_5d_avg_slope = list(cases_rounded.percent_pos_5d_avg_slope)
total_rounded_5d_avg_slope = list(cases_rounded.total_rounded_5d_avg_slope)
percent_neg_5d_avg_slope = list(cases_rounded.percent_neg_5d_avg_slope)
percent_death_5d_avg_slope = list(cases_rounded.percent_death_5d_avg_slope)
percent_hospitalized_5d_avg_slope = list(
    cases_rounded.percent_hospitalized_5d_avg_slope)


# Create fig30ure with secondary y-axis
fig30 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig30.add_trace(
    go.Scatter(x=date, y=total_rounded, name="total_rounded", mode="lines+markers"  # ,opacity=.5
               , marker_color=px.colors.qualitative.Plotly[3]),
    secondary_y=False,
)
fig30.add_trace(
    go.Scatter(x=date, y=percent_positive_rounded  # , opacity=.5
               , mode="lines+markers", marker_color=px.colors.qualitative.Plotly[5], name="percent_positive_rounded"),
    secondary_y=True,
)

# moving averages
fig30.add_trace(
    go.Scatter(x=date, y=total_rounded_5d_avg, opacity=.6, mode="lines",
               marker_color=px.colors.qualitative.Plotly[1], name="total_rounded_5d_avg"),
    secondary_y=False,
)
fig30.add_trace(
    go.Scatter(x=date, y=percent_pos_5d_avg, opacity=.6, mode="lines",
               marker_color=px.colors.qualitative.Plotly[1], name="percent_pos_5d_avg"),
    secondary_y=True,
)

# slopes
fig30.add_trace(
    go.Scatter(x=date, y=total_rounded_5d_avg_slope, opacity=.7, mode="lines",
               marker_color=px.colors.qualitative.Plotly[3], name="total_rounded_5d_avg_slope"),
    secondary_y=False,
)
fig30.add_trace(
    go.Scatter(x=date, y=percent_pos_5d_avg_slope, opacity=.7, mode="lines",
               marker_color=px.colors.qualitative.Plotly[5], name="percent_pos_5d_avg_slope"),
    secondary_y=True,
)

# Add fig30ure title
fig30.update_layout(
    title_text="<b>Total Daily Cases vs. Daily Percent Positive (Rounded) with 5 Day Moving Average and Slope</b>", height=800
)

# Set x-axis title
fig30.update_xaxes(title_text="<b>Date</b>")

# Set y-axes titles
fig30.update_yaxes(title_text="<b>Count Cases</b>", secondary_y=False)
fig30.update_yaxes(title_text="<b>% Positive Cases</b>", secondary_y=True)

# Change the bar mode
fig30.update_layout(barmode='stack')

# Customize aspect
fig30.update_traces(
    #                   marker_color='rgb(158,202,225)'
    #                   , marker_line_color='rgb(8,48,107)',
    marker_line_width=.01)
#                   ,opacity=0.6)

# update legend
fig30.update_layout(
    template='plotly_dark', legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.01,
        xanchor="right",
        x=1
    ))
# fig30.show()

# Create fig30ure with secondary y-axis
fig31 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig31.add_trace(
    go.Scatter(x=date, y=total_rounded, name="total_rounded", mode="lines+markers"  # ,opacity=.5
               , marker_color=px.colors.qualitative.Plotly[3]),
    secondary_y=False,
)
fig31.add_trace(
    go.Scatter(x=date, y=percent_negative_rounded  # , opacity=.5
               , mode="lines+markers", marker_color=px.colors.qualitative.Plotly[2], name="percent_negative_rounded"),
    secondary_y=True,
)

# moving averages
fig31.add_trace(
    go.Scatter(x=date, y=total_rounded_5d_avg, opacity=.6, mode="lines",
               marker_color=px.colors.qualitative.Plotly[1], name="total_rounded_5d_avg"),
    secondary_y=False,
)
fig31.add_trace(
    go.Scatter(x=date, y=percent_neg_5d_avg, opacity=.6, mode="lines",
               marker_color=px.colors.qualitative.Plotly[1], name="percent_neg_5d_avg"),
    secondary_y=True,
)

# slopes
fig31.add_trace(
    go.Scatter(x=date, y=total_rounded_5d_avg_slope, opacity=.7, mode="lines",
               marker_color=px.colors.qualitative.Plotly[3], name="total_rounded_5d_avg_slope"),
    secondary_y=False,
)
fig31.add_trace(
    go.Scatter(x=date, y=percent_neg_5d_avg_slope, opacity=.7, mode="lines",
               marker_color=px.colors.qualitative.Plotly[2], name="percent_neg_5d_avg_slope"),
    secondary_y=True,
)

# Add fig30ure title
fig31.update_layout(
    title_text="<b>Total Daily Cases vs. Daily Percent Negative (Rounded) with 5 Day Moving Average and Slope</b>", height=800
)

# Set x-axis title
fig31.update_xaxes(title_text="<b>Date</b>")

# Set y-axes titles
fig31.update_yaxes(title_text="<b>Count Cases</b>", secondary_y=False)
fig31.update_yaxes(title_text="<b>% Negative Cases</b>", secondary_y=True)

# Change the bar mode
fig31.update_layout(barmode='stack')

# Customize aspect
fig31.update_traces(
    #                   marker_color='rgb(158,202,225)'
    #                   , marker_line_color='rgb(8,48,107)',
    marker_line_width=.01)
#                   ,opacity=0.6)

# update legend
fig31.update_layout(
    template='plotly_dark', legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.01,
        xanchor="right",
        x=1
    ))
# fig31.show()

# Create fig30ure with secondary y-axis
fig32 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig32.add_trace(
    go.Scatter(x=date, y=total_rounded, name="total_rounded", mode="lines+markers"  # ,opacity=.5
               , marker_color=px.colors.qualitative.Plotly[3]),
    secondary_y=False,
)
fig32.add_trace(
    go.Scatter(x=date, y=percent_death_rounded  # , opacity=.5
               , mode="lines+markers", marker_color=px.colors.qualitative.Plotly[6], name="percent_death_rounded"),
    secondary_y=True,
)

# moving averages
fig32.add_trace(
    go.Scatter(x=date, y=total_rounded_5d_avg, opacity=.6, mode="lines",
               marker_color=px.colors.qualitative.Plotly[1], name="total_rounded_5d_avg"),
    secondary_y=False,
)
fig32.add_trace(
    go.Scatter(x=date, y=percent_death_5d_avg, opacity=.6, mode="lines",
               marker_color=px.colors.qualitative.Plotly[1], name="percent_death_5d_avg"),
    secondary_y=True,
)

# slopes
fig32.add_trace(
    go.Scatter(x=date, y=total_rounded_5d_avg_slope, opacity=.7, mode="lines",
               marker_color=px.colors.qualitative.Plotly[3], name="total_rounded_5d_avg_slope"),
    secondary_y=False,
)
fig32.add_trace(
    go.Scatter(x=date, y=percent_death_5d_avg_slope, opacity=.7, mode="lines",
               marker_color=px.colors.qualitative.Plotly[6], name="percent_death_5d_avg_slope"),
    secondary_y=True,
)

# Add fig30ure title
fig32.update_layout(
    title_text="<b>Total Daily Cases vs. Daily Percent Death (Rounded) with 5 Day Moving Average and Slope</b>", height=800
)

# Set x-axis title
fig32.update_xaxes(title_text="<b>Date</b>")

# Set y-axes titles
fig32.update_yaxes(title_text="<b>Count Cases</b>", secondary_y=False)
fig32.update_yaxes(title_text="<b>% Death Cases</b>", secondary_y=True)

# Change the bar mode
fig32.update_layout(barmode='stack')

# Customize aspect
fig32.update_traces(
    #                   marker_color='rgb(158,202,225)'
    #                   , marker_line_color='rgb(8,48,107)',
    marker_line_width=.01)
#                   ,opacity=0.6)

# update legend
fig32.update_layout(
    template='plotly_dark', legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.01,
        xanchor="right",
        x=1
    ))
# fig32.show()

# Create fig30ure with secondary y-axis
fig33 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig33.add_trace(
    go.Scatter(x=date, y=total_rounded, name="total_rounded", mode="lines+markers"  # ,opacity=.5
               , marker_color=px.colors.qualitative.Plotly[3]),
    secondary_y=False,
)
fig33.add_trace(
    go.Scatter(x=date, y=percent_hospitalized_rounded  # , opacity=.5
               , mode="lines+markers", marker_color=px.colors.qualitative.Plotly[4], name="percent_hospitalized_rounded"),
    secondary_y=True,
)

# moving averages
fig33.add_trace(
    go.Scatter(x=date, y=total_rounded_5d_avg, opacity=.6, mode="lines",
               marker_color=px.colors.qualitative.Plotly[1], name="total_rounded_5d_avg"),
    secondary_y=False,
)
fig33.add_trace(
    go.Scatter(x=date, y=percent_hospitalized_5d_avg, opacity=.6, mode="lines",
               marker_color=px.colors.qualitative.Plotly[1], name="percent_hospitalized_5d_avg"),
    secondary_y=True,
)

# slopes
fig33.add_trace(
    go.Scatter(x=date, y=total_rounded_5d_avg_slope, opacity=.7, mode="lines",
               marker_color=px.colors.qualitative.Plotly[3], name="total_rounded_5d_avg_slope"),
    secondary_y=False,
)
fig33.add_trace(
    go.Scatter(x=date, y=percent_hospitalized_5d_avg_slope, opacity=.7, mode="lines",
               marker_color=px.colors.qualitative.Plotly[4], name="percent_hospitalized_5d_avg_slope"),
    secondary_y=True,
)

# Add fig30ure title
fig33.update_layout(
    title_text="<b>Total Daily Cases vs. Daily Percent Hospitalized (Rounded) with 5 Day Moving Average and Slope</b>", height=800
)

# Set x-axis title
fig33.update_xaxes(title_text="<b>Date</b>")

# Set y-axes titles
fig33.update_yaxes(title_text="<b>Count Cases</b>", secondary_y=False)
fig33.update_yaxes(title_text="<b>% Hospitalized Cases</b>", secondary_y=True)

# Change the bar mode
fig33.update_layout(barmode='stack')

# Customize aspect
fig33.update_traces(
    #                   marker_color='rgb(158,202,225)'
    #                   , marker_line_color='rgb(8,48,107)',
    marker_line_width=.01)
#                   ,opacity=0.6)

# update legend
fig33.update_layout(
    template='plotly_dark', legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="right",
        x=1
    ))


print("graphs created.....")
