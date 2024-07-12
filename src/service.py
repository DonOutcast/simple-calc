from utils import Lexemes


def calculate(expression: str) -> int:
    output, curr, sign, stack = 0, 0, 1, []
    for c in expression:
        if c.isdigit():
            curr = (curr * 10) + int(c)

        elif c in (Lexemes.plus.value, Lexemes.minus.value):
            output += curr * sign
            curr = 0
            if c == Lexemes.plus.value:
                sign = 1

            else:
                sign = -1

    return output + (curr * sign)
