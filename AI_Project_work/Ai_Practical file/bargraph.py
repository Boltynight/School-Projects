# Importing the required libraries
import matplotlib.pyplot as mplot

# Providing the dataset
movie_genres = ["Sci-Fi", "Horror", "Animation", "Comedy", "Romance", "Action", "Documentary", "Drama", "Thriller", "Fantasy"]
preferences = [450, 200, 200, 900, 350, 1200, 200, 800, 600, 150]

# Creating a blank graph
tx, ty = mplot.subplots()

# Creating the bar graph to show the Poplularity of Movie Genres
bars = mplot.bar(movie_genres, preferences, color="skyblue")

# Labeling each bar with its score
for b in bars:
    height = b.get_height()
    ty.annotate(str(height), xy=(b.get_x() + b.get_width() / 2, height), xytext=(0, 3),
                textcoords="offset points", ha="center", va="bottom")

# Adding the apt labels and the title
mplot.xlabel("Movie Genres")
mplot.ylabel("Preferences")
mplot.title("Poplularity of Movie Genres")

# Adding lines in the graph for better visualization
mplot.grid(axis="y", linestyle="dotted", alpha= 1)
mplot.xticks(rotation=45)
mplot.yticks(range(0, 1301, 100))

# Displaying  the legend
mplot.legend()

# Showing the graph
mplot.show()