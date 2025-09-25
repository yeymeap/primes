import plotly.graph_objects as go
import numpy as np


def user_values():
    while True:
        try:
            upper = int(input("Upper limit: "))
            if upper < 0:
                print("Please enter a value greater than 0!")
            else:
                break
        except ValueError:
            print("Please enter a valid integer!")
    return upper


def is_prime(n):  # checks if input number is prime based on 6k +- 1 formula
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:  # checks up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def plot_colors(n):
    x_value = list(range(0, n + 1))
    y_value = list(range(len(x_value)))
    colors = []
    hover_texts = []
    for x in x_value:
        if is_prime(x):
            if is_prime(x - 2) or is_prime(x + 2):
                colors.append("green")
                hover_texts.append(f"Value: {x}<br>Twin Prime")
            else:
                colors.append("blue")
                hover_texts.append(f"Value: {x}<br>Prime")
        else:
            colors.append("gray")
            hover_texts.append(f"Value: {x}<br>Non-Prime")
    return x_value, y_value, colors, hover_texts


def get_colors(num):
    if is_prime(num):
        if is_prime(num - 2) or is_prime(num + 2):
            return "green"
        else:
            return "blue"
    else:
        return "gray"


upper_limit = user_values()

# bar graph
x_vals, y_vals, color_list, hover_text = plot_colors(upper_limit)

fig = go.Figure(
    data=[
        go.Bar(
            x=x_vals,
            y=y_vals,
            marker_color=color_list,
            hovertext=hover_text,
            hoverinfo="text",
        )
    ]
)
fig.update_layout(
    title=f"Prime and Twin Prime classification to {upper_limit}",
    xaxis_title="Numbers",
    yaxis_title="Numbers",
)
fig.show()

# 2D grid
grid_size = upper_limit
max_num = grid_size * grid_size
numbers = np.arange(1, max_num + 1).reshape((grid_size, grid_size))
colors = np.vectorize(get_colors)(numbers)
x_coords, y_coords = np.meshgrid(range(grid_size), range(grid_size))
y_coords = grid_size - 1 - y_coords
x_flat = x_coords.flatten()
y_flat = y_coords.flatten()
colors_flat = colors.flatten()
numbers_flat = numbers.flatten()

fig = go.Figure(
    go.Scatter(
        x=x_flat,
        y=y_flat,
        mode="markers",
        marker=dict(color=colors_flat, size=10, line=dict(width=0)),
        text=[f"{num}" for num in numbers_flat],
        hoverinfo="text",
    )
)

fig.update_layout(
    title=f"2D Grid of Numbers up to {max_num} (Blue = Prime, Green = Twin Prime)",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, scaleanchor="x"),
    plot_bgcolor="white",
)

fig.show()
