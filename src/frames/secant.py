from sympy import symbols, sympify, lambdify
from equations import secant_compute
from customtkinter import (
    CTkScrollableFrame,
    CTkFrame,
    CTkButton,
    CTkLabel,
    CTkEntry,
)
from utils import (
    colors,
    create_back_button,
    create_frame_title,
    btn_font,
    text_font,
    scroll_btn_color,
    scroll_hover_color,
    entry_update,
)
from frames.bisection import BisectionInputFrame, BisectionResultFrame


class SecantInputFrame(BisectionInputFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.frame_title.configure(text="Secant Method: INPUT")

        self.labels[1].configure(text="Initial Value for xₐ:")
        self.labels[2].configure(text="Initial Value for xᵥ:")

    def compute(self, parent, expression, left, right, precision):
        parent.frames["SecantResult"].show_result(
            iterations=secant_compute(expression, left, right, precision),
            precision=precision,
        )
        parent.show_frame("SecantResult")

    def validate(self, parent):
        x = symbols("x")
        expression = None
        original_expression = self.equation_input.get()
        try:
            python_expression = original_expression.replace("^", "**").replace(
                "x", " * x"
            )
            expression = sympify(python_expression)
            expression.subs(x, 1)
        except Exception:
            print("Invalid expression")
            return

        x_left = None
        try:
            x_left = float(self.left_input.get())
        except Exception:
            print("Invalid Left Value")
            return

        x_right = None
        try:
            x_right = float(self.right_input.get())
        except Exception:
            print("Invalid Right Value")
            return

        precision = None
        try:
            precision = int(self.precision_input.get())
            if precision < 0:
                raise Exception("Invalid Precision")
        except Exception:
            print("Invalid Precision")
            return

        self.compute(parent, expression, x_left, x_right, precision)


class SecantResultFrame(BisectionResultFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.frame_title.configure(text="Secant Method: RESULT")

        self.labels[0].configure(text="f(xₐ):")
        self.labels[1].configure(text="f(xᵥ):")

        self.back_btn.configure(command=lambda: parent.show_frame("SecantInput"))

    def create_table_row(self, row, data, bold=False):
        cells = [
            self.create_table_cell(data["a_x"], bold),
            self.create_table_cell(data["b_x"], bold),
            self.create_table_cell(data["new_x"], bold),
            self.create_table_cell(data["a_y"], bold),
            self.create_table_cell(data["b_y"], bold),
            self.create_table_cell(data["new_y"], bold),
        ]
        for i in range(len(cells)):
            cells[i].grid(row=row, column=i, sticky="ew")
        return

    def show_result(self, iterations, precision):
        if self.output_table is not None:
            self.output_table.destroy()
        if len(iterations) > 6:
            self.output_table = CTkScrollableFrame(
                self,
                fg_color="transparent",
                height=200,
                scrollbar_button_color=scroll_btn_color,
                scrollbar_button_hover_color=scroll_hover_color,
            )
        else:
            self.output_table = CTkFrame(self, fg_color="transparent")
        self.output_table.grid_columnconfigure(6, weight=1)
        self.output_table.grid(row=2, column=0, sticky="new", padx=20, pady=40)
        self.output_table.grid_rowconfigure(len(iterations) + 1, weight=1)

        self.labels[0].configure(text="f(xₐ):")
        self.labels[1].configure(text="f(xᵥ):")
        self.output_table_headers = self.create_table_row(
            0,
            {
                "a_x": "xₐ",
                "b_x": "xᵥ",
                "new_x": "xₙ",
                "a_y": "f(xₐ)",
                "b_y": "f(xᵥ)",
                "new_y": "f(xₙ)",
            },
            bold=True,
        )

        for i in range(len(iterations)):
            self.create_table_row(i + 1, iterations[i])

        entry_update(self.left_value, iterations[0]["a_y"])
        entry_update(self.right_value, iterations[0]["b_y"])
        entry_update(self.precision_value, 1 / (10**precision))
        entry_update(self.result_x, iterations[-1]["new_x"])
        y_precision = f".{precision+2}f"
        entry_update(self.result_y, format(iterations[-1]["new_y"], y_precision))
