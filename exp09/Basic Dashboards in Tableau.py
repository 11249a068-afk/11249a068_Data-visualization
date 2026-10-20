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

# Load dataset
data = pd.read_csv("sales_data.csv")

# Bar chart
data.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.show()

# Pie chart
data.groupby("Region")["Sales"].sum().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.title("Sales by Region")
plt.show()

# Line chart
plt.plot(data["Quantity"], data["Sales"])
plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()
```


