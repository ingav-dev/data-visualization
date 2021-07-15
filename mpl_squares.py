import matplotlib.pyplot as plt

input_values = range(1, 1001)
squares = [x**2 for x in input_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues, s=10)

#ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1100, 0, 1100000])


plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()