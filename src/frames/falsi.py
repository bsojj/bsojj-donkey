from frames.bisection import BisectionInputFrame, BisectionResultFrame
from equations import falsi_compute


class FalsiInputFrame(BisectionInputFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.frame_title.configure(text="Falsi Method: INPUT")
        self.back_btn.configure(command=lambda: parent.show_frame("RootFind"))

    def compute(self, parent, expression, left, right, precision):
        iterations = falsi_compute(expression, left, right, precision)
        parent.frames["FalsiResult"].show_result(iterations, precision)
        parent.show_frame("FalsiResult")


class FalsiResultFrame(BisectionResultFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.frame_title.configure(text="Falsi Method: RESULT")
        self.back_btn.configure(command=lambda: parent.show_frame("FalsiInput"))
