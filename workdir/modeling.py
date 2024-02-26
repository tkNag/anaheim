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
                    description="create basement",
                    children=dmc.Text(
                        "Step 1 Base Architecture", align="center"
                    ),
                ),
                dmc.StepperStep(
                    label="Second Step",
                    description="add computational blocks",
                    children=dmc.Text(
                        "Step 2 Computational Blocks / Sub-modules", align="center"
                    ),
                ),
                dmc.StepperStep(
                    label="Third Step",
                    description="augment params",
                    children=dmc.Text(
                        "Step 3 Hyper parameters Modification", align="center"
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
            title="Preview (Hydra Yaml)",
            id="yml_preview",
            zIndex=10000,
            size="55%",
            padding="md",
            position="right",
            children=[
                dmc.Text('Check your network architecture'),
                dmc.Spoiler(
                    showLabel="Show more",
                    hideLabel="Hide",
                    maxHeight=150,
                    children=[
                        dmc.Code(
                            """
                                use_gpu: True

                                model:
                                name: "ViT"
                                image_size: 72  # We'll resize input images to this size
                                patch_size: 6  # Size of the patches to be extract from the input images
                                projection_dim: 64
                                num_heads: 4
                                transformer_layers: 8
                                mlp_head_units: [2048, 1024]  # Size of the dense layers of the final classifier
                                num_classes: 100

                                train:
                                learning_rate: 0.001
                                weight_decay: 0.0001
                                batch_size: 100
                                num_epochs: 100
                            """,
                            block=True
                        )
                    ]
                )
            ]
        ),
        dmc.Group(
            spacing="xl",
            children=[
                dmc.Button("Preview (Yaml)", id="open_preview", style={"align": "right"}),
            ],
            style={
                "marginBottom": "5px"
            }
        )
    ]
)

Footer = html.Div(
    dmc.Footer(
        height=120,
        fixed=True,
        children=[
            dmc.Text("Fujifilm Software, inc. Division of Development, NS/NPS.")
        ],
        style={
            "backgroundColor": "#f7f9fa"
        }
    ),
)

app.layout = html.Div([
    html.Div(
        dmc.Header(
            height=70,
            children=[
                dmc.Image("../assets/text-1708161623047.png", width=180)
            ]
        )
    ),
    html.Div(
        children=[
            dmc.Container(
                Stepper,
                size="lg",
                style={
                    "marginTop": "15px"
                }
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
                style={"sizes": "lg", "marginBottom": 20, "height": "75dvh", "width": "100%"}
                # style={"height": "80vh", "width": "100%"}
            )
        ]
    ),
    Footer
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