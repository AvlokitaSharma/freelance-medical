# Import necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample Data: Replace with the startup company's data
# For demonstration, create a simple DataFrame
df = pd.DataFrame({
    "Date": pd.date_range(start="2024-01-01", periods=120, freq="D"),
    "RecoveryRate": pd.np.random.rand(120) * 100,
    "Department": pd.np.random.choice(["Cardiology", "Neurology", "Oncology", "Pediatrics"], size=120)
})

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Health Data Visualization Dashboard", style={'text-align': 'center'}),
    dcc.Dropdown(
        id="select_department",
        options=[{"label": i, "value": i} for i in df['Department'].unique()],
        multi=False,
        value="Cardiology",
        style={'width': "40%"}
    ),
    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='my_health_data', figure={})
])

# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_health_data', component_property='figure')],
    [Input(component_id='select_department', component_property='value')]
)
def update_graph(option_selected):
    container = f"Department: {option_selected}"

    dff = df.copy()
    dff = dff[dff["Department"] == option_selected]

    # Example visualization: Recovery Rate over time for selected department
    fig = px.line(
        data_frame=dff,
        x="Date",
        y="RecoveryRate",
        title="Recovery Rate Over Time"
    )

    return container, fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
