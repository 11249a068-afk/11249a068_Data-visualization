# Experiment No. 10: Storytelling in Tableau

# Aim:
To create a story in Tableau by arranging multiple visualizations as a sequence of insights that explain the data step by step.

# Description
Data storytelling is a method of communicating analytical results through a sequence of visualizations accompanied by explanations.
In Tableau, a story consists of multiple story points, with each point containing a worksheet or dashboard and a suitable caption.
By arranging these points in a meaningful order, users can present their findings progressively and help viewers understand the analysis.
This approach makes complex information easier to interpret, including for users who do not have a technical background.

# Uses:
- Presenting data analysis results in an understandable manner.
- Describing trends and patterns in a sequence.
- Organizing multiple charts into a meaningful presentation.
- Supporting business reports and presentations.
- Sharing analytical findings with non-technical audiences.

# Algorithm
1. Start Tableau Public.
2. Connect to the required dataset (Excel/CSV).
3. Create the individual charts, each on its own worksheet.
4. Create a dashboard if required.
5. Click the New Story tab at the bottom.
6. Add story points by dragging worksheets or dashboards onto the story canvas.
7. Arrange the story points in a logical sequence.
8. Add a caption to each story point to explain the insight.
9. Review the story, then save or publish it.

# Program

import pandas as pd
import matplotlib.pyplot as plt
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
print("Story Created: Category performance, "
"regional distribution, and sales trends analyzed.")

# Libraries Used
- Pandas: Used to load, organize, group, and summarize the dataset.
- Matplotlib: Used to generate the bar chart, pie chart, and scatter plot.
- Tableau: Used to arrange worksheets and dashboards into story points and present insights in sequence.

# Sample Output
The program displays three visualizations representing different stages of the analysis:

1. Story 1: A bar chart comparing sales across categories.
2. Story 2: A pie chart illustrating the sales contribution of different regions.
3. Story 3: A scatter plot representing the relationship between quantity and sales.

Together, these views help explain category performance, regional distribution, and the relationship between sales and quantity.

# Result
Thus, the concept of storytelling in Tableau was studied, and multiple visualizations were generated to explain data insights in a logical sequence.
