# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkinter import *
from tkcalendar import Calendar
import re
from student_example import set_the_login_or_signup_details
import MySQLdb
import os
from dotenv import load_dotenv
from constants import Constants
import random

load_dotenv()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"frame3")

signup_canvas: Canvas


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def change_state(comb, g_entry):
    comb["state"] = "readonly"
    g_entry.event_generate("<Down>")


def change_state_back(comb):
    comb["state"] = "normal"


def grab_date(cal, date, date_win):
    date["state"] = "normal"
    date.delete(0, END)
    date.insert(0, cal.get_date())
    date_win.destroy()


def pick_date(event, dob):
    dob["state"] = "readonly"
    date_window = Toplevel()
    date_window.grab_set()
    date_window.title('Choose Date Of Birth')
    date_window.geometry('450x280+590+370')
    cal_style = ttk.Style()
    cal_style.theme_use('clam')
    cal = Calendar(
        date_window,
        selectmode="day", date_pattern="dd/mm/y",
        background="#86BEC9", bordercolor="#86BEC9",
        headersbackground="#86BEC9", foreground='white',
        normalforeground='black', headersforeground='white'
    )
    cal.pack(fill=BOTH, expand=TRUE)

    submit_btn = Button(
        date_window,
        text="Submit",
        background='#86BEC9',
        command=(lambda: grab_date(cal, dob, date_window)),
        height=2,
        width=10
    )
    submit_btn.pack(pady=10)


def get_data_from_entries(name, grade, email, gender, dob, password, change_frame, valid_text):
    global signup_canvas

    connection = MySQLdb.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        passwd=os.getenv("PASSWD"),
        db=os.getenv("DB")
    )
    cursor = connection.cursor()
    cursor.execute("""SELECT studentID FROM sgdb.studentlogin Order by studentID desc LIMIT 1;""")
    nextID = cursor.fetchall()[0][0]
    nextID += 1

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not name or not grade or not email or not re.fullmatch(regex, email) or not password or dob == "dd/mm/yyyy":
        signup_canvas.itemconfig(valid_text, text="One or more fields are not valid")
    else:
        list_det = [name, grade, email, gender, dob, password]
        genD = 0 if gender == "Male" else 1
        nameArray = name.split(" ")
        firstName = nameArray[0]
        lastName = nameArray[1]
        studyTime = random.uniform(0, 18)
        cursor.execute("""INSERT INTO
        sgdb.studentlogin (`studentID`, `FirstName`, `LastName`, `Email`, `Password`, `Birthday`, `Grade`)
        VALUES (%s, %s, %s, %s, %s, %s, %s);""", (nextID, firstName, lastName, email, password, dob, grade))
        connection.commit()

        cursor.execute("""INSERT INTO
        sgdb.studentinfo (`studentID`, `Gender`, `StudyTimeWeekly`, `Absences`, `Tutoring`, `ParentalSupport`)
        VALUES (%s, %s, %s, %s, %s, %s);""", (nextID, genD, studyTime, 0, 0, 2))
        connection.commit()

        cursor.execute(""" INSERT INTO
        sgdb.studentskills (`studentID`, `GraphingEquationsFunctions`, `SolvingEquations`,
                        `UnderstandingApplyingProperties`, `UsingAlgebraicTechniques`, `AnalyzingInterpretingData`,
                        `ApplyingTheoremsFormulas`, `UnderstandingConcepts`, `SolvingRWProblems`,
                        `UsingCalculatorsSoftware`, `ProvingTheoremsConcepts`)
        VALUES(%s, '55', '55', '55', '55', '55', '55', '55', '55', '55', '55');""", (nextID,))
        connection.commit()

        cursor.execute("""INSERT INTO
        sgdb.studentmarks (`studentID`, `AlgebraLinearEquations`, `AlgebraQuadraticEquations`, `AlgebraPolynomials`,
                       `AlgebraExponentsAndLogarithms`, `GeometryCoordinateGeometry`, `GeometryTrigonometry`,
                       `GeometryCircles`, `GeometryVectors`, `CalculusLimitsAndContinuity`, `CalculusDifferentiation`,
                       `CalculusIntegration`, `CalculusApplicationsCalculus`, `StatisticsDescriptiveStatistics`,
                       `StatisticsInferentialStatistics`, `StatisticsProbabilityTheorems`, `StatisticsDistributions`)
        VALUES(%s, '55', '55', '55', '55', '55', '55', '55', '55', '55', '55', '55', '55', '55', '55', '55', '55');""",
                       (nextID,))
        connection.commit()

        Constants.studentID = nextID
        set_the_login_or_signup_details(list_det)
        change_frame("main", name)

    connection.close()


# global selected_date

# window = Tk()
#
# window.geometry("1440x886")
# window.configure(bg="#FFFFFF")


