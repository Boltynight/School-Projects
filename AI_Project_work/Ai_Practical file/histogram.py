# Importing the required libraries
import matplotlib.pyplot as mplot

# Providing the dataset
weights_kg = [63, 71, 67, 80, 75, 72, 79, 85, 78, 90, 95, 70, 65, 74, 88, 82, 69, 81, 77, 72,68, 73, 76, 89, 84, 91, 73, 79, 86, 92, 97, 75, 83, 76, 74, 79, 80, 70, 78, 73,68, 81, 86, 90, 75, 83, 77, 70, 65, 71, 68, 75, 82, 84, 89, 71, 79, 82, 87, 70,73, 75, 81, 79, 78, 84, 90, 86, 72, 76, 73, 77, 85, 88, 68, 75, 70, 73, 79, 82,74, 81, 84, 88, 90, 70, 77, 75, 68, 72, 79, 82, 85, 71, 73, 79, 87, 88, 69, 76,80, 85, 77, 70, 71, 83, 86, 82, 75, 74]
students_num = 500

# Creating the histogram
mplot.hist(weights_kg, bins=10, edgecolor='k', alpha=1, label="Weight Distribution")

# Adding the apt labels and the title
mplot.xlabel("Weight")
mplot.ylabel("Number of Students")
mplot.title("Weight Distribution of Students")

# Displaying the legend
mplot.legend()

# Show the plot
mplot.show()
