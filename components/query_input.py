import dash_bootstrap_components as dbc
import dash_html_components as html


query_input = html.Div(
    [
        dbc.Input(id="query-input", placeholder="What's Your Mood?", type="text"),
        html.Br(),
        html.P(id="output"),
    ]
)
