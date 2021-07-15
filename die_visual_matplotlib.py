import matplotlib.pyplot as plt

from die import Die 

# Create a D6.
die_1 = Die()
die_2 = Die()

#Make some rolls and store the results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Analyze the results.

max_result = die_1.num_sides + die_2.num_sides 
frequencies = [results.count(value) for value in range(3, max_result+1)]

# Visualize the results 
x_values = range(3, max_result+1)
data = plt.bar(x=x_values, height=frequencies)
plt.show()