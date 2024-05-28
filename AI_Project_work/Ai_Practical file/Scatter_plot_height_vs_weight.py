# Importing required libraries
import random
import matplotlib.pyplot as mplot

# Creating the lists: weight and height
# and poroviding the dataset
weight = [52.21,53.12,54.48,55.84,57.2,58.57,59.93,61.29,63.11,64.47,66.28,68.1,69.92,72.19,74.46]
height = [1.47,1.5,1.52,1.55,1.57,1.6,1.63,1.65,1.68,1.7,1.73,1.75,1.78,1.8,1.83,]

# Creating the scatter plot
mplot.scatter(weight, height, label="Height vs. Weight", color="g", marker="o")

# Adding the apt labels and title
mplot.xlabel("Weight")
mplot.ylabel("Height")
mplot.title("Height vs. Weight")

# Displaying the legend
mplot.legend()

# Showing the plot
mplot.show()
