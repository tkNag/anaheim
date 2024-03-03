import dash
from dash import html, dash_table
import dash_mantine_components as dmc
import pandas as pd

dash.register_page(__name__, path='/')

dict = dict(
    ModelName=["MobileNet v2", "ResNet-50", "EfficientNet"],
    Platform=["Keras", "Keras", "PyTorch"],
    Description=["Lightweight segmentation model", "Regular model", "Regular model 2"],
    CreateDate=["2023/02/23", "2022/12/04", "2024/01/09"],
)
df = pd.DataFrame(data=dict)


ModelTable = html.Div(
    dash_table.DataTable(
        id='model_table',
        columns=[
            {"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        row_selectable="single",
        row_deletable=True,
        page_current=0,
        page_size=20,
        page_action="native"
    )
)

layout = html.Div([
    # html.H1('Home'),
    ModelTable,
])