import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

def plot_heatmap(hist_df, lot):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(np.random.rand(10, 6) * 100, annot=True, cmap="YlOrRd", ax=ax)  # Demo — replace with real freq
    ax.set_title(f"Hot/Cold Heatmap - {lot['name']}")
    return fig

def plot_trends(hist_df):
    return px.line(x=range(len(hist_df)), y=np.random.rand(len(hist_df)), title="Number Trends Over Draws")
