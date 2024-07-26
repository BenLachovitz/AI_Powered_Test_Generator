from tkinter import *
from tkinter import Tk, Frame, BOTH

from login import show_login_frame
from home_page import show_main_frame
from init_header import init_header_frame
from init_header import change
from my_profile import show_my_profile_frame
from statistics import show_statistics_frame
from sign_up import show_signup_frame


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1440x1024")
        self.configure(bg="#69D3D2")
        self.resizable(False, False)

        self.container = Frame(self)
        self.container.pack(fill=BOTH, expand=1)

        self.frames = {}
        self.create_frames()

    def create_frames(self):
        header_frame = Frame(self.container, height=138)
        main_window = Frame(self.container, height=886)

        header_frame.pack(fill=X, side=TOP)
        main_window.pack(fill=BOTH, expand=TRUE)

        init_header_frame(header_frame, self.show_frame)

        login_frame = Frame(main_window)
        profile_frame = Frame(main_window)
        stats_frame = Frame(main_window)
        signup_frame = Frame(main_window)
        main_frame = Frame(main_window)

        self.frames["login"] = login_frame
        self.frames["profile"] = profile_frame
        self.frames["stats"] = stats_frame
        self.frames["signup"] = signup_frame
        self.frames["main"] = main_frame

        login_frame.grid(row=0, column=0, sticky=NSEW)
        profile_frame.grid(row=0, column=0, sticky=NSEW)
        stats_frame.grid(row=0, column=0, sticky=NSEW)
        signup_frame.grid(row=0, column=0, sticky=NSEW)
        main_frame.grid(row=0, column=0, sticky=NSEW)

        show_login_frame(login_frame, self.show_frame, self.show_frame_after_sign)
        show_my_profile_frame(profile_frame, self.show_frame)
        show_statistics_frame(stats_frame, self.show_frame)
        show_signup_frame(signup_frame, self.show_frame, self.show_frame_after_sign)
        show_main_frame(main_frame, self.show_frame)

        self.show_frame("main")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

    def show_frame_after_sign(self, frame_name, student_name):
        frame = self.frames[frame_name]
        change(student_name)
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
