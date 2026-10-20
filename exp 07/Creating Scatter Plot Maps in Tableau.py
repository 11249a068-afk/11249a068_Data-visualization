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
1 import pandas as pd
2 import matplotlib . pyplot as plt
3
4 # Load dataset
5 data = pd . read_csv (" sales_map_data .csv")
7 # Scatter plot
8 plt . scatter ( data [" Sales "] , data [" Quantity "])
9 plt . xlabel (" Sales ")
10 plt . ylabel (" Quantity ")
11 plt . title (" Scatter Plot : Sales vs Quantity ")
12 plt . show ()

