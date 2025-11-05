import matplotlib.pyplot as plt
import numpy as np
import collections
import os

def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    counts = collections.Counter(data)
    categories = list(counts.keys())
    frequencies = list(counts.values())

    fig, ax = plt.subplots(figsize=(6, 4))
    colors = ['#66c2a5', '#fc8d62', '#8da0cb']  
    ax.bar(categories, frequencies, color=colors[:len(categories)], edgecolor='black')
    ax.set_xlabel("Category", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    ax.set_title("Frequency of Categorical Data", fontsize=14)
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    os.makedirs('plots', exist_ok=True)

    output_path = os.path.join('plots', 'task1_bar_chart.png')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close(fig) 
    return fig


# Example data
data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
