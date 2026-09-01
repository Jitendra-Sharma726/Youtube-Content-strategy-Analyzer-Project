import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Headless mode for saving files
import matplotlib.pyplot as plt

# 1. Load Dataset
def load_data():
    """
    Load and return the YouTube dataset.
    """
    path = "youtube.csv" 
    df = pd.read_csv(path)
    
    print("Dataset Preview:")
    print(df.head())
    return df


# 2. Scatter Plot: Views vs Likes
def plot_scatter(df):
    """
    Create a scatter plot comparing Views vs Likes.
    Marker size proportional to comment count + slight transparency.
    """

    plt.figure(figsize=(10, 6)) 

    plt.scatter(
        df["views"],
        df["likes"],

        # Marker size based on comment count
        s=df["comment_count"] * 0.3, 

        color="purple",
        alpha=0.5,     
        edgecolors="black"
    )

    plt.title("Views vs Likes (Size = Comment Count)")
    plt.xlabel("Views")
    plt.ylabel("Likes")
    plt.grid(True, alpha=0.5)

    # Set margins slightly wider than data range
    plt.xlim(0, df["views"].max() * 1.1)
    plt.ylim(0, df["likes"].max() * 1.1)

    plt.savefig("scatter_plot.png")
    print("Chart saved: scatter_plot.png")


# 3. Side-by-Side Bar Chart
def bar_chart_side_by_side(df):
    """
    Compare Likes and Comments per video using side-by-side bars.
    """
    titles = df["title"]
    likes = df["likes"]
    comments = df["comment_count"]

    # X-axis locations for the groups
    x = np.arange(len(titles)) 

    # Width of the bars
    width = 0.35 

    plt.figure(figsize=(12, 6))

    # Plotting two bars side-by-side
    plt.bar(x - width/2, likes, width, label="Likes", color="skyblue")
    plt.bar(x + width/2, comments, width, label="Comments", color="orange")

    plt.title("Engagement Analysis: Likes vs Comments")
    plt.xlabel("Video Title")
    plt.ylabel("Count")
    
    # Custom X-axis labels rotated for readability
    plt.xticks(x, titles, rotation="vertical")
    
    plt.legend()
    plt.grid(axis='y', alpha=0.7)

    # Tight layout prevents labels from being cut off
    plt.tight_layout()

    plt.savefig("bar_chart.png")
    print("Chart saved: bar_chart.png")


if __name__ == "__main__":
    print("YouTube Content Strategy Analyzer...\n")

    # Load Data
    df = load_data()

    if df is not None:
        # Scatter Plot: Views vs Likes 
        plot_scatter(df)

        # Bar Chart: Likes vs Comments
        bar_chart_side_by_side(df)


