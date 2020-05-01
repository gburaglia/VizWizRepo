import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from datetime import datetime
import logging
import os
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objects as go

from functions import (retrieve_data, build_targ, get_states, build_loc, draw_loc_trace, draw_targ_trace, draw_parties_trace, build_parties, draw_polls_trace, create_parties_limits,
build_polls, build_polls_zarray, build_polls_limits, generate_polls_mapped_z, generate_polls_colors, create_parties_limits, map_layout, draw_map, get_bar_data)

start_date= "1/03/2020"
end_date = "2/17/2020"
mynum=4
loc_df, targ_df, parties_df, polls_df, kwords = retrieve_data()
cleaned_pivot = build_targ(targ_df)
loc_tbl = build_loc(loc_df)
parties_df,zarray = build_parties(parties_df)
polls_max_filtered_df, polls_orgvotes_df = build_polls(polls_df,start_date,end_date)
layout = map_layout()

external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        {%css%}
        <title>{%title%}</title>
        {%favicon%}
    </head>
    <body>
        <div></div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>Accenture VizWiz Challenge</div>
    </body>
</html>
<script src="/static/barplots.js"></script>
'''

app.layout = html.Div(children=[
    html.H1(children='Politcal Ad Spending on Google'),

    html.Div(className ='maintext', children='''
        Data is provided by Google Open Data and can be found on their BigQuery platform.
    '''),

    html.Div(className='container',children=[
    html.Div([
        html.Div(className="barhalfA", children = [
            html.Div(className='plotHolder', children=[
                html.Div(id='loading', className='loading', children = [
                    html.Div(id='circle1',className='circle1',children=5),
                    html.Div(id='circle2',className='circle2',children=3),
                    html.Div(id='circle3', className='circle3',children=1),
                    html.Div(id='circle4', className='circle4',children=2),
                    html.Div(id='circle5', className='circle5',children=4),
                    html.Div(id='axis1', className='axis'),
                    html.Div(id='lab1',className='lab1',children=None),
                    html.Div(id='lab2',className='lab2',children=None),
                    html.Div(id='lab3', className='lab3',children=None),
                    html.Div(id='lab4', className='lab4',children=None),
                    html.Div(id='lab5', className='lab5',children=None),
                    html.Div(id='barTitle', className='barTitle',children="Average Polling Score")
                    ]),
                ])
            ]),
            html.Div(className="barhalfB", children = [
                html.Div([
                    html.Label("Pick Date Range"),
                    dcc.DatePickerRange(
                        id='my-bar-date-picker-range',
                        min_date_allowed=datetime(1995, 8, 5),
                        max_date_allowed=datetime(2020, 9, 19),
                        start_date = datetime(2020,1,3).date(),
                        end_date=datetime(2020, 2, 17).date(),
                        minimum_nights = 7
                    ),
                    html.Label('Select Bars'),
                    dcc.Dropdown(id='bar_select',
                        options=[
                            {'label': 'Poll Winners', 'value':'1'},
                            {'label': 'Poll Ratings', 'value':'3'},
                            {'label': 'Google Keywords Total Spend', 'value':'2'},
                        ],
                        value='1'
                    ),
                    html.Div(id='output-container-bar-date-picker-range'),
                    html.Br(),
                    dcc.Dropdown(
                        id = 'dropdown-poll-type',
                        options=[
                            {'label': 'Democratic', 'value': '1'},
                            {'label': 'Republican', 'value': '2'}
                        ],value = '1', style = {'display': 'block'}
                    ),
                ]),
            ])
            ],className="row")
        ]),
        html.Br(),

        html.Label('Select Map'),
        dcc.Dropdown(id='map_select',
            options=[
                {'label': 'Poll Winners', 'value': '4'},
                {'label': 'State Party Identification', 'value': '3'},
                {'label': 'Ad Targeting', 'value': '2'},
                {'label': 'Ad Spending', 'value': '1'}
            ],
            value='4'
        ),
        html.Div([
            html.Label("Pick Date Range"),
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=datetime(1995, 8, 5),
                    max_date_allowed=datetime(2020, 9, 19),
                    start_date = datetime(2020,1,3).date(),
                    end_date=datetime(2020, 2, 17).date()
                ),
            html.Div(id='output-container-date-picker-range')
        ]),
    dcc.Graph(
        id='example-graph'
    )

])

@app.callback(
   Output('dropdown-poll-type', 'style'),
   [Input(component_id='bar_select', component_property='value')])
def show_hide_element(visibility_state):
    if visibility_state == 1:
        return {'display': 'block'}
    if int(visibility_state) == 2:
        return {'display': 'none'}
    if visibility_state == 3:
        return {'display': 'block'}

@app.callback(
    Output('example-graph', 'figure'),
    [Input(component_id='map_select', component_property='value'),
    Input(component_id='my-date-picker-range', component_property='start_date'),
    Input(component_id='my-date-picker-range', component_property='end_date')]
)
def update_map(input_value,start_date,end_date):
    polls_max_filtered_df, polls_orgvotes_df = build_polls(polls_df,start_date,end_date)
    mynum=input_value
    displayFig, displayData = draw_map(mynum, loc_tbl, cleaned_pivot, parties_df, zarray, polls_orgvotes_df)
    layout = map_layout()
    displayFig.update_layout(layout)
    return displayFig

@app.callback(
    [Output(component_id = 'circle1', component_property = 'children'),
    Output(component_id = 'circle2', component_property = 'children'),
    Output(component_id = 'circle3', component_property = 'children'),
    Output(component_id = 'circle4', component_property = 'children'),
    Output(component_id = 'circle5', component_property = 'children'),
    Output(component_id ='my-bar-date-picker-range', component_property='min_date_allowed'),
    Output(component_id = 'my-bar-date-picker-range', component_property = 'max_date_allowed'),
    Output(component_id = 'lab1', component_property = 'children'),
    Output(component_id = 'lab2', component_property = 'children'),
    Output(component_id = 'lab3', component_property = 'children'),
    Output(component_id = 'lab4', component_property = 'children'),
    Output(component_id = 'lab5', component_property = 'children'),
    Output(component_id = 'barTitle', component_property = 'children')
    ],
    [Input(component_id='bar_select', component_property='value'),
    Input(component_id='my-bar-date-picker-range', component_property='start_date'),
    Input(component_id='my-bar-date-picker-range', component_property='end_date'),
    Input(component_id='dropdown-poll-type', component_property='value')
    ]
)
def update_bar(input_value,start_date,end_date,poll_type=None):

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    if int(input_value) == 1:
        start_date_b = min(pd.to_datetime(polls_df['Week Beginning']))
        end_date_b = max(pd.to_datetime(polls_df['Week Beginning']))
        title = "Polls Won"
        if start_date > end_date_b or end_date < start_date_b:
            start_date = start_date_b
            end_date = end_date_b
        elif start_date < start_date_b:
            start_date = start_date_b
        elif end_date > end_date_b:
            end_date = end_date_b
    elif int(input_value) == 2:
        kwords['Report_Date'] = pd.to_datetime(kwords['Report_Date'])
        start_date_b = min(kwords.Report_Date)
        end_date_b = max(kwords.Report_Date)
        title = "Total Keyword Ad Spend in Millions"
        if start_date > end_date_b or end_date < start_date_b:
            start_date = start_date_b
            end_date = end_date_b
        elif start_date < start_date_b:
            start_date = start_date_b
        elif end_date > end_date_b:
            end_date = end_date_b
    else:
        start_date_b = min(pd.to_datetime(polls_df['Week Beginning']))
        end_date_b = max(pd.to_datetime(polls_df['Week Beginning']))
        title = "Percentage Share of Polling Choices"
        if start_date > end_date_b or end_date < start_date_b:
            start_date = start_date_b
            end_date = end_date_b
        elif start_date < start_date_b:
            start_date = start_date_b
        elif end_date > end_date_b:
            end_date = end_date_b

    numbers, names = get_bar_data(int(input_value), start_date, end_date, polls_df, kwords, poll_type)

    return numbers[3],numbers[1],numbers[0],numbers[2],numbers[4], start_date_b, end_date_b, names[3], names[1], names[0], names[2], names[4], title

if __name__ == '__main__':
    app.run_server(debug=True,port=3050)
