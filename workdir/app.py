import dash
from dash import Dash, Output, Input, State, html, callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from flowfunc import Flowfunc, config, jobrunner

app = dash.Dash(__name__)

"""
    page layout 
    https://dash.plotly.com/urls
"""
app.layout = html.Div([

])

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8088)