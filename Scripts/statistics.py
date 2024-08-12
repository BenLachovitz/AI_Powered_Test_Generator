from tkinter import *
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import MySQLdb
import os
from dotenv import load_dotenv
from constants import Constants
import random
import colorsys

load_dotenv()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"frame2")

stats_canvas: Canvas
my_scrollbar: Scrollbar


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


np.random.seed(42)


# Function to display the plot in the Tkinter canvas
def display_plot():
    global stats_canvas, my_scrollbar

    connection = MySQLdb.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        passwd=os.getenv("PASSWD"),
        db=os.getenv("DB")
    )

    cursor = connection.cursor()
    cursor.execute("select "
                   "skills.GraphingEquationsFunctions, "
                   "skills.SolvingEquations, "
                   "skills.UnderstandingApplyingProperties, "
                   "skills.UsingAlgebraicTechniques, "
                   "skills.AnalyzingInterpretingData, "
                   "skills.ApplyingTheoremsFormulas, "
                   "skills.UnderstandingConcepts, "
                   "skills.SolvingRWProblems, "
                   "skills.UsingCalculatorsSoftware, "
                   "skills.ProvingTheoremsConcepts "
                   "from sgdb.studentskills as skills "
                   "where studentID = %s;", (Constants.studentID,))

    fetchedAll = cursor.fetchall()

    if fetchedAll:
        field_names = [i[0] for i in cursor.description]
        values = [i for i in fetchedAll[0]]
        colors = []
        hue = random.random()
        saturation_range = (0.5, 1.0)
        brightness_range = (0.5, 1.0)
        for _ in range(len(field_names)):
            saturation = random.uniform(*saturation_range)
            brightness = random.uniform(*brightness_range)
            rgb = colorsys.hsv_to_rgb(hue, saturation, brightness)
            hex_color = '#{:02X}{:02X}{:02X}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
            colors.append(hex_color)

        fig, ax = plt.subplots(figsize=(10, 5))  # Create a figure and axis
        plt.tight_layout()
        plt.subplots_adjust(top=0.9, left=0.25)
        ax.barh(field_names, values, color=colors)  # Plot the histogram on the axis
        plt.title("Skills", fontdict={"fontname": "Comic Sans MS", "size": 16})
        fig.patch.set_alpha(0.0)  # Figure background transparency
        ax.patch.set_alpha(0.0)  # Axes background transparency
        fig.savefig('histogram.png')  # Save the figure as a PNG file
        plt.close(fig)  # Close the figure to free memory
    else:
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

    cursor.execute("select "
                   "marks.AlgebraLinearEquations, "
                   "marks.AlgebraQuadraticEquations, "
                   "marks.AlgebraPolynomials, "
                   "marks.AlgebraExponentsAndLogarithms, "
                   "marks.GeometryCoordinateGeometry, "
                   "marks.GeometryTrigonometry, "
                   "marks.GeometryCircles, "
                   "marks.GeometryVectors, "
                   "marks.CalculusLimitsAndContinuity, "
                   "marks.CalculusDifferentiation, "
                   "marks.CalculusIntegration, "
                   "marks.CalculusApplicationsCalculus, "
                   "marks.StatisticsDescriptiveStatistics, "
                   "marks.StatisticsInferentialStatistics, "
                   "marks.StatisticsProbabilityTheorems, "
                   "marks.StatisticsDistributions "
                   "FROM sgdb.studentmarks as marks "
                   "where studentID = %s", (Constants.studentID,))

    fetchedAll = cursor.fetchall()

    if fetchedAll:
        markNames = [i[0] for i in cursor.description]
        markValues = [i for i in fetchedAll[0]]

        mark1 = []
        mark2 = []
        mark3 = []
        mark4 = []
        val1 = []
        val2 = []
        val3 = []
        val4 = []
        colo1 = []
        colo2 = []
        colo3 = []
        colo4 = []

        for i in range(len(markNames)):
            if i < 4:
                mark1.append(markNames[i])
                val1.append(markValues[i])
                hue = random.random()
                saturation_range = (0.5, 1.0)
                brightness_range = (0.5, 1.0)
                for _ in range(4):
                    saturation = random.uniform(*saturation_range)
                    brightness = random.uniform(*brightness_range)
                    rgb = colorsys.hsv_to_rgb(hue, saturation, brightness)
                    hex_color = '#{:02X}{:02X}{:02X}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
                    colo1.append(hex_color)
            elif i < 8:
                mark2.append(markNames[i])
                val2.append(markValues[i])
                hue = random.random()
                saturation_range = (0.5, 1.0)
                brightness_range = (0.5, 1.0)
                for _ in range(4):
                    saturation = random.uniform(*saturation_range)
                    brightness = random.uniform(*brightness_range)
                    rgb = colorsys.hsv_to_rgb(hue, saturation, brightness)
                    hex_color = '#{:02X}{:02X}{:02X}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
                    colo2.append(hex_color)
            elif i < 12:
                mark3.append(markNames[i])
                val3.append(markValues[i])
                hue = random.random()
                saturation_range = (0.5, 1.0)
                brightness_range = (0.5, 1.0)
                for _ in range(4):
                    saturation = random.uniform(*saturation_range)
                    brightness = random.uniform(*brightness_range)
                    rgb = colorsys.hsv_to_rgb(hue, saturation, brightness)
                    hex_color = '#{:02X}{:02X}{:02X}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
                    colo3.append(hex_color)
            else:
                mark4.append(markNames[i])
                val4.append(markValues[i])
                hue = random.random()
                saturation_range = (0.5, 1.0)
                brightness_range = (0.5, 1.0)
                for _ in range(4):
                    saturation = random.uniform(*saturation_range)
                    brightness = random.uniform(*brightness_range)
                    rgb = colorsys.hsv_to_rgb(hue, saturation, brightness)
                    hex_color = '#{:02X}{:02X}{:02X}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
                    colo4.append(hex_color)

        fig, ax = plt.subplots(figsize=(10, 5))  # Create a figure and axis
        plt.tight_layout()
        plt.subplots_adjust(top=0.9, left=0.25)
        ax.barh(mark1, val1, color=colo1)  # Plot the histogram on the axis
        ax.set_title("Algebra", fontdict={"fontname": "Comic Sans MS", "size": 16})
        fig.patch.set_alpha(0.0)  # Figure background transparency
        ax.patch.set_alpha(0.0)  # Axes background transparency
        fig.savefig('histogram1.png')  # Save the figure as a PNG file
        plt.close(fig)  # Close the figure to free memory

        fig, ax = plt.subplots(figsize=(10, 5))  # Create a figure and axis
        plt.tight_layout()
        plt.subplots_adjust(top=0.9, left=0.25)
        ax.barh(mark2, val2, color=colo2)  # Plot the histogram on the axis
        ax.set_title("Geometry", fontdict={"fontname": "Comic Sans MS", "size": 16})
        fig.patch.set_alpha(0.0)  # Figure background transparency
        ax.patch.set_alpha(0.0)  # Axes background transparency
        fig.savefig('histogram2.png')  # Save the figure as a PNG file
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(10, 5))  # Create a figure and axis
        plt.tight_layout()
        plt.subplots_adjust(top=0.9, left=0.25)
        ax.barh(mark3, val3, color=colo3)  # Plot the histogram on the axis
        ax.set_title("Calculus", fontdict={"fontname": "Comic Sans MS", "size": 16})
        fig.patch.set_alpha(0.0)  # Figure background transparency
        ax.patch.set_alpha(0.0)  # Axes background transparency
        fig.savefig('histogram3.png')  # Save the figure as a PNG file
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(10, 5))  # Create a figure and axis
        plt.tight_layout()
        plt.subplots_adjust(top=0.9, left=0.25)
        ax.barh(mark4, val4, color=colo4)  # Plot the histogram on the axis
        ax.set_title("Statistics", fontdict={"fontname": "Comic Sans MS", "size": 16})
        fig.patch.set_alpha(0.0)  # Figure background transparency
        ax.patch.set_alpha(0.0)  # Axes background transparency
        fig.savefig('histogram4.png')  # Save the figure as a PNG file
        plt.close(fig)

    else:
        data = np.random.randn(20000)
        fig, ax = plt.subplots()  # Create a figure and axis
        ax.hist(data, color='blue')  # Plot the histogram on the axis
        ax.set_title("Subject #1", fontdict={"fontname": "Comic Sans MS", "size": 16})
        ax.set_xlabel('Value', fontdict={"fontname": "Comic Sans MS", "size": 12})
        ax.set_ylabel('Frequency', fontdict={"fontname": "Comic Sans MS", "size": 12})
        fig.patch.set_alpha(0.0)  # Figure background transparency
        ax.patch.set_alpha(0.0)  # Axes background transparency
        fig.savefig('histogram1.png')  # Save the figure as a PNG file
        plt.close(fig)  # Close the figure to free memory

        data = np.random.randn(30000)
        fig, ax = plt.subplots()  # Create a figure and axis
        ax.hist(data, color='blue')  # Plot the histogram on the axis
        ax.set_title("Subject #2", fontdict={"fontname": "Comic Sans MS", "size": 16})
        ax.set_xlabel('Value', fontdict={"fontname": "Comic Sans MS", "size": 12})
        ax.set_ylabel('Frequency', fontdict={"fontname": "Comic Sans MS", "size": 12})
        fig.patch.set_alpha(0.0)  # Figure background transparency
        ax.patch.set_alpha(0.0)  # Axes background transparency
        fig.savefig('histogram2.png')  # Save the figure as a PNG file
        plt.close(fig)  # Close the figure to free memory

        data = np.random.randn(40000)
        fig, ax = plt.subplots()  # Create a figure and axis
        ax.hist(data, color='blue')  # Plot the histogram on the axis
        ax.set_title("Subject #3", fontdict={"fontname": "Comic Sans MS", "size": 16})
        ax.set_xlabel('Value', fontdict={"fontname": "Comic Sans MS", "size": 12})
        ax.set_ylabel('Frequency', fontdict={"fontname": "Comic Sans MS", "size": 12})
        fig.patch.set_alpha(0.0)  # Figure background transparency
        ax.patch.set_alpha(0.0)  # Axes background transparency
        fig.savefig('histogram3.png')  # Save the figure as a PNG file
        plt.close(fig)  # Close the figure to free memory

        data = np.random.randn(50000)
        fig, ax = plt.subplots()  # Create a figure and axis
        ax.hist(data, color='blue')  # Plot the histogram on the axis
        ax.set_title("Subject #4", fontdict={"fontname": "Comic Sans MS", "size": 16})
        ax.set_xlabel('Value', fontdict={"fontname": "Comic Sans MS", "size": 12})
        ax.set_ylabel('Frequency', fontdict={"fontname": "Comic Sans MS", "size": 12})
        fig.patch.set_alpha(0.0)  # Figure background transparency
        ax.patch.set_alpha(0.0)  # Axes background transparency
        fig.savefig('histogram4.png')  # Save the figure as a PNG file
        plt.close(fig)  # Close the figure to free memory

    """cursor.execute("select "
                   "skills.GraphingEquationsFunctions, "
                   "skills.SolvingEquations, "
                   "skills.UnderstandingApplyingProperties, "
                   "skills.UsingAlgebraicTechniques, "
                   "skills.AnalyzingInterpretingData, "
                   "skills.ApplyingTheoremsFormulas, "
                   "skills.UnderstandingConcepts, "
                   "skills.SolvingRWProblems, "
                   "skills.UsingCalculatorsSoftware, "
                   "skills.ProvingTheoremsConcepts "
                   "from sgdb.studentskills as skills "
                   "where studentID = 1;")
    val = cursor.fetchall()"""
    """data = np.array(val)"""

    """fig, ax = plt.subplots()  # Create a figure and axis
    ax.hist(data)  # Plot the histogram on the axis
    ax.set_title("Recent tests", fontdict={"fontname": "Comic Sans MS", "size": 16})
    ax.set_xlabel('Value', fontdict={"fontname": "Comic Sans MS", "size": 12})
    ax.set_ylabel('Frequency', fontdict={"fontname": "Comic Sans MS", "size": 12})
    fig.patch.set_alpha(0.0)  # Figure background transparency
    ax.patch.set_alpha(0.0)  # Axes background transparency
    fig.savefig('histogram3.png')  # Save the figure as a PNG file
    plt.close(fig)  # Close the figure to free memory"""

    connection.close()
    stats_canvas.image_image_0 = PhotoImage(
        file="histogram.png")

    stats_canvas.image_image_1 = PhotoImage(
        file="histogram1.png")

    stats_canvas.image_image_2 = PhotoImage(
        file="histogram2.png")

    stats_canvas.image_image_3 = PhotoImage(
        file="histogram3.png")

    stats_canvas.image_image_4 = PhotoImage(
        file="histogram4.png")

    # stats_canvas.image_image_1 = PhotoImage(
    #     file=relative_to_assets("image_1.png"))
    new_size = (stats_canvas.image_image_0.height() + stats_canvas.image_image_1.height() +
                stats_canvas.image_image_2.height() + stats_canvas.image_image_3.height() +
                stats_canvas.image_image_4.height())

    image = Image.open(relative_to_assets("image_1.png"))
    image = image.resize((1440, new_size))
    stats_canvas.pic = ImageTk.PhotoImage(image)
    image_1 = stats_canvas.create_image(
        720.0,
        new_size / 3 + 500 / 2,
        image=stats_canvas.pic
    )

    graphs_offset = 150
    image_20 = stats_canvas.create_image(
        720.0,
        graphs_offset,
        image=stats_canvas.image_image_0
    )

    graphs_offset += stats_canvas.image_image_0.height() - 20

    image_21 = stats_canvas.create_image(
        720.0,
        graphs_offset,
        image=stats_canvas.image_image_1
    )

    graphs_offset += stats_canvas.image_image_1.height() - 20

    image_22 = stats_canvas.create_image(
        720.0,
        graphs_offset,
        image=stats_canvas.image_image_2
    )

    graphs_offset += stats_canvas.image_image_2.height() - 20

    image_23 = stats_canvas.create_image(
        720.0,
        graphs_offset,
        image=stats_canvas.image_image_3
    )

    graphs_offset += stats_canvas.image_image_3.height() - 20

    image_24 = stats_canvas.create_image(
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
