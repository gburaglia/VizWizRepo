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
build_polls, build_polls_zarray, build_polls_limits, generate_polls_mapped_z, generate_polls_colors, create_parties_limits, map_layout, draw_map)

loc_df, targ_df, parties_df, polls_df = retrieve_data()
cleaned_pivot = build_targ(targ_df)
loc_tbl = build_loc(loc_df)
parties_df,zarray = build_parties(parties_df)
polls_orgvotes_df = build_polls(polls_df)
layout = map_layout()
mynum=4
start_date= "1/03/2020"
end_date = "2/17/2020"

app = dash.Dash(__name__)
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
        html.Div(className='plotHolder', children=[
            html.Div(id='loading', className='loading', children = [
                html.Div(id='circle1', className='circle1',children=np.random.randint(20, size=1)),
                html.Div(id='circle2', className='circle2',children=np.random.randint(20, size=1)),
                html.Div(id='circle3', className='circle3',children=np.random.randint(20, size=1)),
                html.Div(id='circle4', className='circle4',children=np.random.randint(20, size=1)),
                html.Div(id='circle5', className='circle5',children=np.random.randint(20, size=1)),
                html.Div(id='axis1', className='axis')
                ]),
            ])
        ]),
        html.Br(),

        html.Label('Select Map'),
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

])

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

# @app.callback(
#     Output('cirlce1','c1Value')
# )
# def getC1Value():
#     value = np.randint(0,20)
#     return value


if __name__ == '__main__':
    app.run_server(debug=True)
