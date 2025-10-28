from dash import Dash, html, dcc, Input, Output, State
from dash.dependencies import MATCH
import dash_daq as daq

# Sample data for plotting
sample_data_1_x = [1, 2, 3, 4, 5]
sample_data_1_y = [2, 5, 3, 8, 7]
sample_data_2_x = [1, 2, 3, 4, 5]
sample_data_2_y = [3, 1, 4, 6, 2]

def get_layout():
    """Return the layout for app_3"""
    return html.Div([
        html.H1("App 3 - Line vs Scatter Plot Toggle"),
        html.P("Toggle the switch to change between line and scatter plots."),
        daq.ToggleSwitch(
            id='toggle-switch-app3',
            label='Scatter Plot / Line Plot ',
            value=True  # Default to line plot
        ),
        dcc.Graph(
            id='graph-app3',
            figure={
                'data': [
                    {'x': [1, 2, 3, 4, 5], 'y': [2, 5, 3, 8, 7], 'type': 'scatter', 'mode': 'lines', 'name': 'Dataset 1'},
                    {'x': [1, 2, 3, 4, 5], 'y': [3, 1, 4, 6, 2], 'type': 'scatter', 'mode': 'lines', 'name': 'Dataset 2'}
                ],
                'layout': {'title': 'Graph (Line Plot)'}
            }
        )
    ])

def register_callbacks(app):
    """Register callbacks for app_3 with the provided app instance"""
    
    # Callback to update graph type based on toggle
    @app.callback(
        Output('graph-app3', 'figure'),
        Input('toggle-switch-app3', 'value')
    )
    def update_graph_type_app3(toggle_value):
        if toggle_value:
            # Line plot
            title_suffix = " (Line Plot)"
            data = [
                {'x': sample_data_1_x, 'y': sample_data_1_y, 'type': 'scatter', 'mode': 'lines', 'name': 'Dataset 1'},
                {'x': sample_data_2_x, 'y': sample_data_2_y, 'type': 'scatter', 'mode': 'lines', 'name': 'Dataset 2'}
            ]
        else:
            # Scatter plot
            title_suffix = " (Scatter Plot)"
            data = [
                {'x': sample_data_1_x, 'y': sample_data_1_y, 'type': 'scatter', 'mode': 'markers', 'name': 'Dataset 1'},
                {'x': sample_data_2_x, 'y': sample_data_2_y, 'type': 'scatter', 'mode': 'markers', 'name': 'Dataset 2'}
            ]
        
        return {
            'data': data,
            'layout': {'title': f'Graph{title_suffix}'}
        }

# Keep the original standalone functionality
if __name__ == "__main__":
    app = Dash(__name__)
    app.layout = get_layout()
    register_callbacks(app)
    app.run(debug=True)