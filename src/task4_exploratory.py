import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    print("Descriptive Statistics:\n", df.describe())
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=df, ax=ax1)
    ax1.set_title("Boxplot for Outlier Detection")
    plt.close(fig1)
    corr = df.corr(numeric_only=True)
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
    ax2.set_title("Correlation Heatmap")
    plt.close(fig2)
    sns.pairplot(df)
    plt.close()
    return None


# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})
perform_eda(df)
