from dash import Dash, html, dcc, Input, Output

def get_layout():
    """Return the layout for app_1"""
    return html.Div([
        html.H1("App 1 - Basic Application"),
        html.P("This is a simple Dash application."),
        html.Button("Click Me", id="my-button-app1"),
        html.Div(id="output-div-app1")
    ])

def register_callbacks(app):
    """Register callbacks for app_1 with the provided app instance"""
    @app.callback(
        Output("output-div-app1", "children"),
        Input("my-button-app1", "n_clicks")
    )
    def update_output_app1(n_clicks):
        if n_clicks is None:
            return "Button not clicked yet."
        else:
            return f"Button clicked {n_clicks} times."

# Keep the original standalone functionality
if __name__ == "__main__":
    app = Dash(__name__)
    app.layout = get_layout()
    register_callbacks(app)
    app.run(debug=True)