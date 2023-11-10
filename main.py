import plotly.subplots as sp
import numpy as np
import plotly.graph_objects as go
# Generate random noise for x and y
num_plots = 20
num_points_per_plot = 100

# Create a subplot with 4 rows and 5 columns
fig = sp.make_subplots(rows=4, cols=5, subplot_titles=[f"Plot {i+1}" for i in range(num_plots)])

for i in range(num_plots):
    noise_x = np.random.rand(num_points_per_plot)
    noise_y = np.random.rand(num_points_per_plot)

    # Create a scatter plot and add it to the subplot
    scatter = go.Scatter(x=noise_x, y=noise_y, mode='markers', name=f'Plot {i+1}')
    fig.add_trace(scatter, row=(i // 5) + 1, col=(i % 5) + 1)

# Update layout
fig.update_layout(title_text="Multiple Scatter Plots", showlegend=False)

# Save the subplot as an HTML file
fig.write_html("index.html")

