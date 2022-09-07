#---------------------------------------------------------------------------------------------------------------#
#                                       VISUALIZATION OF DATA                                                   #
#---------------------------------------------------------------------------------------------------------------#
# Bar Chats
import matplotlib.pyplot as plt
from collections import Counter
# Data we are plotting
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
# Bar plot is made using plt.bar() command
plt.bar([i for i in range(len(movies))], num_oscars, align="center")
plt.title("My Favorite movies")
plt.ylabel("# of academy awards")
plt.xticks([i for i in range(len(movies))], movies)
plt.show()
plt.clf()

# Second Plot
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
# Create xticks that run from 0 to 90 where 100 is included in 90
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],  # Shifts bars right by 5
        histogram.values(),
        10,
        edgecolor=(0,0,0))
    
plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of students")
plt.title("Distribution of Exam 1 Grades")
plt.show()