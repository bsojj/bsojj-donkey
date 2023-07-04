from customtkinter import (
    CTkFrame,
    CTkButton,
    CTkLabel,
)
from utils import (
    colors,
    create_back_button,
    text_font,
    btn_text_color,
)


class RootFindFrame(CTkFrame):
    def create_label(self, row, label):
        new_label = CTkLabel(
            self,
            text=label,
            font=("Lilita One", 16),
            text_color=btn_text_color,
            fg_color=(colors["blue-500"], colors["blue-800"]),
            corner_radius=20,
            width=50,
        )
        new_label.grid(row=row, column=0, ipadx=15, pady=10)
        return new_label

    def create_root_btn(self, parent, column, label, command=None):
        new_btn = CTkButton(
            master=parent,
            text=label,
            command=command,
            font=text_font(16),
            width=250,
        )
        new_btn.grid(row=0, column=column, padx=10, ipadx=20, ipady=10)
        return new_btn

    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.bracket_label = self.create_label(0, "Bracket Method")
        self.bracket_group = CTkFrame(self, fg_color="transparent")
        self.bracket_group.grid(row=1, column=0, pady=20)
        self.bisection_btn = self.create_root_btn(
            self.bracket_group,
            0,
            "Bisection",
            command=lambda: parent.show_frame("BisectionInput"),
        )
        self.falsi_btn = self.create_root_btn(self.bracket_group, 1, "False Position")

        self.open_label = self.create_label(2, "Open Method")
        self.open_group = CTkFrame(self, fg_color="transparent")
        self.open_group.grid(row=3, column=0, pady=20)
        self.newton_btn = self.create_root_btn(self.open_group, 0, "Newton-Raphson")
        self.secant_btn = self.create_root_btn(self.open_group, 1, "Secant")

        self.back_btn = create_back_button(self, parent.show_home)
        self.back_btn.grid(row=4, column=0, padx=20, pady=20, ipadx=10, sticky="e")
