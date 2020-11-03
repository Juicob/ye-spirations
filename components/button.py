import dash_html_components as html
import dash_bootstrap_components as dbc

button = dbc.Button("Click for Inspiration",
                    className="inspiration-button",
                    id="submit-button",
                    color="light",
                    block=True,
                    n_clicks=0)

button_container = html.Div(id='button-container',
                            children=[
                                button
                            ])