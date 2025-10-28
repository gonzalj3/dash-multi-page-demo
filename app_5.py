from dash import Dash, html, dcc, register_page, page_container
import app_1
import app_2
import app_3
import app_4

# Initialize the main app with pages enabled
app = Dash(__name__, use_pages=True, pages_folder="", suppress_callback_exceptions=True)

# Register pages by importing layouts from each app module
register_page(
    module='app_1',
    path='/',
    name='App 1 - Basic',
    title='Basic Dash Application',
    layout=app_1.get_layout
)

register_page(
    module='app_2',
    path='/app2',
    name='App 2 - Store', 
    title='App with Toggle Store',
    layout=app_2.get_layout
)

register_page(
    module='app_3',
    path='/app3',
    name='App 3 - Plot Toggle',
    title='Line vs Scatter Plot Toggle',
    layout=app_3.get_layout
)

register_page(
    module='app_4',
    path='/app4',
    name='App 4 - Append',
    title='App with Append Approach', 
    layout=app_4.get_layout
)

# Register all callbacks from imported apps
app_1.register_callbacks(app)
app_2.register_callbacks(app)
app_3.register_callbacks(app)
app_4.register_callbacks(app)

# Main layout with navigation
app.layout = html.Div([
    html.H1("Multi-Page Dash Application Platform", style={'textAlign': 'center'}),
    html.P("Choose an application to explore different approaches:", style={'textAlign': 'center'}),
    
    # Navigation bar
    html.Div([
        dcc.Link("App 1 - Basic", href="/", className="nav-link"),
        " | ",
        dcc.Link("App 2 - Store Approach", href="/app2", className="nav-link"), 
        " | ",
        dcc.Link("App 3 - Plot Toggle", href="/app3", className="nav-link"),
        " | ",
        dcc.Link("App 4 - Append Approach", href="/app4", className="nav-link"),
    ], style={
        'margin': '20px 0', 
        'textAlign': 'center', 
        'padding': '10px',
        'backgroundColor': '#f0f0f0',
        'border': '1px solid #ddd'
    }),
    
    html.Hr(),
    
    # This container will display the selected page
    page_container
])

if __name__ == "__main__":
    app.run(debug=True, port=8050)