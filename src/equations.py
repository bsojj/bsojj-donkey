from sympy import symbols, lambdify


def bracket_loop(expression, left, right, precision, mid_equation):
    iterations = []
    x = symbols("x")
    f = lambdify([x], expression)
    precision_float = 4 / (10**precision)
    output_precision = precision + 2
    left = round(left, output_precision)
    right = round(right, output_precision)
    while left < right:
        left_y = round(f(left), output_precision)
        right_y = round(f(right), output_precision)

        mid = round(mid_equation(left, right), output_precision)
        mid_y = round(f(mid), output_precision)

        iterations.append(
            {
                "left_x": left,
                "mid_x": mid,
                "right_x": right,
                "left_y": left_y,
                "mid_y": mid_y,
                "right_y": right_y,
            }
        )
        if abs(mid_y) <= precision_float:
            break
        elif mid_y * left_y < 0:
            right = mid
        else:
            left = mid
    return iterations


def root_find(expression, left, right, precision, mid_equation, loop):
    return loop(expression, left, right, precision, mid_equation)


def falsi_compute(expression, left, right, precision):
    f = lambdify([symbols("x")], expression)
    return root_find(
        expression,
        left,
        right,
        precision,
        lambda l, r: l + (r - l) * (f(l) / (f(l) - f(r))),
        bracket_loop,
    )


def bisection_compute(expression, left, right, precision):
    return root_find(
        expression, left, right, precision, lambda l, r: (l + r) / 2, bracket_loop
    )


def secant_compute(expression, a, b, precision):
    def secant_loop(expression, a, b, precision, mid_equation):
        y = 1
        iterations = []
        f = lambdify([symbols("x")], expression)
        precision_float = 4 / (10**precision)
        output_precision = precision + 2
        while abs(y) > precision_float:
            a_y = round(f(a), output_precision)
            b_y = round(f(b), output_precision)

            new_x = round(mid_equation(a, b, a_y, b_y), output_precision)
            new_y = round(f(new_x), output_precision)

            iterations.append(
                {
                    "a_x": a,
                    "b_x": b,
                    "new_x": new_x,
                    "a_y": a_y,
                    "b_y": b_y,
                    "new_y": new_y,
                }
            )
            a = b
            b = new_x
            y = new_y
        return iterations

    return root_find(
        expression,
        a,
        b,
        precision,
        lambda a, b, ay, by: a - ((ay * (a - b)) / (ay - by)),
        secant_loop,
    )


def newton_raphson_compute(expression, initial_x, precision):
    y = 1
    iterations = []
    f = lambdify([symbols("x")], expression)
    dx = lambdify([symbols("x")], expression.diff(symbols("x")))
    precision_float = 4 / (10**precision)
    output_precision = precision + 2
    old_x = round(initial_x, output_precision)
    while abs(y) > precision_float:
        old_y = round(f(old_x), output_precision)
        new_x = round(old_x - old_y / dx(old_x), output_precision)
        new_y = round(f(new_x), output_precision)

        iterations.append(
            {
                "old_x": old_x,
                "new_x": new_x,
                "old_y": old_y,
                "new_y": new_y,
            }
        )
        old_x = new_x
        y = new_y
    return iterations


def binary_convert(num):
    BIT_PRECISION_LEN = 53
    SIGNIFICAND_LEN = 52
    EXPONENT_LEN = 11
    EXPONENT_BIAS = 1023
    SINGLE_SIGNIFICAND_LEN = 23
    SINGLE_EXPONENT_LEN = 8
    SINGLE_EXPONENT_BIAS = 127

    left_digits = abs(int(num))
    right_digits = num - int(num)

    if num < 0:
        sign = 1
    else:
        sign = 0

    left_bin = ""
    count = 0
    while left_digits > 0:
        count += 1
        left_bin += str(left_digits % 2)
        left_digits //= 2
    left_bin = left_bin[::-1]

    right_bin = ""
    while right_digits != 0 and count < BIT_PRECISION_LEN:
        count += 1
        right_bin += str(int(right_digits * 2))
        right_digits = (right_digits * 2) - int(right_digits * 2)

    significand = left_bin + right_bin
    if not right_bin == "":
        start = right_bin.index("1") + 1
    else:
        start = 0
    if len(left_bin) == 0:
        exponent = (right_bin.index("1") + 1) * -1
    else:
        exponent = len(left_bin) - 1

    bias = EXPONENT_BIAS + exponent
    single_bias = SINGLE_EXPONENT_BIAS + exponent
    exponent_bin = ""
    single_exponent_bin = ""

    while bias > 0:
        exponent_bin += str(bias % 2)
        bias //= 2
    while single_bias > 0:
        single_exponent_bin += str(single_bias % 2)
        single_bias //= 2

    return {
        "double": {
            "sign": sign,
            "exponent": exponent_bin[::-1].rjust(EXPONENT_LEN, "0"),
            "mantissa": significand[start : start + SIGNIFICAND_LEN].ljust(
                SIGNIFICAND_LEN, "0"
            ),
        },
        "single": {
            "sign": sign,
            "exponent": single_exponent_bin[::-1].rjust(SINGLE_EXPONENT_LEN, "0"),
            "mantissa": significand[start : start + SINGLE_SIGNIFICAND_LEN].ljust(
                SINGLE_SIGNIFICAND_LEN, "0"
            ),
        },
    }
