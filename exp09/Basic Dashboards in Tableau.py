## Experiment No. 9: Basic Dashboards in Tableau//

## Aim

To create basic dashboards in Tableau by combining multiple visualizations.

## Algorithm

1. Open Tableau Public.
2. Connect to the dataset.
3. Create multiple worksheets.
4. Open the Dashboard tab.
5. Drag sheets into the dashboard.
6. Add filters and interactive elements.
7. Arrange the layout properly.
8. Save the dashboard.

## Procedure

1. Import `sales_data.csv` using Pandas.
2. Group the data by Category and create a bar chart.
3. Group the data by Region and create a pie chart.
4. Create a line chart showing Sales versus Quantity.
5. Combine the visualizations in Tableau to create an interactive dashboard.

## Program

import pandas as pd
import matplotlib.pyplot as plt
import os

# Create sample data if the CSV file does not exist
if not os.path.exists("sales_data.csv"):
    sample_data = pd.DataFrame({
        "Category": ["Furniture", "Office Supplies", "Technology", "Furniture", "Office Supplies", "Technology"],
        "Region": ["West", "East", "West", "East", "Central", "South"],
        "Sales": [250, 150, 500, 300, 50, 600],
        "Quantity": [3, 2, 5, 4, 1, 6]
    })
    sample_data.to_csv("sales_data.csv", index=False)

data = pd.read_csv("sales_data.csv")

# STORY STEP 1: Category performance
category_sales = data.groupby("Category")["Sales"].sum()
category_sales.plot(kind="bar")
plt.title("Story 1: Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

# STORY STEP 2: Regional contribution
region_sales = data.groupby("Region")["Sales"].sum()
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Story 2: Sales by Region")
plt.ylabel("")
plt.show()

# STORY STEP 3: Quantity and sales relationship
plt.scatter(data["Quantity"], data["Sales"])
plt.title("Story 3: Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()

print("Story Created: Category performance, regional distribution, and sales trends analyzed.")


