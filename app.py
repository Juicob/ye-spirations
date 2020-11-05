import dash

import random

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from dash.dependencies import Input, Output, State

from components.button import button
from components.query_input import get_query_input

external_stylesheets = dbc.themes.LUX

app = dash.Dash(__name__, external_stylesheets=[external_stylesheets])

app.title = "Ye-Spirations"

server = app.server

app.layout = html.Div(children=[
    html.Div(className="big-container",
             children=[
                 dcc.Interval(id="app-interval-timer", interval=3.6e6, n_intervals=0),
                 html.H1("Ye-Spirations"),
                 html.Div(id="query-input-container", children=[]),
                 button,
                 html.Br(),
                 html.Div(id="image-container",
                          children=[])
    ])
])


@app.callback(Output(component_id="image-container", component_property="children"),
              [Input(component_id="submit-button", component_property="n_clicks")])
def return_on_click(n_clicks):
    if n_clicks == 0:
        src = "https://assets.capitalxtra.com/2013/40/kanye-3-1381050600-view-1.jpg"
        return html.Img(className="inspiration-image", src=src)
    else:
        message = f"You have clicked the button\n{n_clicks} times"
        return html.H3(message)

# comment
@app.callback(Output(component_id="query-input-container", component_property="children"),
              [Input(component_id="app-interval-timer", component_property="n_intervals")])
def refresh_placeholder(n_intervals):
    placeholders = ["what's your vibe?",
                    "how you feeling?",
                    "where do you want to go?",
                    "where's your favorite memory?",
                    "what's your favorite drug?"]
    placeholder = random.choice(placeholders)
    query_input = get_query_input(placeholder=placeholder)
    return query_input

if __name__ == "__main__":
    app.run_server('localhost', debug=True)
