# AIM:
# To perform data aggregation and apply statistical functions
# in Tableau for better data analysis.

# ALGORITHM:
# 1. Open Tableau Public.
# 2. Connect to the dataset.
# 3. Drag required fields into rows and columns.
# 4. Apply aggregation functions.
# 5. Use statistical measures.
# 6. Analyze the results and save the workbook.

# PROCEDURE:
# 1. Create a file named sales_data.csv.
# 2. Enter the sales dataset given below.
# 3. Run the Python program.
# 4. Observe the total, average, minimum, maximum,
#    and category-wise sales.

import pandas as pd

# Load dataset
data = pd.read_csv("sales_data.csv")

# Total Sales
print("Total Sales:", data["Sales"].sum())

# Average Sales
print("Average Sales:", data["Sales"].mean())

# Minimum Sales
print("Minimum Sales:", data["Sales"].min())

# Maximum Sales
print("Maximum Sales:", data["Sales"].max())

# Group by Category
print("\nSales by Category:")
print(data.groupby("Category")["Sales"].sum())
