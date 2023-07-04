import tkinter
from customtkinter import (
    set_appearance_mode,
    CTk,
)
from os import path
from frames.home_frame import HomeFrame
from frames.binary import BinaryInputFrame, BinaryResultFrame
from frames.root_find import RootFindFrame
from frames.bisection import BisectionInputFrame, BisectionResultFrame
from frames.falsi import FalsiInputFrame, FalsiResultFrame

# Modes: "System" (standard), "Dark", "Light"
set_appearance_mode("Dark")


class App(CTk):
    current_frame = None
    current_path = path.dirname(path.realpath(__file__))
    image_path = path.join(current_path, "images")
    main_width = 900
    main_padding = 50
    main_height = 600
    frames = {}

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Calculator")
        self.geometry(f"{self.main_width}x{self.main_height}")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.resizable(False, False)

        self.frames["BinaryInput"] = BinaryInputFrame(self)
        self.frames["BinaryResult"] = BinaryResultFrame(self)
        self.frames["RootFind"] = RootFindFrame(self)
        self.frames["BisectionInput"] = BisectionInputFrame(self)
        self.frames["BisectionResult"] = BisectionResultFrame(self)
        self.frames["FalsiInput"] = FalsiInputFrame(self)
        self.frames["FalsiResult"] = FalsiResultFrame(self)
        self.frames["Home"] = HomeFrame(self)
        self.frames["Home"].grid(
            row=0, column=0, ipadx=10, ipady=10, sticky="ew", padx=self.main_padding
        )

        self.current_frame = self.frames["Home"]

    def show_frame(self, frame):
        self.current_frame.grid_forget()
        self.frames[frame].grid(row=0, column=0, sticky="ew", padx=self.main_padding)
        self.current_frame = self.frames[frame]

    def show_home(self):
        self.show_frame("Home")


if __name__ == "__main__":
    app = App()
    app.mainloop()
