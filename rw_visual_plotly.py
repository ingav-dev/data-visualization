import plotly.graph_objects as go

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt = go.Figure(data=go.Scatter(x=rw.x_values, y=rw.y_values))

plt.show()
