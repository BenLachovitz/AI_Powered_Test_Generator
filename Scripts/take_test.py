import random
from tkinter import *
from pathlib import Path
from string_check import parse_evaluation_string

import numpy as np
from groq_try import get_questions_and_answers, use_llama
from constants import Constants
import MySQLdb
import os
from dotenv import load_dotenv

load_dotenv()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"frame4")

test_canvas: Canvas
test_frame: Frame
options: []
i = 0
rnd = 0


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def performance_evaluation(questions, checking_ans):
    global skillTable
    global subjectSubTable

    connection = MySQLdb.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        passwd=os.getenv("PASSWD"),
        db=os.getenv("DB")
    )

    cursor = connection.cursor()

    cursor.execute("""SELECT * 
    FROM sgdb.studentskills 
    where studentID = %s;""", (Constants.studentID,))

    fetchedAll = cursor.fetchall()

    if fetchedAll:
        field_names = [i[0] for i in cursor.description][1:]
        values = [i for i in fetchedAll[0]][1:]
        skillTable = [[i, j] for i, j in zip(field_names, values)]
    else:
        skillTable = []

    cursor.execute(
        "SET @sql = NULL; "
        "SELECT GROUP_CONCAT(column_name) INTO @sql "
        "FROM information_schema.columns "
        "WHERE table_name = 'studentmarks' "
        "AND table_schema = 'sgdb' "
        f"AND column_name LIKE '{Constants.subjects[Constants.randomIndex]}%';"
    )
    cursor.execute(
        f"SET @sql = CONCAT('SELECT ', @sql, ' FROM sgdb.studentmarks WHERE studentID = {Constants.studentID}');"
        "PREPARE stmt FROM @sql;"
    )
    cursor.execute("EXECUTE stmt;")
    fetchedAll = cursor.fetchall()

    if fetchedAll:
        field_names = [i[0] for i in cursor.description]
        values = [i for i in fetchedAll[0]]
        subjectSubTable = [[i, j] for i, j in zip(field_names, values)]
    else:
        skillTable = []

    cursor.execute("DEALLOCATE PREPARE stmt;")

    evaluate_skills_prompt = (
        f"Given the questions that i give you the results of the student , his set of skills and his set of grades in each subject,"
        f"Please evaluate and update the relevant skills and subjects. "
        #f"if the new grade is lower than we original please do not change it. change only if the grade is improving"
        f"The skills: {skillTable} "
        f"The subjects: {subjectSubTable} "
        f"The questions:\n{questions}"
        f"The results:\n{checking_ans}"
        f"- At your response give only the set of skills by the next format:"
        f"SKILL_NAME: SKILL_GRADE or SUBJECT_NAME:SUBJECT_GRADE"
        f"please start each set with '***'"
        f"without any notes or starting or ending, just the skills set and the subject set")

    evaluate_skills_answer_string = use_llama(evaluate_skills_prompt)
    skills, subjects = parse_evaluation_string(evaluate_skills_answer_string)

    cursor.execute("UPDATE sgdb.studentskills SET "
                   f"{skills[0][0]} = {skills[0][1]}, "
                   f"{skills[1][0]} = {skills[1][1]}, "
                   f"{skills[2][0]} = {skills[2][1]}, "
                   f"{skills[3][0]} = {skills[3][1]}, "
                   f"{skills[4][0]} = {skills[4][1]}, "
                   f"{skills[5][0]} = {skills[5][1]}, "
                   f"{skills[6][0]} = {skills[6][1]}, "
                   f"{skills[7][0]} = {skills[7][1]}, "
                   f"{skills[8][0]} = {skills[8][1]}, "
                   f"{skills[9][0]} = {skills[9][1]} "
                   f"WHERE (`studentID` = {Constants.studentID});")
    connection.commit()

    cursor.execute("UPDATE sgdb.studentmarks SET "
                   f"{subjects[0][0]} = {subjects[0][1]}, "
                   f"{subjects[1][0]} = {subjects[1][1]}, "
                   f"{subjects[2][0]} = {subjects[2][1]}, "
                   f"{subjects[3][0]} = {subjects[3][1]} "
                   f"WHERE (`studentID` = {Constants.studentID});")
    connection.commit()


def make_a_test(text_to_show, next_button, restart_button):
    global test_frame
    global skillTable

    connection = MySQLdb.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        passwd=os.getenv("PASSWD"),
        db=os.getenv("DB")
    )

    cursor = connection.cursor()

    cursor.execute("""SELECT * 
        FROM sgdb.studentskills 
        where studentID = %s;""", (Constants.studentID,))

    fetchedAll = cursor.fetchall()

    if fetchedAll:
        field_names = [i[0] for i in cursor.description][1:]
        values = [i for i in fetchedAll[0]][1:]
        skillTable = [[i, j] for i, j in zip(field_names, values)]
    else:
        skillTable = []

    Constants.randomIndex = random.randint(0, 3)
    test_maker = ("Build a test in the following subject "
                  f"{Constants.subjects[Constants.randomIndex]} "
                  f"that has the following learning skills: {skillTable}."
                  "The test is made of 6 questions and 4 multi-option answers for the 11th grade. "
                  "- In your response provide just the test in the next format: "
                  "Question(number)\n - without marks like '**' just the question and the number"
                  "the question.\n\n"
                  "the answers (from A to D)")
    questions, answers = get_questions_and_answers(test_maker)
    checking_ans = []
    for j, (q, a) in enumerate(zip(questions, answers)):
        print(f"{q}\n")
        for ans in a:
            print(ans)
        print()

    next_button.place(
        x=620.0,
        y=681.0,
        width=198.0,
        height=51.0
    )
    next_button.configure(
        command=lambda: show_next(text_to_show, questions, answers, next_button, restart_button, checking_ans))
    show_next(text_to_show, questions, answers, next_button, restart_button, checking_ans)


