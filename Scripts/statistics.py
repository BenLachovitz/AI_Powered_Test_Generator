from tkinter import *
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\benzo\PycharmProjects\TryNewUI\Scripts\frame2")

stats_canvas: Canvas


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


np.random.seed(42)


# Function to display the plot in the Tkinter canvas
def display_plot():
    global stats_canvas

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

    graphs_offset = 250

    stats_canvas.image_image_2 = PhotoImage(
        file="histogram.png")
    image_2 = stats_canvas.create_image(
        720.0,
        graphs_offset,
        image=stats_canvas.image_image_2
    )

    graphs_offset += stats_canvas.image_image_2.height()-20

    stats_canvas.image_image_3 = PhotoImage(
        file="histogram2.png")
    image_3 = stats_canvas.create_image(
        720.0,
        graphs_offset,
        image=stats_canvas.image_image_3
    )


# Function to display histograms in the scrollable canvas
def show_statistics_frame(stats_frame, show_frame):
    global stats_canvas

    stats_canvas = Canvas(
        stats_frame,
        bg="#FFFFFF",
        height=886,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    stats_canvas.image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = stats_canvas.create_image(
        720.0,
        512.0,
        image=stats_canvas.image_image_1
    )

    # stats_canvas.button_image_1 = PhotoImage(
    #     file=relative_to_assets("button_1.png"))
    # button_1 = Button(
    #     stats_frame,
    #     image=stats_canvas.button_image_1,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     activebackground="#7DABB2",
    #     relief="flat"
    # )
    # button_1.place(
    #     x=905.0,
    #     y=681.0,
    #     width=198.0,
    #     height=51.0
    # )

    stats_canvas.grid(row=0, column=0, sticky=NSEW)

    # Create a scrollbar
    my_scrollbar = Scrollbar(stats_frame, orient=VERTICAL, command=stats_canvas.yview)
    my_scrollbar.grid(row=0, column=0, sticky="nse")

    stats_canvas.configure(yscrollcommand=my_scrollbar.set)
    stats_canvas.bind('<Configure>', lambda e: stats_canvas.configure(scrollregion=stats_canvas.bbox("all")))

    second_frame = Frame(stats_canvas)

    stats_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    stats_canvas.bind('<MouseWheel>', lambda e: stats_canvas.yview_scroll(-int(e.delta / 120), "units"))
