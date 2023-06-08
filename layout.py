import os
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from app import DATASETS_PATH


# Serve page layout
def serve_layout():
    return html.Div(id='root', children=[
        dcc.Store(id='session', storage_type='local'),


        
        html.Span(id='main-span', children=[
            html.Div(id='sidebar', children=[
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select File to upload')
                    ]),
                    # Do NOT Allow SIMULTANEOUS uploads by the user
                    multiple=False
                ),
                # List all .csv or .xls files hosted on the server
                html.Div(id='file-list',
                    children=[dcc.Dropdown(id='files', options=[
                        {'label': filename,'value': filename} for filename in
                        os.listdir(DATASETS_PATH)],
                        placeholder="Select Dataset"),
                    ]),
                 ]),
                html.Button('Populate menu', id='show-dashboard-opts'),
                html.Div(id='dashboard-creation-area')
            ]),
            html.Div(id='body', children=[
                html.Div(id='choropleth-output-area'),

                #All code relating to the nav bar and it's various buttons
                html.Div(id='topnav', className='shortbutton', children=[
                html.Button(className='invisible', children=[
                    html.Img(className='LeftArrow', src='assets/Blackleftarrow.png')
                    ]),
                html.Button(className='invisible', children=[
                    html.P('Home',className='topnavtext')
                    ]),
                html.Button(className='invisible', children=[
                    html.P('View',className='topnavtext')
                    ]),
                html.Button(className='invisible', children=[
                    html.P('Create',className='topnavtext')
                    ]),
                html.Button(className='invisible', children=[
                    html.P('About',className='topnavtext')
                    ]),
                html.Button(style={'float':'right'},id='Night',className='invisible', children=[
                    html.Img(src='assets/Night.png')
                    ]),
                html.Button(style={'float':'right'},id='Day',className='invisible', children=[
                    html.Img(src='assets/Day.png')
                    ]),
            ]),
            html.Div(id='line', className='line'),

            #Main body for View
            html.Div(id='View', className='MainContainer', children=[
                html.Button(className='invisible', children=[
                    html.Img(className='TopArrow', src='assets/Blackuparrow.png'),
                    ]),
            html.P('Discover the Data we have curated',className='MainText'),
                #Not sure how <br>s are implemented but this is my attempt
            html.Br('and find what the implications are.'),
            html.Img(className='MainPicture', src='assets/heatmap.png'),
            html.Button(className='invisible', children=[
                html.Img(className='RightArrow', src='assets/Blackrightarrow.png')
                ]),
            html.Button(className='invisible', children=[
                html.Img(className='DownArrow', src='assets/Blackdownarrow.png')
                ]),

            ]),

            #Main body for Create
            html.Div(id='Create', className='MainContainer', children=[
                html.Button(className='invisible', children=[
                    html.Img(className='TopArrow', src='assets/Blackuparrow.png'),
                    ]),
            html.P('Discover the Data we have curated',className='MainText'),
                #Not sure how <br>s are implemented but this is my attempt
            html.Br('and find what the implications are.'),
            html.Img(className='MainPicture', src='assets/report.png'),
            html.Button(className='invisible', children=[
                html.Img(className='RightArrow', src='assets/Blackrightarrow.png')
                ]),
            html.Button(className='invisible', children=[
                html.Img(className='DownArrow', src='assets/Blackdownarrow.png')
                ]),

            ]),

            #Main body for About
            html.Div(id='About', className='MainContainer', children=[
                html.Button(className='invisible', children=[
                    html.Img(className='TopArrow', src='assets/greyworldmap.png'),
                    ]),
            html.P('Discover the Data we have curated',className='MainText'),
                #Not sure how <br>s are implemented but this is my attempt
            html.Br('and find what the implications are.'),
            html.Img(className='MainPicture', src='assets/greyworldmap.png'),
            html.Button(className='invisible', children=[
                html.Img(className='RightArrow', src='assets/Blackrightarrow.png')
                ]),
            html.Button(className='invisible', children=[
                html.Img(className='DownArrow', src='assets/Blackdownarrow.png')
                ]),

            ]),

            html.Div(id='NextView', className = 'MainContainer', children=[
                html.P('View')
                ]),
            html.Div(id='NextCreate', className = 'MainContainer', children=[
                html.P('Create')
                ]),
            html.Div(id='NextAbout', className = 'MainContainer', children=[
                html.P('Create')
                ]),
            
            
                
            html.Div(id='stats'),
            html.Div(id='graph-creation-area'),
            html.Div(id='download-area'),










                ]),






        ])
