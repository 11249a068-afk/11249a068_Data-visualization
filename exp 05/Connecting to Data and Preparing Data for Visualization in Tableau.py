Experiment No. 5: Connecting to Data and Preparing Data for Visualization in Tableau

Aim

To connect Tableau to a data source and prepare the data for creating visualizations.

Algorithm

Open Tableau Public.

Select the required data source.

Import the dataset into Tableau.

Verify the imported data.

Perform basic data preparation.

Save the workbook.

Procedure

Create a CSV file named sales_data.csv.

Import the CSV file using Python and Pandas.

Display the first five rows of the dataset.

Check for missing values.

Remove duplicate records.

Convert the Sales column to numeric format.

Save the cleaned dataset as cleaned_sales_data.csv.

Connect the cleaned dataset to Tableau Public for visualization.

Program

import pandas as pd

# Load dataset
data = pd.read_csv("sales_data.csv")

# Display first 5 rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Remove duplicate records
data = data.drop_duplicates()

# Convert Sales column to numeric
data["Sales"] = pd.to_numeric(data["Sales"])

# Save cleaned dataset
data.to_csv("cleaned_sales_data.csv", index=False)

print("Data prepared successfully.")
