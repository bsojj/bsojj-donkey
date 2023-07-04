from customtkinter import (
    CTkFrame,
    CTkImage,
    CTkButton,
    CTkLabel,
)
from PIL import Image
from os import path, sep
from utils import btn_text_color, btn_hover_color


class HomeFrame(CTkFrame):
    image_path = ""
    btn_size = 180

    def createHomeButton(self, column, image, label, command=None):
        new_btn_img = CTkImage(
            Image.open(path.join(self.image_path, f"{image}.png")),
            size=(self.btn_size - 50, self.btn_size - 50),
        )
        new_btn = CTkButton(
            self.container,
            image=new_btn_img,
            corner_radius=7,
            compound="top",
            height=self.btn_size,
            width=self.btn_size,
            text=label,
            font=("Lilita One", 18),
            text_color=btn_text_color,
            hover_color=btn_hover_color,
            fg_color="transparent",
            command=command,
        )
        new_btn.grid(row=0, column=column, padx=10, pady=10)
        return new_btn

    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.container = CTkFrame(self, fg_color="transparent")
        self.container.grid(row=0, column=0)
        self.container.grid_columnconfigure(3, weight=1)
        self.image_path = parent.image_path

        self.home_binary_btn = self.createHomeButton(
            column=0,
            image="convert",
            label="IEEE754 Conversion",
            command=lambda: parent.show_frame("BinaryInput"),
        )
        self.home_root_btn = self.createHomeButton(
            column=1,
            image="root",
            label="Root Finding",
            command=lambda: parent.show_frame("RootFind"),
        )
        self.home_jacobi_btn = self.createHomeButton(
            column=2,
            image="jacobi",
            label="Jacobi Method",
            command=lambda: parent.show_frame("BinaryInput"),
        )
