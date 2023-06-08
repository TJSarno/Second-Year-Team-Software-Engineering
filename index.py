import dash_core_components as dcc
import dash_html_components as html
import uiCallbacks
import graphCallbacks
from dash.dependencies import Input, Output, State
from app import app
from layout import serve_layout


app.layout = serve_layout
application = app.server

if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
