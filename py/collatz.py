from matplotlib.patches import ConnectionStyle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx


def user_values():
    while True:
        try:
            num = int(input("Starting value: "))
            if num < 0:
                print("Please enter a value greater than 0!")
            else:
                break
        except ValueError:
            print("Please enter a valid integer!")
    return num


def collatz_rule(n):
    collatz_sequence = [
        n,
    ]
    while n > 1:
        if n % 2 == 0:
            n //= 2
            collatz_sequence.append(n)
        else:
            n *= 3
            n += 1
            collatz_sequence.append(n)
    print(" -> ".join(str(n) for n in collatz_sequence))
    print(f"Steps: {len(collatz_sequence) - 1}")
    return collatz_sequence


def draw_collatz_network(sequence):
    G = nx.DiGraph()
    for i in range(len(sequence) - 1):
        G.add_edge(sequence[i], sequence[i + 1])
    vertical_spacing = 1.5
    pos = {n: (0, -i * vertical_spacing) for i, n in enumerate(sequence)}
    plt.figure(figsize=(4, len(sequence) * 0.6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        arrows=True,
        node_color="lightblue",
        edge_color="gray",
        arrowsize=20,
        node_size=1000,
        font_size=10,
        connectionstyle="arc3,rad=0.0",
    )
    plt.title("Collatz Sequence Graph")
    plt.axis("off")
    plt.show()


def get_dataframe(sequence):
    df = pd.DataFrame({"Step": list(range(len(sequence))), "Value": sequence})
    return df


def draw_collatz_plot_px(df):
    start_value = df["Value"].iloc[0]
    fig = px.line(
        df,
        x="Step",
        y="Value",
        title=(f"Collatz Sequence for value {start_value}"),
        log_y=True,
        markers=True,
    )
    fig.update_traces(line_color="blue", marker=dict(color="red"))
    fig.show()


def draw_collatz_plot_go(df):
    start_value = df["Value"].iloc[0]
    hover_text = [
        f"Step {step}<br>Value {value}" for step, value in zip(df["Step"], df["Value"])
    ]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["Step"],
            y=df["Value"],
            mode="lines+markers",
            line=dict(color="gray"),
            marker=dict(
                color=df["Value"],
                colorscale="plasma",
                size=10,
                colorbar=dict(title="Value"),
            ),
            name=("Collatz Sequence"),
            hovertext=hover_text,
            hoverinfo="text",
        )
    )
    fig.update_layout(
        title=(f"Collatz Sequence for value {start_value}"), yaxis_type="log"
    )
    fig.show()


collatz_start = user_values()
collatz_sequence = collatz_rule(collatz_start)
dataframe = get_dataframe(collatz_sequence)
draw_collatz_network(collatz_sequence)
draw_collatz_plot_px(dataframe)
draw_collatz_plot_go(dataframe)
