from tkinter import *
from pathlib import Path
import numpy as np
from groq_try import get_questions_and_answers

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\benzo\PycharmProjects\TryNewUI\Scripts\frame2")

test_canvas: Canvas
i = 0


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def make_a_test(text_to_show, next_button):
    test_maker = ("Build a test at algebra with 6 questions and 4 multi-option answers for 8th grade. "
                  "- At your respond give just the text by the next format: "
                  "Question(number)\n"
                  "the question.\n\n"
                  "the answers (from A to D)")
    questions, answers = get_questions_and_answers(test_maker)
    # for j, (q, a) in enumerate(zip(questions, answers)):
    #     print(f"{q}\n")
    #     for ans in a:
    #         print(ans)
    #     print()

    # test_canvas.itemconfig(text_to_show, text=questions[0])
    print("Before")
    next_button.configure(command=lambda: show_next(text_to_show, questions))


def show_next(text_to_show, questions):
    print("After")
    global i
    if i < len(questions):
        test_canvas.itemconfig(text_to_show, text=questions[i])
        i += 1
    else:
        test_canvas.itemconfig(text_to_show, text="END of test")
        i = 0


def show_test_frame(test_frame, show_frame):
    global test_canvas
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

    test_canvas.image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = test_canvas.create_image(
        720.0,
        443.0,
        image=test_canvas.image_image_1
    )

    test_text = test_canvas.create_text(
        720.0,
        400.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    test_canvas.button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        test_frame,
        image=test_canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#7DABB2",
        relief="flat"
    )
    button_1.place(
        x=905.0,
        y=681.0,
        width=198.0,
        height=51.0
    )

    make_a_test(test_text, button_1)


