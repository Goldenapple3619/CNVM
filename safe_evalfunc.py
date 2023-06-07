from typing import Any, Mapping

ALLOWED_FUNCTIONS = [
    "sin",
    "cos",
    "tan",
    "sinh",
    "cosh",
    "tanh",
    "acos",
    "atan",
    "asin",
    "asinh",
    "atanh",
    "acosh",
    "log10",
    "log2",
    "log",
    "exp",
    "+",
    "-",
    "*",
    "/",
    "%",
    ".",
    "(",
    ")",
    " "
]

def safe_eval(__source: str, __globals: dict = None, __locals: Mapping = None) -> Any:
    check: str = __source

    for item in ALLOWED_FUNCTIONS:
        check = check.replace(item, "")

    if (not check.isnumeric()):
        return (None)

    return (eval(__source, __globals, __locals))

if __name__ == "__main__":
    while 1:
        print(safe_eval(input("> ")))