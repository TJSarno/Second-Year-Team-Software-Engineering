import plotly.graph_objects as go
import plotly_express as px
import pandas as pd

# Lists of avaliable plotly continuous colourscales etc.
CONTINUOUS_COLOUR_SCALES = px.colors.named_colorscales()


UNIVARIATE_GRAPHS= [
    'Histogram',
    'Box Plot'
]

BIVARIATE_GRAPHS = [
    'Overlaid Histogram',
    'Scatter Plot'
]


def choropleth(df, x_variable, location_mode, countries, colour_scheme):
    fig = go.Figure(data=go.Choropleth(
        locations=df[countries],  # Spatial coordinates
        z=df[x_variable].astype(float),  # Data to be color-coded
        locationmode=location_mode,  # set of locations match entries in `locations`
        colorscale=colour_scheme,
        text=df[countries],
    ))
    fig.update_layout(
        autosize=True,
        margin=go.layout.Margin(
            l=10, r=10, b=25, t=25,
            pad=2
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title=x_variable,
        title_x=0.5,
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="#ffffff"
        )
    )
    return fig


# TODO finish implementation of histogram fig
def histogram(df, x_variable):
    fig = go.Figure(data=go.Histogram(x=df[x_variable]))
    fig.update_layout(
        autosize=True,
        margin=go.layout.Margin(
            l=10, r=10, b=25, t=25,
            pad=2
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title=x_variable,
        title_x=0.5,
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="#ffffff"
        )
    )
    return fig


def overlaid_histogram(df, x1_variable, x2_variable):
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x = df[x1_variable],
        name = x1_variable
        )
    )
    fig.add_trace(go.Histogram(
        x = df[x2_variable],
        name = x2_variable
        )
    )
    fig.update_layout(
        autosize=True,
        margin=go.layout.Margin(
            l=10, r=10, b=25, t=25,
            pad=2
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="#ffffff"
        )
    )
    return fig


def scatter_plot(df, x_variable, y_variable, countries):
    fig = go.Figure(
        data=go.Scatter(x=df[x_variable],
        y=df[y_variable],
        mode='markers',
        marker_color=df[x_variable],
        text=df[countries])) # hover text goes here

    fig.update_layout(
        autosize=True,
        margin=go.layout.Margin(
            l=10, r=10, b=25, t=25,
            pad=2
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title=x_variable,
        title_x=0.5,
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="#ffffff"
        )
    )
    return fig


def box_plot(df, x_variable):
    fig = go.Figure()
    fig.add_trace(go.Box(y=df[x_variable], name=x_variable))

    fig.update_layout(
        autosize=True,
        margin=go.layout.Margin(
            l=10, r=10, b=25, t=25,
            pad=2
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title=x_variable,
        title_x=0.5,
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="#ffffff"
        )
    )
    return fig
