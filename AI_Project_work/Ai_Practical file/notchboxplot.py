# Importing the required libraries
import matplotlib.pyplot as mplot

# Providing the dataset
marks = [75, 82, 88, 92, 65, 78, 90, 85, 70, 92, 76, 80, 73, 89, 94, 68, 75, 82, 88, 85, 91, 79, 87, 83, 71, 72]

# Creating the notch boxplot
mplot.boxplot(marks , notch=True )

# Adding the apt labels and the title
mplot.xlabel("Marks of the Student")
mplot.ylabel("Frequency Distribution of marks")
mplot.title("Notch Boxplot of Marks Distribution")

# Showing the plot
mplot.show()