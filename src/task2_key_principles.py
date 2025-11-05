import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=data, x='x', y='y', ax=ax, color='blue', s=50)
    ax.set_xlabel("X values", fontsize=11)
    ax.set_ylabel("Y values", fontsize=11)
    ax.set_title("Scatter Plot of X vs Y", fontsize=13)
    ax.grid(True)
    return fig



# Example data
data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})
create_scatter_plot(data)