def show_signup_frame(signup_frame, show_frame, show_frame_log):
    global signup_canvas

    signup_canvas = Canvas(
        signup_frame,
        bg="#FFFFFF",
        height=886,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    signup_canvas.place(x=0, y=0)

    signup_canvas.image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = signup_canvas.create_image(
        720.0,
        443.0,
        image=signup_canvas.image_image_1
    )

    signup_canvas.image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = signup_canvas.create_image(
        720.0,
        442.0,
        image=signup_canvas.image_image_2
    )

    signup_canvas.text_img = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    grade_bg_1 = signup_canvas.create_image(
        408.5,
        487.5,
        image=signup_canvas.text_img
    )
    grade_entry = Entry(
        signup_frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Intern", 18)
    )
    grade_entry.place(
        x=198.0,
        y=471.0,
        width=421.0,
        height=34.0
    )

    signup_canvas.create_text(
        195.0,
        201.0,
        anchor="nw",
        text="Sign up",
        fill="#000000",
        font=("Inter", 34 * -1)
    )

    signup_canvas.create_text(
        828.0,
        542.0,
        anchor="nw",
        text="Create password",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    signup_canvas.create_text(
        195.0,
        542.0,
        anchor="nw",
        text="Enter email",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    signup_canvas.create_text(
        823.0,
        426.0,
        anchor="nw",
        text="DOB",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    signup_canvas.create_text(
        195.0,
        426.0,
        anchor="nw",
        text="Enter your grade",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    signup_canvas.create_text(
        823.0,
        310.0,
        anchor="nw",
        text="Gender",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    signup_canvas.create_text(
        195.0,
        310.0,
        anchor="nw",
        text="Enter full name",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    name_bg = signup_canvas.create_image(
        408.5,
        377.5,
        image=signup_canvas.text_img
    )
    name_entry = Entry(
        signup_frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Intern", 18)
    )
    name_entry.place(
        x=198.0,
        y=361.0,
        width=421.0,
        height=34.0
    )

    gender_bg = signup_canvas.create_image(
        1034.5,
        377.5,
        image=signup_canvas.text_img
    )

    style = ttk.Style()
    style.theme_use("clam")
    style.configure('MyTheme.TCombobox',
                    background='#FFFFFF',
                    bordercolor='#FFFFFF',
                    foreground='#000123',
                    fieldbackground='white',
                    darkcolor="white",
                    lightcolor="white",
                    )

    values = ["Male", "Female", "Other"]

    gender_entry = ttk.Combobox(
        signup_frame,
        font=("Intern", 24 * -1),
        style='MyTheme.TCombobox',
        values=values,
    )

    gender_entry.current(0)

    gender_entry.bind("<Button-1>", lambda e: change_state(gender_entry, gender_entry))
    gender_entry.bind("<<ComboboxSelected>>", lambda e: change_state_back(gender_entry))

    # gender_entry = Entry(
    #     bd=0,
    #     bg="#FFFFFF",
    #     fg="#000716",
    #     highlightthickness=0,
    #     font=("Intern", 18)
    # )
    gender_entry.place(
        x=824.0,
        y=361.0,
        width=421.0,
        height=34.0
    )

    email_bg = signup_canvas.create_image(
        408.5,
        611.5,
        image=signup_canvas.text_img
    )
    email_entry = Entry(
        signup_frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Intern", 18)
    )
    email_entry.place(
        x=198.0,
        y=595.0,
        width=421.0,
        height=34.0
    )

    dob_bg = signup_canvas.create_image(
        1034.5,
        487.5,
        image=signup_canvas.text_img
    )
    dob_entry = Entry(
        signup_frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("Intern", 18)
    )
    dob_entry.place(
        x=824.0,
        y=471.0,
        width=421.0,
        height=34.0
    )
    dob_entry.insert(0, "dd/mm/yyyy")
    dob_entry.bind("<Button-1>", lambda e: pick_date(e, dob_entry))

    entry_bg_6 = signup_canvas.create_image(
        1034.5,
        611.5,
        image=signup_canvas.text_img
    )
    password_entry = Entry(
        signup_frame,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        show='*',
        highlightthickness=0,
        font=("Intern", 18)
    )
    password_entry.place(
        x=824.0,
        y=595.0,
        width=421.0,
        height=34.0
    )

    signup_canvas.button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        signup_frame,
        image=signup_canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#96C1C9",
        command=lambda: get_data_from_entries(
            name_entry.get(),
            grade_entry.get(),
            email_entry.get(),
            gender_entry.get(),
            dob_entry.get(),
            password_entry.get(),
            show_frame_log,
            validation_text
        ),
        relief="flat"
    )
    button_1.place(
        x=637.0,
        y=678.0,
        width=176.0,
        height=52.0
    )

    validation_text = signup_canvas.create_text(
        585.0,
        645.0,
        anchor="nw",
        text="",
        fill="red",
        font=("Inter", 20 * -1)
    )
# window.resizable(False, False)
# window.mainloop()
