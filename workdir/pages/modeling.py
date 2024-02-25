import dash
from dash import Dash, Output, Input, State, html, callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from flowfunc import Flowfunc, config, jobrunner

app = Dash(__name__)


def conv2d(input1, input2, filters: int, stride: int):
    """Add two numbers"""
    layer = '' ## tensorflow/keras conv2d()
    return layer, input1

def subtract(a: int, b: int):
    """Subtract one number from another"""
    return a - b


flist = [
    conv2d,
    subtract,
]
app = dash.Dash(__name__)
fconfig = config.Config.from_function_list(flist)
runner = jobrunner.JobRunner(fconfig)

Stepper = html.Div(
    children=[
        dmc.Stepper(
            id="stepper",
            active=0,
            breakpoint="sm",
            children=[
                dmc.StepperStep(
                    label="First Step",
                    description="first step",
                    children=dmc.Text(
                        "Step 1 content: first", align="center"
                    ),
                ),
                dmc.StepperStep(
                    label="Second Step",
                    description="second step",
                    children=dmc.Text(
                        "Step 2 content: second", align="center"
                    ),
                ),
                dmc.StepperStep(
                    label="Third Step",
                    description="third step",
                    children=dmc.Text(
                        "Step 3 content: third", align="center"
                    ),
                ),
            ]
        ),
        dmc.Group(
            children=[
                dmc.Button("Left step"),
                dmc.Button("Right step"),
            ],
            position="center"
        )
    ]
)

Navbar = dmc.Navbar(
    p="md",
    fixed=False,
    width={"base": 300},
    hidden=True,
    hiddenBreakpoint="md",
    height='100vh',
    id='sidebar',
    children=[
        html.Div(
            [
                dmc.NavLink(
                    label="With icon",
                    icon=DashIconify(icon="bi:house-door-fill", height=16, color="#c2c7d0")
                ),
            ]
        )
    ]
)

YmlPreview = html.Div(
    [
        dmc.Drawer(
            id="yml_preview",
            zIndex=10000,
            size="55%",
            padding="md",
            position="right",
            children=[
                dmc.Text('hoghoge')
            ]
        ),
        dmc.Group(
            align="center",
            spacing="xl",
            children=[
                dmc.Button("Preview (Yaml)", id="open_preview"),
            ]
        )
    ]
)

app.layout = html.Div([
    html.Div(

        dmc.Header(
            height=70,
            children=[
                dmc.Image("/assets/text-1708161623047.png", width=180)
            ]
        )
    ),
    html.Div(
        children=[
            dmc.Container(
                Stepper,
                size="lg"
            ),
            dmc.Container(
                children=[
                    YmlPreview,
                    Flowfunc(
                        id="nodeeditor",
                        config=fconfig.dict(),
                        disable_zoom=False,
                        type_safety=False,
                    ),
                ],
                size = "lg",
                style={"height": "85vh", "width": "100%"}
            )
        ]
    )
])

@callback(
    Output("yml_preview", "opened"),
    Input("open_preview", "n_clicks"),
    prevent_initial_call=True
)
def toggle_drawer(n_clicks):
    return True

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8088)