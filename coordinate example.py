from mpl_toolkits.axisartist import Subplot as AxisArtistSubplot

def plot_graph_with_arrow(self, x_array=[], y_array=[],
               x_axis_name=" ", y_axis_name=" ",
               x_axis_rotation=0, y_axis_rotation=0,
               x_axis_location="center", y_axis_location="center",
               title=" ",
               x_log_axes=False, y_log_axes=False,
               graph_font='DejaVu Sans', math_font="stix",
               comments_x_axis=None, comments_x_coordinates=None,
               comments_drawing=False, comments_drawing_x=[], comments_drawing_y=[], comments_drawing_text=[],
               axis_scientific=False, automatic_scientific=False, scientific_power=1,
               axis_arrow=True, hide_bound=True):
    """
    Plot a scatter plot with axis tick labels in scientific notation.

    Parameters:
    x_array (numpy.ndarray or list): Array of x values.
    y_array (numpy.ndarray or list): Array of y values.
    x_axis_name (str): Name of the x-axis.
    y_axis_name (str): Name of the y-axis.
    title (str): Title of the graph.
    x_log_axes (bool): Whether to use logarithmic scale for the x-axis (default: False).
    y_log_axes (bool): Whether to use logarithmic scale for the y-axis (default: False).
    """

    # Convert lists to numpy arrays if necessary
    x_array = np.array(x_array)
    y_array = np.array(y_array)

    plt.rcParams["font.family"] = graph_font
    plt.rcParams["mathtext.fontset"] = math_font

    # Clear all axes in the figure
    fig = self.MplWidget.canvas.figure
    fig.clear()

    # Create new axisartist axes
    ax = AxisArtistSubplot(fig, 111)
    fig.add_axes(ax)

    # Plot data
    if x_array.size > 0 and y_array.size > 0:
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
    # Set x-axis label with rotation and location
    # Set x-axis label with rotation and location
    # Set x-axis label with rotation and position on the right
    x_label = ax.axis["bottom"].label
    x_label.set_text(x_axis_name)
    x_label.set_rotation(x_axis_rotation)
    x_label.set_position(('right', 0))  # Adjust the position as needed

    # Set y-axis label with rotation and position on the top
    y_label = ax.axis["left"].label
    y_label.set_text(y_axis_name)
    y_label.set_rotation(y_axis_rotation)
    y_label.set_position(('top', 0))  # Adjust the position as needed

    if axis_scientific:
        if automatic_scientific:
            ax.xaxis.set_major_formatter(ticker.FuncFormatter(scientific_formatter))
            ax.yaxis.set_major_formatter(ticker.FuncFormatter(scientific_formatter))
        else:
            ax.xaxis.set_major_formatter(ticker.FuncFormatter(manual_scientific_formatter(scientific_power)))
            ax.yaxis.set_major_formatter(ticker.FuncFormatter(manual_scientific_formatter(scientific_power)))

    if title:
        ax.set_title(title)

    # Add arrows at the ends of each axis
    if axis_arrow:
        ax.axis["right"].set_visible(False)
        ax.axis["top"].set_visible(False)
        ax.axis["left"].set_axisline_style("-|>", size=1.5)
        ax.axis["bottom"].set_axisline_style("-|>", size=1.5)

        # doesnt work
        '''ax.spines[['top', 'right']].set_visible(True)
        ax.spines['top'].set_position(('outward', 10))  
        ax.spines['right'].set_position(('outward', 10))  
        ax.spines[['left', 'bottom']].set_visible(False)'''

    if hide_bound:
        ax.spines[['top', 'right']].set_visible(False)
        if comments_x_coordinates is not None:
            ax2.spines[['top', 'right']].set_visible(False)

    # Draw the canvas
    self.MplWidget.canvas.draw()