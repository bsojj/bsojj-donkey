from sympy import symbols, sympify, lambdify
from equations import newton_raphson_compute
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


class NewtonRaphsonInputFrame(CTkFrame):
    def create_textbox(self, row, label):
        group = CTkFrame(self.container, fg_color="transparent")
        group.grid(row=row, column=0, pady=10, sticky="ew")
        group.grid_columnconfigure(2, weight=1)

        self.labels.append(CTkLabel(group, font=("Lilita One", 16), text=label))
        self.labels[-1].grid(row=0, column=0, sticky="w", padx=5)

        text_box = CTkEntry(group, font=text_font(16))
        text_box.grid(row=0, column=1, padx=10, columnspan=2, sticky="ew")

        return text_box

    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.labels = []
        self.frame_title = create_frame_title(self, "Newton-Raphson Method: INPUT")

        self.container = CTkFrame(self, fg_color="transparent")
        self.container.grid(row=1, column=0, sticky="ew", padx=20, pady=20)
        self.container.grid_rowconfigure(4, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.equation_input = self.create_textbox(0, "Equation:")
        self.initial_input = self.create_textbox(1, "Initial Value for xₒ:")
        self.precision_input = self.create_textbox(2, "Precision(Decimal Places):")
        self.equation_input.insert(0, "4x^2 + 2x - 5")
        self.initial_input.insert(0, "0")
        self.precision_input.insert(0, "4")

        self.control_group = CTkFrame(self.container, fg_color="transparent")
        self.control_group.grid_columnconfigure(2, weight=1)
        self.control_group.grid(row=3, column=0, pady=20, sticky="e")
        self.compute_btn = CTkButton(
            self.control_group,
            text="Compute",
            font=btn_font,
            command=lambda: self.validate(parent),
        )
        self.compute_btn.grid(row=0, column=1, padx=10)
        self.back_btn = create_back_button(
            self.control_group, command=lambda: parent.show_frame("RootFind")
        )
        self.back_btn.grid(row=0, column=0, padx=10)

    def compute(
        self,
        parent,
        expression,
        old_x,
        precision,
        original_expression,
        derivative,
    ):
        parent.frames["NewtonRaphsonResult"].show_result(
            original_expression,
            derivative,
            iterations=newton_raphson_compute(expression, old_x, precision),
            precision=precision,
        )
        parent.show_frame("NewtonRaphsonResult")

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

        derivative = None
        try:
            derivative = expression.diff(x)
        except Exception:
            print("Unable to get derivative from expression")
            return

        initial_x = None
        try:
            initial_x = float(self.initial_input.get())
        except Exception:
            print("Invalid Initial Value")
            return

        precision = None
        try:
            precision = int(self.precision_input.get())
            if precision < 0:
                raise Exception("Invalid Precision")
        except Exception:
            print("Invalid Precision")
            return

        self.compute(
            parent,
            expression,
            initial_x,
            precision,
            original_expression,
            derivative,
        )


class NewtonRaphsonResultFrame(CTkFrame):
    def create_text_value(self, column, row, label):
        container = CTkFrame(self.value_group, fg_color="transparent")
        container.grid(row=row, column=column, sticky="ew", pady=10)
        container.grid_columnconfigure(2, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.labels.append(CTkLabel(container, font=text_font(16), text=label))
        self.labels[-1].grid(row=0, column=0, sticky="w", padx=5)
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
        self.labels = []
        self.headers = []

        self.frame_title = create_frame_title(self, "Newton-Raphson Method: RESULT")

        self.value_group = CTkFrame(self, fg_color="transparent")
        self.value_group.grid(row=1, column=0, sticky="ew", padx=100)
        self.value_group.grid_rowconfigure(3, weight=1)
        self.value_group.grid_columnconfigure(0, weight=1)

        self.expression_value = self.create_text_value(0, 0, "Expression:")
        self.initial_value = self.create_text_value(0, 1, "f(xₒ)₀:")
        self.derivative_value = self.create_text_value(0, 2, "Derivative:")
        self.precision_value = self.create_text_value(1, 0, "Precision:")
        self.result_x = self.create_text_value(1, 1, "X:")
        self.result_y = self.create_text_value(1, 2, "Y:")
        self.output_table = None

        self.back_btn = create_back_button(
            self, command=lambda: parent.show_frame("NewtonRaphsonInput")
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
            width=190,
            fg_color=fg_color,
            text_color=text_color,
        )

    def create_table_row(self, row, data, bold=False):
        cells = [
            self.create_table_cell(data["old_x"], bold),
            self.create_table_cell(data["new_x"], bold),
            self.create_table_cell(data["old_y"], bold),
            self.create_table_cell(data["new_y"], bold),
        ]
        for i in range(len(cells)):
            cells[i].grid(row=row, column=i, sticky="ew")
        return

    def show_result(self, expression, derivative, iterations, precision):
        if self.output_table is not None:
            self.output_table.destroy()
        if len(iterations) > 5:
            self.output_table = CTkScrollableFrame(
                self,
                fg_color="transparent",
                height=60,
                scrollbar_button_color=scroll_btn_color,
                scrollbar_button_hover_color=scroll_hover_color,
            )
        else:
            self.output_table = CTkFrame(self, fg_color="transparent")
        self.output_table.grid_columnconfigure(4, weight=1)
        self.output_table.grid(row=2, column=0, sticky="new", padx=20, pady=10)
        self.output_table.grid_rowconfigure(len(iterations) + 1, weight=1)

        self.output_table_headers = self.create_table_row(
            0,
            {
                "old_x": "xₒ",
                "new_x": "xₙ",
                "old_y": "f(xₒ)",
                "new_y": "f(xₙ)",
            },
            bold=True,
        )

        for i in range(len(iterations)):
            self.create_table_row(i + 1, iterations[i])

        entry_update(self.expression_value, expression)
        entry_update(self.initial_value, iterations[0]["old_y"])
        entry_update(self.derivative_value, derivative.__str__().replace("**", "^").replace("*x", "x"))
        entry_update(self.precision_value, 1 / (10**precision))
        entry_update(self.result_x, iterations[-1]["new_x"])
        y_precision = f".{precision+2}f"
        entry_update(self.result_y, format(iterations[-1]["new_y"], y_precision))
