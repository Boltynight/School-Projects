# Importing required libraries
import random
import matplotlib.pyplot as mplot

# Creating the empty lists: age and TV hours
age = []
tv_hours = []

# Generate and adding the data to the lists
for i in range(13, 50):
    age.append(i)
    tv_hours.append(random.randint(0, 24))

# Creating the scatter plot
mplot.scatter(age, tv_hours, label="TV Hours vs. Age", color="b", marker="o")

# Adding the apt labels and title
mplot.xlabel("Age")
mplot.ylabel("TV Hours")
mplot.title("TV Hours vs. Age")

# Displaying the legend
mplot.legend()

# Showing the plot
mplot.show()