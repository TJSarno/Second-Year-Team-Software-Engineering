import os
import re
import plotly.graph_objects as go
import pandas as pd
import dash_table as dt
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from pandas.api.types import is_string_dtype, is_numeric_dtype
from app import app, DATASETS_PATH
from graphs import *
from stats import *


# Callback to create the choropleth from user dataset
@app.callback(Output('choropleth-output-area', 'children'),
    [Input('create-dashboard', 'n_clicks')],
    [State('x-variable-dropdown', 'value'), State('countries', 'value'),
    State('location-radio', 'value'), State('files', 'value'),
    State('colour-dropdown', 'value'), State('normalization-radio', 'value')])
def create_choropleth(n_clicks,
                    x_variable,
                    countries,
                    location_mode,
                    filename,
                    colour_scheme,
                    normalization):
    if n_clicks is None:
        raise PreventUpdate

    df = pd.read_csv(os.path.join(DATASETS_PATH, filename))
    if normalization != 'None':
        df = normalize(df, normalization)

    if not is_numeric_dtype(df[x_variable]):
        return html.H3("Error: Can not create choropleth from non-quantative variable.")

    if not is_string_dtype(df[countries]):
        return html.H3("Error: Locations for plotting must be a string type.")

    if location_mode == 'ISO-3':
        ISO_3 = re.compile('^[A-Z]{3}$')
        invalid_records = df[~df[countries].str.contains(ISO_3)]
        if not invalid_records.empty:
            return html.H3("Error: Non ISO-3 complient entries in countries column.")

    #TODO NORMALIZATION TEST
    fig = choropleth(df, x_variable, location_mode, countries, colour_scheme)
    return [
        dcc.Graph(id='user-choropleth', figure=fig),
        html.Div(id='country-data')
    ]


@app.callback(Output('graph-creation-area', 'children'),
    [Input('create-dashboard', 'n_clicks')],
    [State('files', 'value'), State('x-variable-dropdown', 'value'),
    State('y-variable-dropdown', 'value'), State('normalization-radio', 'value')])
def populate_graph_menu(n_clicks, filename, x_variable, y_variable, normalization):
    if n_clicks is None:
        raise PreventUpdate

    df = pd.read_csv(os.path.join(DATASETS_PATH, filename))
    if normalization != 'None':
        df = normalize(df, normalization)
    # Default/starting graph
    fig = histogram(df, x_variable)

    if y_variable is not None:
        GRAPH_TYPES = UNIVARIATE_GRAPHS + BIVARIATE_GRAPHS
    else:
        GRAPH_TYPES = UNIVARIATE_GRAPHS

    return [
        dcc.Dropdown(id='graph-type',
                options=[{'label': graph_type, 'value': graph_type}
                            for graph_type in GRAPH_TYPES],
                value=GRAPH_TYPES[0]),
        html.Button('Graph selection', id='graph-selection'),
        html.Div(id='graph-output-area', children=[
            dcc.Graph(id='user-graph', figure=fig)
            ]
        )
    ]


@app.callback(Output('graph-output-area', 'children'),
    [Input('graph-selection', 'n_clicks')],
    [State('graph-type', 'value')])
def graph_type_options(n_clicks, graph_type):
    if n_clicks is None:
        raise PreventUpdate

    if graph_type == 'Histogram':
        return [
            html.Button('Create Histogram', id='create-histogram'),
            dcc.Graph(id='user-histogram')
        ]
    elif graph_type == 'Overlaid Histogram':
        return [
            html.Button('Create Overlaid Histogram', id='create-overlaid-histogram'),
            dcc.Graph(id='user-overlaid-histogram')
        ]
    elif graph_type == 'Scatter Plot':
        return [
            html.Button('Create Scatter Plot', id='create-scatter-plot'),
            dcc.Graph(id='user-scatter-plot')
        ]
    elif graph_type == 'Box Plot':
         return [
            html.Button('Create Box Plot', id='create-box-plot'),
            dcc.Graph(id='user-box-plot')
        ]


@app.callback(Output('user-histogram', 'figure'),
    [Input('create-histogram', 'n_clicks')],
    [State('x-variable-dropdown', 'value'), State('files', 'value'),
    State('normalization-radio', 'value')])
def create_histogram(n_clicks,
                x_variable,
                filename,
                normalization):
    if n_clicks is None:
        raise PreventUpdate

    df = pd.read_csv(os.path.join(DATASETS_PATH, filename))
    if normalization != 'None':
        df = normalize(df, normalization)

    fig = histogram(df, x_variable)
    return fig


@app.callback(Output('user-overlaid-histogram', 'figure'),
    [Input('create-overlaid-histogram', 'n_clicks')],
    [State('x-variable-dropdown', 'value'), State('y-variable-dropdown', 'value'),
    State('files', 'value'),State('normalization-radio', 'value')])
def create_overlaid_histogram(n_clicks,
                x_variable,
                y_variable,
                filename,
                normalization):
    if n_clicks is None:
        raise PreventUpdate

    df = pd.read_csv(os.path.join(DATASETS_PATH, filename))
    if normalization != 'None':
        df = normalize(df, normalization)

    fig = overlaid_histogram(df, x_variable, y_variable)
    return fig


@app.callback(Output('user-scatter-plot', 'figure'),
    [Input('create-scatter-plot', 'n_clicks')],
    [State('x-variable-dropdown', 'value'), State('y-variable-dropdown', 'value'),
    State('files', 'value'), State('countries', 'value'), 
    State('normalization-radio', 'value')])
def create_scatter_plot(n_clicks,
                x_variable,
                y_variable,
                filename,
                countries,
                normalization):
    if n_clicks is None:
        raise PreventUpdate

    df = pd.read_csv(os.path.join(DATASETS_PATH, filename))
    if normalization != 'None':
        df = normalize(df, normalization)

    fig = scatter_plot(df, x_variable, y_variable, countries)
    return fig


@app.callback(Output('user-box-plot', 'figure'),
    [Input('create-box-plot', 'n_clicks')],
    [State('x-variable-dropdown', 'value'), State('files', 'value'),
     State('normalization-radio', 'value')])
def create_box_plot(n_clicks,
                x_variable,
                filename,
                normalization):
    if n_clicks is None:
        raise PreventUpdate

    df = pd.read_csv(os.path.join(DATASETS_PATH, filename))
    if normalization != 'None':
        df = normalize(df, normalization)

    fig = box_plot(df, x_variable)
    return fig