def show_next(text_to_show, questions, answers, next_button, restart_button, checking_ans):
    global i, options
    if i == 0 or (i > 0 and test_frame.chose.get() != 'x'):
        if i == 0:
            option1 = Radiobutton(
                test_frame,
                background='#b2cdd1',
                activebackground='#bad3d6',
                activeforeground='black',
                font=("Inter", 16, "bold")
            )
            option2 = Radiobutton(
                test_frame,
                background='#a9c7cc',
                activebackground='#bad3d6',
                activeforeground='black',
                font=("Inter", 16, "bold")
            )
            option3 = Radiobutton(
                test_frame,
                background='#9fc1c6',
                activebackground='#bad3d6',
                activeforeground='black',
                font=("Inter", 16, "bold")
            )
            option4 = Radiobutton(
                test_frame,
                background='#97bcc1',
                activebackground='#bad3d6',
                activeforeground='black',
                font=("Inter", 16, "bold")
            )
            option1.place(
                x=440,
                y=400
            )
            option2.place(
                x=440,
                y=450
            )
            option3.place(
                x=440,
                y=500
            )
            option4.place(
                x=440,
                y=550
            )
            options = [option1, option2, option3, option4]
        else:
            answer_check_prompt = (f"Please check the student answer on the next question:\n{questions[i - 1]}"
                                   f"\n\nThe student answer is:\n{test_frame.chose.get()}. "
                                   f"- at your respond provide only "
                                   f"if it's correct or incorrect")
            llama_string = use_llama(answer_check_prompt)
            checking_ans.append(llama_string)
            test_frame.chose.set('x')
        if i < len(questions):
            test_canvas.itemconfig(text_to_show, text=questions[i])
            for j, the_option in enumerate(options):
                the_option.configure(text=answers[i][j], variable=test_frame.chose, value=answers[i][j])
            i += 1
        else:
            test_canvas.itemconfig(text_to_show, text="END of test")
            next_button.place_forget()
            restart_button.place(
                x=620.0,
                y=681.0,
                width=198.0,
                height=51.0
            )
            printing_results(checking_ans, text_to_show)
            i = 0
            for the_option in options:
                the_option.place_forget()

            if Constants.studentID > 0:
                performance_evaluation(questions, checking_ans)
    else:
        print("choose an option")


def printing_results(selected_answers, text_to_show):
    results_overlook = ""
    for j, a in enumerate(selected_answers):
        results_overlook += f"Question {j + 1}: {a}\n\n"
    test_canvas.itemconfig(text_to_show, text=results_overlook)


def show_test_frame(make_test_frame, show_frame):
    global test_canvas, test_frame, options
    test_frame = make_test_frame
    test_canvas = Canvas(
        test_frame,
        bg="#FFFFFF",
        height=886,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    test_canvas.grid(row=0, column=0, sticky=NSEW)

    test_frame.chose = StringVar(value='x')

    test_canvas.image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = test_canvas.create_image(
        720.0,
        443.0,
        image=test_canvas.image_image_1
    )

    test_canvas.image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = test_canvas.create_image(
        720.0,
        442.0,
        image=test_canvas.image_image_2
    )

    test_text = test_canvas.create_text(
        440.0,
        180.0,
        width=560,
        anchor="nw",
        text="Welcome to automatic test generator and checking using Llama3.1, which is an AI from Meta.",
        fill="#000000",
        font=("Inter", 26 * -1, "bold")
    )

    test_canvas.button_image_1 = PhotoImage(
        file=relative_to_assets("next_button.png"))
    next_button = Button(
        test_frame,
        image=test_canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#7DABB2",
        relief="flat"
    )

    test_canvas.button_image_3 = PhotoImage(
        file=relative_to_assets("restart_button.png"))
    restart_button = Button(
        test_frame,
        image=test_canvas.button_image_3,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#7DABB2",
        relief="flat",
        command=lambda: show_test_frame(test_frame, show_frame=NONE)
    )
    restart_button.place_forget()

    test_canvas.button_image_2 = PhotoImage(
        file=relative_to_assets("start_test.png"))
    start_test_button = Button(
        test_frame,
        image=test_canvas.button_image_2,
        text="START",
        borderwidth=0,
        highlightthickness=0,
        activebackground="#7DABB2",
        relief="flat",
        command=lambda: (make_a_test(test_text, next_button, restart_button), start_test_button.place_forget())
    )
    start_test_button.place(
        x=620.0,
        y=681.0,
        width=198.0,
        height=51.0
    )
