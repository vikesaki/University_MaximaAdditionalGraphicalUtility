import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.ticker import ScalarFormatter

# font for the graph
plt.rcParams["font.family"] = "Times New Roman"


def plot_graph(self, x_array=[], y_array=[],
               x_axis_name=" ", y_axis_name=" ",
               x_axis_rotation=0, y_axis_rotation=0,
               x_axis_location="center", y_axis_location="center",
               title=" ",
               x_log_axes=False, y_log_axes=False,
               graph_font='DejaVu Sans', math_font="stix",
               comments_x_axis=None, comments_x_coordinates=None,
               comments_drawing=False, comments_drawing_x=[], comments_drawing_y=[], comments_drawing_text=[],
               axis_scientific=False, automatic_scientific=False, scientific_power=1):
    """
    Plot a scatter plot with axis tick labels in scientific notation.

    Parameters:
    x_array (numpy.ndarray): Array of x values.
    y_array (numpy.ndarray): Array of y values.
    x_axis_name (str): Name of the x-axis.
    y_axis_name (str): Name of the y-axis.
    title (str): Title of the graph.
    x_log_axes (bool): Whether to use logarithmic scale for the x-axis (default: False).
    y_log_axes (bool): Whether to use logarithmic scale for the y-axis (default: False).
    """

    plt.rcParams["font.family"] = graph_font
    plt.rcParams["mathtext.fontset"] = math_font

    # Clear all axes in the figure
    fig = self.MplWidget.canvas.figure
    fig.clear()

    # Create new axes
    ax = fig.add_subplot(111)

    # Plot data
    ax.plot(x_array, y_array, linestyle='-', color='r', label='Line plot')

    # Comments by x-axis
    if comments_x_coordinates is not None:
        # Draw vertical dotted lines for each x-coordinate
        for xi in comments_x_coordinates:
            ax.axvline(xi, color='gray', linestyle='--', linewidth=0.5)

        # Create a second axes for the top x-axis
        ax2 = ax.twiny()
        # Set the ticks and labels for the top x-axis
        ax2.set_xlim(ax.get_xlim())
        # Set custom tick locations and labels for the new y-axis
        ax2.set_xticks(comments_x_coordinates)
        ax2.set_xticklabels(comments_x_axis)  # Set custom tick labels as point names
        # Hide ticks and tick labels of the top x-axis
        ax2.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

    # Draw comments on the graph
    if comments_drawing:
        for x, y, text in zip(comments_drawing_x, comments_drawing_y, comments_drawing_text):
            ax.annotate(text, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    # Set log scale for axes if specified
    if x_log_axes:
        ax.set_xscale('log')
    if y_log_axes:
        ax.set_yscale('log')

    # Set axis labels and title
    ax.set_xlabel(x_axis_name, rotation=x_axis_rotation, loc=x_axis_location)
    ax.set_ylabel(y_axis_name, rotation=y_axis_rotation, loc=y_axis_location)

    if axis_scientific:
        if automatic_scientific :
            ax.xaxis.set_major_formatter(ticker.FuncFormatter(scientific_formatter))
            ax.yaxis.set_major_formatter(ticker.FuncFormatter(scientific_formatter))
        else:
            ax.xaxis.set_major_formatter(ticker.FuncFormatter(manual_scientific_formatter(scientific_power)))
            ax.yaxis.set_major_formatter(ticker.FuncFormatter(manual_scientific_formatter(scientific_power)))

    if title:
        ax.set_title(title)

    # Draw the canvas
    fig.tight_layout()
    self.MplWidget.canvas.draw()


def scientific_formatter(x, pos):
    if x == 0:
        return '0'
    exponent = int(np.floor(np.log10(np.abs(x))))
    coefficient = x / (10 ** exponent)
    return f'{coefficient:.1f}x$10^{{{exponent}}}$'

def manual_scientific_formatter(power):
    def formatter(x, pos):
        return f'{x / 10**power:.1f}x$10^{power}$'
    return formatter
