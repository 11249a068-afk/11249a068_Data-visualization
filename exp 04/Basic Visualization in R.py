# Experiment No. 4: Basic Visualization in R

## Aim
To create a basic line graph using R programming.

## Algorithm
1. Create vectors for X and Y values.
2. Use the `plot()` function to draw the graph.
3. Add the graph title and axis labels.
4. Execute the program.
5. Observe the output.

## Procedure
1. Open R or RStudio.
2. Create vectors for X and Y values.
3. Use the `plot()` function with line and point options.
4. Add the title and axis labels.
5. Run the program and observe the line graph.

## Program

import matplotlib.pyplot as plt
x <- c(1, 2, 3, 4, 5)
y <- c(10, 15, 12, 18, 20)

plot(x, y,
     type = "o",
     col = "blue",
     main = "Line Graph",
     xlab = "X Values",
     ylab = "Y Values")
