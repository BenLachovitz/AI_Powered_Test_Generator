from tkinter import *
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\benzo\PycharmProjects\TryNewUI\Scripts\frame2")

stats_canvas: Canvas
my_scrollbar: Scrollbar


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


np.random.seed(42)


# Function to display the plot in the Tkinter canvas
def display_plot():
    global stats_canvas, my_scrollbar

    data = np.random.randn(10000)

    fig, ax = plt.subplots()  # Create a figure and axis
    ax.hist(data, color='blue')  # Plot the histogram on the axis
    ax.set_title("Skills", fontdict={"fontname": "Comic Sans MS", "size": 16})
    ax.set_xlabel('Value', fontdict={"fontname": "Comic Sans MS", "size": 12})
    ax.set_ylabel('Frequency', fontdict={"fontname": "Comic Sans MS", "size": 12})
    fig.patch.set_alpha(0.0)  # Figure background transparency
    ax.patch.set_alpha(0.0)  # Axes background transparency
    fig.savefig('histogram.png')  # Save the figure as a PNG file
    plt.close(fig)  # Close the figure to free memory

    data = np.random.randn(20000)

    fig, ax = plt.subplots()  # Create a figure and axis
    ax.hist(data, color='blue')  # Plot the histogram on the axis
    ax.set_title("Recent tests", fontdict={"fontname": "Comic Sans MS", "size": 16})
    ax.set_xlabel('Value', fontdict={"fontname": "Comic Sans MS", "size": 12})
    ax.set_ylabel('Frequency', fontdict={"fontname": "Comic Sans MS", "size": 12})
    fig.patch.set_alpha(0.0)  # Figure background transparency
    ax.patch.set_alpha(0.0)  # Axes background transparency
    fig.savefig('histogram2.png')  # Save the figure as a PNG file
    plt.close(fig)  # Close the figure to free memory

    data = np.random.randn(40000)

    fig, ax = plt.subplots()  # Create a figure and axis
    ax.hist(data, color='blue')  # Plot the histogram on the axis
    ax.set_title("Recent tests", fontdict={"fontname": "Comic Sans MS", "size": 16})
    ax.set_xlabel('Value', fontdict={"fontname": "Comic Sans MS", "size": 12})
    ax.set_ylabel('Frequency', fontdict={"fontname": "Comic Sans MS", "size": 12})
    fig.patch.set_alpha(0.0)  # Figure background transparency
    ax.patch.set_alpha(0.0)  # Axes background transparency
    fig.savefig('histogram3.png')  # Save the figure as a PNG file
    plt.close(fig)  # Close the figure to free memory

    stats_canvas.image_image_2 = PhotoImage(
        file="histogram.png")

    stats_canvas.image_image_3 = PhotoImage(
        file="histogram2.png")

    stats_canvas.image_image_4 = PhotoImage(
        file="histogram3.png")

    # stats_canvas.image_image_1 = PhotoImage(
    #     file=relative_to_assets("image_1.png"))
    new_size = (stats_canvas.image_image_2.height() + stats_canvas.image_image_3.height() +
                stats_canvas.image_image_4.height())

    image = Image.open(relative_to_assets("image_1.png"))
    image = image.resize((1440, new_size))
    stats_canvas.pic = ImageTk.PhotoImage(image)
    image_1 = stats_canvas.create_image(
        720.0,
        new_size/3+500/2,
        image=stats_canvas.pic
    )

    graphs_offset = 250
    image_2 = stats_canvas.create_image(
        720.0,
        graphs_offset,
        image=stats_canvas.image_image_2
    )

    graphs_offset += stats_canvas.image_image_2.height()-20

    image_3 = stats_canvas.create_image(
        720.0,
        graphs_offset,
        image=stats_canvas.image_image_3
    )

    graphs_offset += stats_canvas.image_image_3.height()-20

    image_4 = stats_canvas.create_image(
        720.0,
        graphs_offset,
        image=stats_canvas.image_image_4
    )

    stats_canvas.configure(scrollregion=stats_canvas.bbox("all"))


# Function to display histograms in the scrollable canvas
def show_statistics_frame(stats_frame, show_frame):
    global stats_canvas, my_scrollbar

    stats_canvas = Canvas(
        stats_frame,
        bg="#FFFFFF",
        height=886,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    stats_canvas.grid(row=0, column=0, sticky=NSEW)

    # Create a scrollbar

    second_frame = Frame(stats_canvas)
    stats_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    my_scrollbar = Scrollbar(stats_frame, orient=VERTICAL, command=stats_canvas.yview)
    my_scrollbar.grid(row=0, column=0, sticky="nse")

    stats_canvas.configure(yscrollcommand=my_scrollbar.set)
    stats_canvas.bind('<Configure>', lambda e: stats_canvas.configure(scrollregion=stats_canvas.bbox("all")))

    stats_canvas.bind('<MouseWheel>', lambda e: stats_canvas.yview_scroll(-int(e.delta / 120), "units"))
