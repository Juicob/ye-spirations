import dash_html_components as html
import dash_bootstrap_components as dbc

button = dbc.Button("Click for Inspiration",
                    id="submit-button",
                    color="light",
                    block=True,
                    n_clicks=0,
                    style={"margin-right": "20px", "margin-left": "20px", "width":"50%"})

button_container = html.Div(id='button-container',
                            children=[
                                button
                            ])