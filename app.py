import dash

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from dash.dependencies import Input, Output, State

from components.button import button

external_stylesheets = dbc.themes.LUX

app = dash.Dash(__name__, external_stylesheets=[external_stylesheets])

app.title = "Ye-Spirations"

server = app.server

app.layout = html.Div(children=[
    html.Div(className="big-container",
             children=[
                 html.H1("Ye-Spirations"),
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


if __name__ == "__main__":
    app.run_server('localhost', debug=True)
