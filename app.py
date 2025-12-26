import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Read the processed data
df = pd.read_csv('output.csv')

# Convert date column to datetime for proper sorting
df['date'] = pd.to_datetime(df['date'])

# Sort by date
df = df.sort_values('date')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout with styling
app.layout = html.Div(
    style={
        'backgroundColor': '#f0f2f5',
        'minHeight': '100vh',
        'padding': '20px',
        'fontFamily': 'Arial, sans-serif'
    },
    children=[
        # Header Section
        html.Div([
            html.H1(
                "Pink Morsel Sales Visualizer",
                style={
                    'textAlign': 'center',
                    'color': '#FF1493',
                    'fontSize': '48px',
                    'fontWeight': 'bold',
                    'marginBottom': '10px',
                    'textShadow': '2px 2px 4px rgba(0,0,0,0.1)'
                }
            ),
            html.P(
                "Analyzing sales before and after the price increase on January 15, 2021",
                style={
                    'textAlign': 'center',
                    'fontSize': '18px',
                    'color': '#555',
                    'marginBottom': '30px'
                }
            ),
        ]),

        # Filter Section
        html.Div([
            html.Label(
                "Select Region:",
                style={
                    'fontSize': '20px',
                    'fontWeight': 'bold',
                    'color': '#333',
                    'marginBottom': '10px',
                    'display': 'block'
                }
            ),
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': ' All Regions', 'value': 'all'},
                    {'label': ' North', 'value': 'north'},
                    {'label': ' East', 'value': 'east'},
                    {'label': ' South', 'value': 'south'},
                    {'label': ' West', 'value': 'west'}
                ],
                value='all',
                inline=True,
                style={
                    'fontSize': '16px',
                    'color': '#444'
                },
                inputStyle={
                    'marginRight': '5px',
                    'marginLeft': '15px'
                },
                labelStyle={
                    'marginRight': '20px',
                    'cursor': 'pointer'
                }
            ),
        ], style={
            'backgroundColor': 'white',
            'padding': '20px',
            'borderRadius': '10px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.1)',
            'marginBottom': '30px',
            'maxWidth': '1200px',
            'margin': '0 auto 30px auto'
        }),

        # Chart Section
        html.Div([
            dcc.Graph(
                id='sales-chart',
                style={'height': '600px'}
            )
        ], style={
            'backgroundColor': 'white',
            'padding': '20px',
            'borderRadius': '10px',
            'boxShadow': '0 4px 12px rgba(0,0,0,0.15)',
            'maxWidth': '1200px',
            'margin': '0 auto'
        })
    ]
)


# Callback to update the chart based on region selection
@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    # Filter data based on selected region
    if selected_region == 'all':
        filtered_df = df.copy()
    else:
        filtered_df = df[df['region'] == selected_region].copy()

    # Group by date and sum sales
    daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()

    # Create the line chart
    fig = px.line(
        daily_sales,
        x='date',
        y='sales',
        title=f'Pink Morsel Sales Over Time - {selected_region.title()}',
        labels={'date': 'Date', 'sales': 'Sales ($)'},
        markers=True
    )

    # Customize the chart appearance
    fig.update_traces(
        line_color='#FF1493',
        line_width=3,
        marker=dict(size=6, color='#FF69B4')
    )

    # Add a vertical line at January 15, 2021
    fig.add_vline(
        x=pd.Timestamp('2021-01-15').timestamp() * 1000,
        line_dash="dash",
        line_color="red",
        line_width=2,
        annotation_text="Price Increase",
        annotation_position="top"
    )

    # Update layout for better appearance
    fig.update_layout(
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='white',
        font=dict(family="Arial, sans-serif", size=12, color="#333"),
        title_font=dict(size=24, color='#FF1493', family="Arial"),
        hovermode='x unified',
        hoverlabel=dict(bgcolor="white", font_size=14),
        xaxis=dict(
            showgrid=True,
            gridcolor='#e0e0e0',
            showline=True,
            linecolor='#333'
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='#e0e0e0',
            showline=True,
            linecolor='#333'
        )
    )

    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)