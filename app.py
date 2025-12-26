import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Read the processed data
df = pd.read_csv('output.csv')

# Convert date column to datetime for proper sorting
df['date'] = pd.to_datetime(df['date'])

# Sort by date
df = df.sort_values('date')

# Group by date and sum sales (in case there are multiple regions per date)
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Create the line chart
fig = px.line(daily_sales,
              x='date',
              y='sales',
              title='Pink Morsel Sales Over Time',
              labels={'date': 'Date', 'sales': 'Sales ($)'},
              markers=True)

# Add a vertical line at January 15, 2021 to show the price increase
fig.add_vline(x=pd.Timestamp('2021-01-15').timestamp() * 1000,
              line_dash="dash",
              line_color="red",
              annotation_text="Price Increase",
              annotation_position="top")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer",
            style={'textAlign': 'center', 'color': '#503D36', 'fontSize': 40}),

    html.P("Analyzing sales before and after the price increase on January 15, 2021",
           style={'textAlign': 'center', 'fontSize': 16}),

    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)