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
    """Return the layout for app_2"""
    return html.Div([
        html.H1("App 2 - With Store for Toggle States"),
        html.P("This app uses dcc.Store to maintain toggle states."),
        html.Button("Click Me", id="my-button-app2"),
        html.Div(id="output-div-app2"),
        dcc.Store(id="toggle-states-app2", data={})
    ])

def register_callbacks(app):
    """Register callbacks for app_2 with the provided app instance"""
    
    # Callback to store toggle states
    @app.callback(
        Output("toggle-states-app2", "data"),
        Input({'type': 'toggle-switch-app2', 'index': ALL}, 'value'),
        State("toggle-states-app2", "data")
    )
    def store_toggle_state_app2(toggle_values, stored_states):
        # Get the triggered input to find which toggle was clicked
        ctx = callback_context
        if not ctx.triggered:
            return stored_states
        
        # Extract index from triggered input
        triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
        toggle_id = json.loads(triggered_id)
        index = str(toggle_id['index'])
        
        # Get the specific toggle value from the list
        if toggle_values and len(toggle_values) > toggle_id['index']:
            toggle_value = toggle_values[toggle_id['index']]
            stored_states[index] = toggle_value
        return stored_states

    # Use the MATCH pattern to update individual graphs based on their corresponding toggle switch
    @app.callback(
        Output({'type': 'graph-app2', 'index': MATCH}, 'figure'),
        Input({'type': 'toggle-switch-app2', 'index': MATCH}, 'value'),
        State({'type': 'toggle-switch-app2', 'index': MATCH}, 'id')
    )
    def update_graph_app2(toggle_value, toggle_id):
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
        Output("output-div-app2", "children"),
        Input("my-button-app2", "n_clicks"),
        State("toggle-states-app2", "data")
    )
    def update_output_app2(n_clicks, stored_states):
        if n_clicks is None:
            return "Button not clicked yet."
        else:
            graph_to_return=[]
            for click in range(n_clicks):
                # Get stored toggle state or default to True (raw data)
                toggle_value = stored_states.get(str(click), True)
                
                # Choose data based on stored toggle state
                if toggle_value:
                    data = raw_data_source
                    title_suffix = " (Raw)"
                else:
                    data = normalized_data_source
                    title_suffix = " (Normalized)"
                
                new_graph=html.Div([
                    daq.ToggleSwitch(
                        id={'type': 'toggle-switch-app2', 'index': click},
                        label='Toggle Graph',
                        value=toggle_value
                    ),
                    dcc.Graph(
                        id={'type': 'graph-app2', 'index': click},
                        figure={
                            'data': data,
                            'layout': {'title': f'Graph for Click {click + 1}{title_suffix}'}
                        }
                    )
                ])
                graph_to_return.append(new_graph)
            return graph_to_return

# Keep the original standalone functionality
if __name__ == "__main__":
    app = Dash(__name__)
    app.layout = get_layout()
    register_callbacks(app)
    app.run(debug=True)