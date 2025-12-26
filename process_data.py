import pandas as pd
import os

# List of CSV files to process
csv_files = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

# List to store processed dataframes
processed_dfs = []

# Process each CSV file
for file in csv_files:
    # Read the CSV file
    df = pd.read_csv(file)

    # Filter for only Pink Morsels
    df = df[df['product'] == 'pink morsel']

    # Create sales column (quantity * price)
    df['sales'] = df['quantity'] * df['price']

    # Keep only the required columns
    df = df[['sales', 'date', 'region']]

    # Add to our list
    processed_dfs.append(df)

# Combine all dataframes
final_df = pd.concat(processed_dfs, ignore_index=True)

# Save to output file
final_df.to_csv('output.csv', index=False)

print("Data processing complete!")
print(f"Total rows in output: {len(final_df)}")
print(f"Output saved to: output.csv")