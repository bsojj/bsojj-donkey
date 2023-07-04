from frames.bisection import BisectionInputFrame, BisectionResultFrame
from equations import falsi_compute


class FalsiInputFrame(BisectionInputFrame):
    def __init__(self, parent):
        super().__init__(parent)

    def show_results(
        self, parent, expression, left, right, precision
    ):
        iterations = falsi_compute(expression, left, right, precision)
        parent.frames["FalsiResult"].compute(
            iterations, precision
        )
        parent.show_frame("FalsiResult")


class FalsiResultFrame(BisectionResultFrame):
    def __init__(self, parent):
        super().__init__(parent)
