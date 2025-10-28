from dash import Dash, html
import app_1
import app_2
import app_3
import app_4
import app_7

# Initialize the main app
app = Dash(__name__, suppress_callback_exceptions=True)

# Main layout combining all apps
app.layout = html.Div([
    html.H1("App 6 - Combined Apps Platform", style={'textAlign': 'center'}),
    html.P("This platform combines multiple apps using their existing unique IDs.", style={'textAlign': 'center'}),
    html.Hr(),
    
    # Import layouts from each app
    app_1.get_layout(),
    html.Hr(),
    app_2.get_layout(),
    html.Hr(),
    app_3.get_layout(),
    html.Hr(),
    app_4.get_layout(),
    html.Hr(),
    app_7.get_layout()
])

# Register all callbacks from imported apps
app_1.register_callbacks(app)
app_2.register_callbacks(app)
app_3.register_callbacks(app)
app_4.register_callbacks(app)
app_7.register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True, port=8051)