# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from statistics import display_plot

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\benzo\PycharmProjects\TryNewUI\Scripts\frame1")

header_frame: Frame
header_canvas: Canvas
welcome_text: str


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def init_header_frame(head_frame, show_frame):
    global header_frame
    global header_canvas
    global welcome_text

    header_frame = head_frame
    header_canvas = Canvas(
        header_frame,
        bg="#FFFFFF",
        height=138,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    header_canvas.image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = header_canvas.create_image(
        150.0,
        78.0,
        image=header_canvas.image_image_3
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        header_frame,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        command=lambda: show_frame("profile"),
        relief="flat"
    )
    button_2.place(
        x=625.0 + 10,
        y=76.0,
        width=95.0,
        height=24.0
    )
    button_2.image = button_image_2

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        header_frame,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        command=lambda: (show_frame("stats"), display_plot()),
        relief="flat"
    )
    button_3.place(
        x=347.0 + 10,
        y=76.0,
        width=88.0,
        height=24.0
    )
    button_3.image = button_image_3

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        header_frame,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=478.0 + 10,
        y=76.0,
        width=104.0,
        height=24.0
    )
    button_4.image = button_image_4

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        header_frame,
        name="sign_b",
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=1270.0,
        y=63.0,
        width=119.0,
        height=52.0
    )
    button_5.image = button_image_5

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        header_frame,
        name="login_b",
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#FFFFFF",
        command=lambda: show_frame("login"),
        relief="flat"
    )
    button_6.place(
        x=1133.0,
        y=63.0,
        width=120.0,
        height=52.0
    )
    button_6.image = button_image_6

    button_image_7 = PhotoImage(
        file=relative_to_assets("home_page_writen.png"))
    button_7 = Button(
        header_frame,
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#FFFFFF",
        bg='#FFFFFF',
        command=lambda: show_frame("main"),
        relief="flat"
    )
    button_7.place(
        x=264.0,
        y=76.0,
        width=56.0,
        height=24.0
    )
    button_7.image = button_image_7

    welcome_text = header_canvas.create_text(
        1150.0,
        63,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 32 * -1)
    )
    header_canvas.grid(row=0, column=0, sticky=NSEW)


# button_5.bind("<Button-1>", lambda e: on_click(e))


def change():
    header_frame.nametowidget("login_b").destroy()
    header_frame.nametowidget("sign_b").destroy()
    header_canvas.itemconfig(welcome_text, text="Welcome, Ben")
