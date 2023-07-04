from customtkinter import (
    CTkFrame,
    CTkEntry,
    CTkButton,
    CTkLabel,
    CTkTextbox,
)
from utils import (
    colors,
    create_back_button,
    create_frame_title,
    text_font,
    btn_font,
    input_text_color,
    textbox_update,
    entry_update,
    frame_radius,
)
from equations import (
    binary_convert,
)


class BinaryInputFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=frame_radius)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame_title = create_frame_title(self, "IEEE754 Conversion: INPUT")

        input_group = CTkFrame(self, fg_color="transparent")
        input_group.grid(row=1, column=0, sticky="ew", pady=40, padx=10)
        input_group.grid_columnconfigure(2, weight=1)
        decimal_label = CTkLabel(input_group, text="Decimal Value:", font=text_font(16))
        decimal_label.grid(row=0, column=0, padx=10, sticky="w")
        self.decimal_input = CTkEntry(input_group, font=text_font(16))
        self.decimal_input.grid(
            row=0, column=1, columnspan=2, padx=5, ipadx=5, sticky="ew"
        )

        control_btn = CTkFrame(self, fg_color="transparent")
        control_btn.grid_columnconfigure(2, weight=1)
        control_btn.grid(row=2, column=0, pady=20)
        submit_btn = CTkButton(
            control_btn,
            text="Submit",
            font=btn_font,
            command=lambda: self.compute(parent),
        )
        submit_btn.grid(row=0, column=1, ipadx=10)
        back_btn = create_back_button(control_btn, command=parent.show_home)
        back_btn.grid(row=0, column=0, padx=10, ipadx=10)

    def compute(self, parent):
        decimal_value = None
        try:
            decimal_value = float(self.decimal_input.get())
        except Exception:
            print("Invalid")
            return
        parent.frames["BinaryResult"].show_results(decimal_value)
        parent.show_frame("BinaryResult")
        return


class BinaryResultFrame(CTkFrame):
    results = {
        "single": {"sign": None, "exponent": None, "mantissa": None},
        "double": {"sign": None, "exponent": None, "mantissa": None},
    }

    def __init__(self, parent):
        super().__init__(parent, corner_radius=frame_radius)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame_title = create_frame_title(self, "IEEE754 Conversion: RESULT")

        input_group = CTkFrame(self, fg_color="transparent")
        input_group.grid(row=1, column=0, sticky="ew", pady=20, padx=20)
        input_group.grid_rowconfigure(2, weight=1)
        input_group.grid_columnconfigure(0, weight=1)
        input_label = CTkLabel(input_group, text="Decimal Input:", font=text_font(16))
        input_label.grid(row=0, column=0, pady=5)
        self.input_value = CTkEntry(input_group, font=text_font(20), justify="center")
        self.input_value.grid(row=2, column=0, sticky="ew", ipady=5)

        output_group = CTkFrame(self, fg_color="transparent")
        output_group.grid(row=3, column=0, sticky="ew", pady=20, padx=20)
        output_group.grid_rowconfigure(3, weight=1)
        output_label = CTkLabel(output_group, text="Binary Output:", font=text_font(16))
        output_label.grid(row=0, column=0, pady=5)

        self.create_output_group(output_group, "single", 1)
        self.create_output_group(output_group, "double", 2)

        back_btn = create_back_button(self, command=parent.show_home)
        back_btn.grid(row=4, column=0, padx=10, pady=20, ipadx=10, sticky="e")

    def create_output_group(self, parent, convert_type, row):
        output_group = CTkFrame(parent, fg_color="transparent")
        output_group.grid(row=row, column=0, sticky="ew", pady=10)
        output_group.grid_columnconfigure(3, weight=1)

        def create_output_textbox(parent, width):
            return CTkTextbox(
                parent,
                font=text_font(16),
                height=60,
                width=width,
                activate_scrollbars=False,
            )

        self.results[convert_type]["sign"] = create_output_textbox(output_group, 70)
        self.results[convert_type]["exponent"] = create_output_textbox(
            output_group, 270
        )
        self.results[convert_type]["mantissa"] = create_output_textbox(
            output_group, 390
        )
        columns = ["sign", "exponent", "mantissa"]
        for i in range(len(columns)):
            self.results[convert_type][columns[i]].grid(
                row=0, column=i, padx=5, sticky="ew"
            )

    def show_results(self, decimal_value):
        results = binary_convert(decimal_value)
        entry_update(self.input_value, decimal_value)
        for convert_type in ["single", "double"]:
            for col in ["sign", "exponent", "mantissa"]:
                textbox_update(
                    self.results[convert_type][col], results[convert_type][col]
                )
