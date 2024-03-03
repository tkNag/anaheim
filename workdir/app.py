import dash
from dash import Dash, Output, Input, State, html, callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify

app = Dash(__name__, assets_folder='/workdir/assets', use_pages=True)

"""
    General Contents
"""
Header = html.Div([
    dmc.Header(
        height=70,
        children=[
            dmc.Image(src=dash.get_asset_url('app_logo.png'), width=180),
        ],
        style={
            "marginBottom": 20,
        }
    ),
])

def get_icon(icon):
    return DashIconify(icon=icon, height=16)

Navbar = html.Div([
        dmc.NavLink(
            label="Step1",
            icon=get_icon(icon="bi:house-door-fill"),
            href="/step1"
        ),
])

"""
    page layout 
    https://dash.plotly.com/urls
"""
app.layout = html.Div([
    Header,
    dmc.Grid(
        children=[
            dmc.Col(
                # html.H1("navbar"),
                Navbar,
                span=2
            ),
            dmc.Col(
                # html.H1("main"),
                dash.page_container,
                span=9
            ),
            dmc.Col(
                html.H1("right_side"),
                span=1
            )
        ]
    ),
])

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8088)