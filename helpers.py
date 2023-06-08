import base64
import io
import pandas as pd
from dash.exceptions import PreventUpdate
from app import app
import os


def parse_file_to_df(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    if filename.endswith('.csv') or filename.endswith('.xls'):
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    #elif filename.endswith('xls'):
     #   df = pd.read_excel(io.BytesIO(decoded))
    else:
        raise ValueError
    return df
