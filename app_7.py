from dash import Dash, html, dcc, Input, Output, State, callback_context
from dash.dependencies import MATCH, ALL
import dash_daq as daq
import numpy as np
import json

def min_max_normalize(data):
    min_val = min(data)
    max_val = max(data)

    if min_val == max_val:
        # All values are the same, return an array of zeros
        return np.array([0.0] * len(data))  # Return a NUMPY ARRAY of zeros

    min_max_normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return np.array(min_max_normalized_data)  # Return a NUMPY ARRAY

# Data for this app
sample_data_1_x = [1, 2, 3]
sample_data_1_y = [1, 2, 3]
sample_data_2_x = [1, 2, 3]
sample_data_2_y = [2, 4, 6]

raw_data_source = [
    {'x': sample_data_1_x, 'y': sample_data_1_y, 'type': 'line', 'name': 'Sample Data 1'},
    {'x': sample_data_2_x, 'y': sample_data_2_y, 'type': 'line', 'name': 'Sample Data 2'},
]

normalized_data_source = [
    {'x': min_max_normalize(sample_data_1_x), 'y': min_max_normalize(sample_data_1_y), 'type': 'line', 'name': 'Sample Data 1'},
    {'x': min_max_normalize(sample_data_2_x), 'y': min_max_normalize(sample_data_2_y), 'type': 'line', 'name': 'Sample Data 2'},
]

def get_layout():
    """Return the layout for app_7"""
    return html.Div([
        html.H1("App 7 - Append Approach with Dictionary IDs"),
        html.P("This app appends graphs instead of recreating them, using dictionary-style IDs."),
        html.Button("Click Me", id={"type": "my-button", "app": "app7"}),
        html.Div(id={"type": "output-div", "app": "app7"}),
        dcc.Store(id={"type": "graph-counter", "app": "app7"}, data=0)
    ])

def register_callbacks(app):
    """Register callbacks for app_7 with the provided app instance"""
    
    # Use the MATCH pattern to update individual graphs based on their corresponding toggle switch
    @app.callback(
        Output({'type': 'graph', 'app': 'app7', 'index': MATCH}, 'figure'),
        Input({'type': 'toggle-switch', 'app': 'app7', 'index': MATCH}, 'value'),
        State({'type': 'toggle-switch', 'app': 'app7', 'index': MATCH}, 'id')
    )
    def update_graph_app7(toggle_value, toggle_id):
        index = toggle_id['index']
        
        if toggle_value:
            data = raw_data_source
            title_suffix = " (Raw)"
        else:
            data = normalized_data_source
            title_suffix = " (Normalized)"
        
        return {
            'data': data,
            'layout': {'title': f'Graph for Click {index + 1}{title_suffix}'}
        }

    @app.callback(
        [Output({"type": "output-div", "app": "app7"}, "children"), Output({"type": "graph-counter", "app": "app7"}, "data")],
        Input({"type": "my-button", "app": "app7"}, "n_clicks"),
        [State({"type": "output-div", "app": "app7"}, "children"), State({"type": "graph-counter", "app": "app7"}, "data")]
    )
    def update_output_app7(n_clicks, current_children, current_count):
        if n_clicks is None or n_clicks == 0:
            return "Button not clicked yet.", 0
        
        # If this is the first click, start fresh
        if current_children == "Button not clicked yet." or current_children is None:
            current_children = []
            current_count = 0
        
        # Only add a new graph if we have more clicks than current graphs
        if n_clicks > current_count:
            # Create the new graph with index equal to current_count
            new_graph = html.Div([
                daq.ToggleSwitch(
                    id={'type': 'toggle-switch', 'app': 'app7', 'index': current_count},
                    label='Toggle Graph',
                    value=True  # Default to raw data
                ),
                dcc.Graph(
                    id={'type': 'graph', 'app': 'app7', 'index': current_count},
                    figure={
                        'data': raw_data_source,
                        'layout': {'title': f'Graph for Click {current_count + 1} (Raw)'}
                    }
                )
            ])
            
            # Append the new graph to existing children
            current_children.append(new_graph)
            current_count = n_clicks
        
        return current_children, current_count

# Keep the original standalone functionality
if __name__ == "__main__":
    app = Dash(__name__)
    app.layout = get_layout()
    register_callbacks(app)
    app.run(debug=True)