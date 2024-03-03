import dash
from dash import Dash, Output, Input, State, html, callback
import dash_mantine_components as dmc
from flowfunc import Flowfunc, config, jobrunner
from components.nodes import *

# dash.register_page(__name__, path='/')
dash.register_page(__name__)

"""
    Flowfunc configurations
"""
flist = [
    conv2d,
    subtract,
]

fconfig = config.Config.from_function_list(flist)
runner = jobrunner.JobRunner(fconfig)

"""
    Yaml Preview Function
"""
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

layout = html.Div([
    # html.H1('step1'),
    dmc.Container(
        children=[
            YmlPreview,
            Flowfunc(
                id="node_editor",
                config=fconfig.dict(),
                disable_zoom=True,
                type_safety=False,
            ),
        ],
        size="auto",
        style={"sizes": "lg", "marginBottom": 20, "height": "85dvh", "width": "100%"},
    )
])

@callback(
    Output("yml_preview", "opened"),
    Input("open_preview", "n_clicks"),
    prevent_initial_call=True
)
def toggle_drawer(n_clicks):
    return True