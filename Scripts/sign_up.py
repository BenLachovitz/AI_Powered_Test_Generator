# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import fontTools.config
import ttkbootstrap as tb
from ttkbootstrap.dialogs.dialogs import DatePickerDialog
from ttkbootstrap import Combobox
from datetime import date

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\benzo\PycharmProjects\TryNewUI\Scripts\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def get_entries(name, grade, email, gender, dob, password):
    if not name or not grade or not email or not gender or not dob or not password:
        print("FALSE")
    else:
        print(name, gender, dob)


class CustomDateEntry(tb.DateEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.entry["state"] = "readonly"
        self.entry["font"] = 10

    def _on_date_ask(self):
        self.entry["state"] = "normal"
        super()._on_date_ask()
        self.entry["state"] = "readonly"


text_check: str

window = Tk()

window.geometry("1440x886")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=886,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

text_box_img = PhotoImage(
    file=relative_to_assets("entry_1.png"))

genders = ['Male', 'Female']

gender_img = canvas.create_image(
    1034.5,
    377.5,
    image=text_box_img
)

gender_combobox = Combobox(
    style="light",
    state='readonly',
    values=genders,
    font=("Inter", 16)
)
gender_combobox.current(0)
gender_combobox.place(
    x=824.0,
    y=361.0,
    width=422.0,
    height=34.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    720.0,
    443.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    720.0,
    442.0,
    image=image_image_2
)

grade_img = canvas.create_image(
    408.5,
    487.5,
    image=text_box_img
)
grade_entry = tb.Entry(
    style="light",
    font=("Inter", 16)
)
grade_entry.place(
    x=198.0,
    y=471.0,
    width=421.0,
    height=34.0
)

canvas.create_text(
    195.0,
    201.0,
    anchor="nw",
    text="Sign up",
    fill="#000000",
    font=("Inter", 34 * -1)
)

canvas.create_text(
    828.0,
    542.0,
    anchor="nw",
    text="Create password",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    195.0,
    542.0,
    anchor="nw",
    text="Enter email",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    823.0,
    426.0,
    anchor="nw",
    text="DOB",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    195.0,
    426.0,
    anchor="nw",
    text="Enter your grade",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    823.0,
    310.0,
    anchor="nw",
    text="Gender",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    195.0,
    310.0,
    anchor="nw",
    text="Enter full name",
    fill="#000000",
    font=("Inter", 24 * -1)
)

name_img = canvas.create_image(
    408.5,
    377.5,
    image=text_box_img
)
name_entry = tb.Entry(
    style="light",
    font=("Inter", 16)
)
name_entry.place(
    x=198.0,
    y=361.0,
    width=421.0,
    height=34.0
)

# gender_combobox = ttk.Combobox(
#     background="#FFFFFF",
#     foreground="#000716",
#     font=("Inter", 16),
#     state='readonly',
#     values=genders
# )
# gender_combobox.place(
#     x=824.0,
#     y=361.0,
#     width=422.0,
#     height=34.0
# )

# gender_entry = Entry(
#     bd=0,
#     bg="#FFFFFF",
#     fg="#000716",
#     highlightthickness=0,
#     font=("Inter", 16)
# )
# gender_entry.place(
#     x=824.0,
#     y=361.0,
#     width=421.0,
#     height=34.0
# )

email_img = canvas.create_image(
    408.5,
    611.5,
    image=text_box_img
)
email_entry = tb.Entry(
    style='light',
    font=("Inter", 16)
)
email_entry.place(
    x=198.0,
    y=595.0,
    width=421.0,
    height=34.0
)

# dob_img = canvas.create_image(
#     1034.5,
#     487.5,
#     image=text_box_img
# )

dob_entry = CustomDateEntry(
    bootstyle='light',
    dateformat='%x',
    relief='flat',
)
dob_entry.place(
    x=824.0,
    y=471.0,
    width=424.0,
    height=36.0
)

# dob_entry = Entry(
#     bd=0,
#     bg="#FFFFFF",
#     fg="#000716",
#     highlightthickness=0,
#     font=("Inter", 16)
# )
# dob_entry.place(
#     x=824.0,
#     y=471.0,
#     width=421.0,
#     height=34.0
# )

password_img = canvas.create_image(
    1034.5,
    611.5,
    image=text_box_img
)
password_entry = tb.Entry(
    style="light",
    show='*',
    font=("Inter", 16)
)
password_entry.place(
    x=824.0,
    y=595.0,
    width=421.0,
    height=34.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#96C1C9",
    command=lambda: get_entries(
        name_entry.get(),
        grade_entry.get(),
        email_entry.get(),
        gender_combobox.get(),
        dob_entry.entry.get(),
        password_entry.get()
    ),
    relief="flat"
)
button_1.place(
    x=637.0,
    y=678.0,
    width=176.0,
    height=52.0
)
window.resizable(False, False)
window.mainloop()
