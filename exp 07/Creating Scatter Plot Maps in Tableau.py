                                      Creating Scatter Plot Maps in Tableau.py


Aim:
To create scatter plots and map-based visualizations using Tableau.
Description:
A scatter plot displays the relationship between two numerical variables. Tableau can also use
geographical fields such as city, state, country and region to create map-based visualizations.
Uses:
• Finding relationships between variables.
• Identifying clusters and unusual values.
• Comparing sales and quantity.
• Displaying geographical information.
• Analyzing regional business performance.
Algorithm:
1. Open Tableau Public.
2. Connect to the dataset.
3. Identify geographical and numerical fields.
4. Drag fields to Rows and Columns.
5. Select Scatter Plot from Show Me.
6. Add map features if geographical data is present.
7. Analyze and save the visualization.

  Program: 
import pandas as pd
import matplotlib.pyplot as plt
import os

# Create a fallback dataset if the file is missing
if not os.path.exists("sales_map_data.csv"):
    fallback_data = pd.DataFrame({
        "Sales": [250, 150, 500, 300, 50, 600],
        "Quantity": [3, 2, 5, 4, 1, 6]
    })
    fallback_data.to_csv("sales_map_data.csv", index=False)

# Load dataset
data = pd.read_csv("sales_map_data.csv")

# Scatter plot
plt.scatter(data["Sales"], data["Quantity"])
plt.xlabel("Sales")
plt.ylabel("Quantity")
plt.title("Scatter Plot: Sales vs Quantity")
plt.show()

