import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns
import pandas as pd


def user_values():
    available = list(distributions.keys())
    while True:
        try:
            size = int(input("Size: "))
            if size < 0:
                print("Please enter a value greater than 0!")
            else:
                break
        except ValueError:
            print("Please give a valid integer!")
    print(
        "Available distributions:",
        ", ".join(dist.capitalize() for dist in available),
        "or all.",
    )
    while True:
        try:
            user_input = input("Enter distributions (comma separated): ").lower()
            if user_input in ["a", "all"]:
                dist_list = available
                break
            dist_list = [dist.strip() for dist in user_input.split(",")]
            for dist in dist_list:
                if dist not in distributions:
                    raise ValueError(f"{dist} is not a valid distribution!")
            break
        except ValueError as e:
            print(f"Error {e}")
    return size, dist_list


def get_distributions(n):
    selected_data = {
        dist: distributions[dist](n)
        for dist in user_distributions
        if dist in distributions
    }
    df = pd.DataFrame(selected_data)
    long = pd.melt(df, var_name="distribution", value_name="value")
    return long


def plot_distributions(df, colors):
    sns.displot(
        data=df,
        kind="kde",
        x="value",
        hue="distribution",
        palette=colors,
        fill=True,
        height=6,
        aspect=1.5,
    )
    plt.show()


distributions = {
    "normal": lambda num: random.normal(loc=1, scale=2, size=num),
    "binomial": lambda num: random.binomial(n=10, p=0.5, size=num),
    "poisson": lambda num: random.poisson(lam=2, size=num),
    "uniform": lambda num: random.uniform(low=1, high=1, size=num),
    "logistic": lambda num: random.logistic(loc=1, scale=2, size=num),
    # "multinomial": lambda num: random.multinomial(n=6, pvals=[1 / 6] * 6, size=num),
    "exponential": lambda num: random.exponential(scale=2, size=num),
    "chisquare": lambda num: random.chisquare(df=4, size=num),
    "rayleigh": lambda num: random.rayleigh(scale=2, size=num),
    "pareto": lambda num: random.pareto(a=2, size=num),
    "zipf": lambda num: random.zipf(a=2, size=num),
}

number, user_distributions = user_values()
df_long = get_distributions(number)
color_palette = sns.color_palette("bright")
plot_distributions(df_long, color_palette)
