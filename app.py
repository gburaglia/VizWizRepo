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
build_polls, build_polls_zarray, build_polls_limits, generate_polls_mapped_z, generate_polls_colors, create_parties_limits, map_layout, draw_map, draw_bars)

# import dash_html_components as html
#
# html.Div([
#     html.H1('Hello Dash'),
#     html.Div([
#         html.P('Dash converts Python classes into HTML'),
#         html.P('This conversion happens behind the scenes by Dash's JavaScript front-end')
#     ])
# ])
# ---------------------
# <div>
#     <h1>Hello Dash</h1>
#     <div>
#         <p>Dash converts Python classes into HTML</p>
#         <p>This conversion happens behind the scenes by Dash's JavaScript front-end</p>
#     </div>
# </div>
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

loc_df, targ_df, parties_df, polls_df = retrieve_data()
#Transform data
cleaned_pivot = build_targ(targ_df)
loc_tbl = build_loc(loc_df)
parties_df,zarray = build_parties(parties_df)

start_date= "1/03/2020"
end_date = "2/17/2020"
polls_orgvotes_df = build_polls(polls_df,start_date,end_date)
layout = map_layout()
mynum=4
#displayFig, displayData = draw_map(mynum, loc_tbl, cleaned_pivot, parties_df, zarray, polls_orgvotes_df)
#displayFig.update_layout(layout)

fig=draw_bars()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div(children=[
        html.Div(className='container',children=[
            html.H1(children='Politcal Ad Spending on Google'),



            html.Div(children='''
                Data is provided by Google Open Data and can be found on their BigQuery platform.
            '''),

]),
            html.H3('Candidates'),
                    html.Div([
                        dcc.Graph(id='g1', figure = fig),
                        ]),
            html.H3('Select Map'),
            dcc.Dropdown(id='map_select',
                options=[
                    {'label': 'Polling Results', 'value': '4'},
                    {'label': 'Party Affiliation', 'value': '3'},
                    {'label': 'Ad Targetting', 'value': '2'},
                    {'label': 'Politcal Ad Spending', 'value': '1'}
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

]),
])
    # dcc.Graph(
    #     id='example-graph',
    #     figure=displayFig
    # )
@app.callback(
    Output('example-graph', 'figure'),
    [Input(component_id='map_select', component_property='value'),
    Input(component_id='my-date-picker-range', component_property='start_date'),
    Input(component_id='my-date-picker-range', component_property='end_date')]
)
def update_map(input_value,start_date,end_date):
    polls_orgvotes_df = build_polls(polls_df,start_date,end_date)
    mynum=input_value
    displayFig, displayData = draw_map(mynum, loc_tbl, cleaned_pivot, parties_df, zarray, polls_orgvotes_df)
    layout = map_layout()
    displayFig.update_layout(layout)
    return displayFig

if __name__ == '__main__':
    app.run_server(debug=True, port=3004)
