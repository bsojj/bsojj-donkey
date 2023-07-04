from sympy import symbols, sympify, lambdify
from equations import bisection_compute
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
    btn_font,
    text_font,
    input_text_color,
    scroll_btn_color,
    scroll_hover_color,
    entry_update,
)


class BisectionInputFrame(CTkFrame):
    def create_textbox(self, row, label):
        group = CTkFrame(self.container, fg_color="transparent")
        group.grid(row=row, column=0, pady=10, sticky="ew")
        group.grid_columnconfigure(2, weight=1)

        text_label = CTkLabel(group, font=("Lilita One", 16), text=label)
        text_label.grid(row=0, column=0, sticky="w", padx=5)

        text_box = CTkEntry(group, font=text_font(16))
        text_box.grid(row=0, column=1, padx=10, columnspan=2, sticky="ew")

        return text_box

    def __init__(self, parent):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)
        self.container = CTkFrame(self, fg_color="transparent")
        self.container.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
        self.container.grid_rowconfigure(5, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.equation_input = self.create_textbox(0, "Equation:")
        self.left_input = self.create_textbox(1, "Initial Value for xₗ:")
        self.right_input = self.create_textbox(2, "Initial Value for xᵣ:")
        self.precision_input = self.create_textbox(3, "Precision(Decimal Places):")
        self.equation_input.insert(0, "4x^2 + 2x - 5")
        self.left_input.insert(0, "0")
        self.right_input.insert(0, "1")
        self.precision_input.insert(0, "4")

        self.control_group = CTkFrame(self.container, fg_color="transparent")
        self.control_group.grid_columnconfigure(2, weight=1)
        self.control_group.grid(row=4, column=0, pady=20, sticky="e")
        self.compute_btn = CTkButton(
            self.control_group,
            text="Compute",
            font=btn_font,
            command=lambda: self.compute(parent),
        )
        self.compute_btn.grid(row=0, column=1, padx=10)
        self.back_btn = create_back_button(
            self.control_group, command=lambda: parent.show_frame("RootFind")
        )
        self.back_btn.grid(row=0, column=0, padx=10)

    def show_results(
        self, parent, expression, left, right, precision
    ):
        parent.frames["BisectionResult"].compute(
            iterations=bisection_compute(expression, left, right, precision),
            precision=precision,
        )
        parent.show_frame("BisectionResult")

    def compute(self, parent):
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

        f = lambdify([x], expression)

        if x_left > x_right or f(x_left) * f(x_right) >= 0:
            print("Expression cannot be evaluated with given values")
            return

        precision = None
        try:
            precision = int(self.precision_input.get())
            if precision < 0:
                raise Exception("Invalid Precision")
        except Exception:
            print("Invalid Precision")
            return

        self.show_results(
            parent, original_expression, expression, x_left, x_right, precision
        )


class BisectionResultFrame(CTkFrame):
    def create_text_value(self, column, row, label):
        container = CTkFrame(self.value_group, fg_color="transparent")
        container.grid(row=row, column=column, sticky="ew", pady=10)
        container.grid_columnconfigure(2, weight=1)
        container.grid_rowconfigure(0, weight=1)

        text_label = CTkLabel(container, font=text_font(16), text=label)
        text_label.grid(row=0, column=0, sticky="w", padx=5)
        text_value = CTkEntry(
            container,
            font=text_font(16),
            corner_radius=5,
        )
        text_value.grid(row=0, column=1, columnspan=2, sticky="ew", padx=5)

        return text_value

    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame_title = CTkLabel(
            self,
            font=text_font(28),
            text="Result",
            fg_color=colors["sky-600"],
            text_color=colors["gray-50"],
            corner_radius=10,
        )
        self.frame_title.grid(row=0, column=0, sticky="ew", ipady=10)
        self.value_group = CTkFrame(self, fg_color="transparent")
        self.value_group.grid(row=1, column=0, sticky="ew", padx=100, pady=5)
        self.value_group.grid_rowconfigure(3, weight=1)
        self.value_group.grid_columnconfigure(0, weight=1)

        self.left_value = self.create_text_value(column=0, row=0, label="f(xₗ)₀:")
        self.right_value = self.create_text_value(0, 1, "f(xᵣ)₀:")
        self.precision_value = self.create_text_value(0, 2, "Precision:")
        self.result_x = self.create_text_value(1, 0, "X:")
        self.result_y = self.create_text_value(1, 1, "Y:")

        self.output_table = CTkScrollableFrame(
            self,
            fg_color="transparent",
            height=200,
            scrollbar_button_color=scroll_btn_color,
            scrollbar_button_hover_color=scroll_hover_color,
        )
        self.output_table.grid_columnconfigure(6, weight=1)
        self.output_table.grid(row=2, column=0, sticky="new", padx=20)

        self.back_btn = create_back_button(
            self, command=lambda: parent.show_frame("BisectionInput")
        )
        self.back_btn.grid(row=3, column=0, sticky="e", padx=20, pady=20)

    def create_table_cell(self, value, bold=False):
        if bold:
            font = ("Lilita One", 16)
            text_color = (colors["gray-50"], colors["gray-700"])
            fg_color = (colors["neutral-900"], colors["gray-200"])
        else:
            font = ("Lilita One", 14)
            text_color = (colors["neutral-800"], colors["gray-200"])
            fg_color = (colors["gray-50"], colors["gray-700"])

        return CTkLabel(
            self.output_table,
            text=value,
            font=font,
            width=125,
            fg_color=fg_color,
            text_color=text_color,
        )

    def create_table_row(self, row, data, bold=False):
        cells = [
            self.create_table_cell(data["left_x"], bold),
            self.create_table_cell(data["mid_x"], bold),
            self.create_table_cell(data["right_x"], bold),
            self.create_table_cell(data["left_y"], bold),
            self.create_table_cell(data["mid_y"], bold),
            self.create_table_cell(data["right_y"], bold),
        ]
        for i in range(len(cells)):
            cells[i].grid(row=row, column=i, sticky="ew")
        return

    def compute(self, iterations, precision):
        self.output_table.grid_rowconfigure(len(iterations) + 1, weight=1)
        self.output_table_headers = self.create_table_row(
            0,
            {
                "left_x": "xₗ",
                "mid_x": "xₘ",
                "right_x": "xᵣ",
                "left_y": "f(xₗ)",
                "mid_y": "f(xₘ)",
                "right_y": "f(xᵣ)",
            },
            bold=True,
        )

        for i in range(len(iterations)):
            self.create_table_row(i + 1, iterations[i])

        entry_update(self.left_value, iterations[0]["left_y"])
        entry_update(self.right_value, iterations[0]["right_y"])
        entry_update(self.precision_value, 1 / (10**precision))
        entry_update(self.result_x, iterations[-1]["mid_x"])
        entry_update(self.result_y, iterations[-1]["mid_y"])
