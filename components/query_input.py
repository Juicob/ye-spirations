import dash_bootstrap_components as dbc
import dash_html_components as html
import random


def get_query_input(placeholder):
    query_input = html.Div(
        [
            dbc.Input(id="query-input", placeholder=placeholder, type="text"),
            html.Br(),
            html.P(id="output"),
        ]
    )
    return query_input
