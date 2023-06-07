
def nice(text, new):
    print(f"\033[38;5;10m\033[1mcompiled:\033[0m \033[38;5;14m\033[1m{text}\033[0m -> \033[38;5;11m\033[1m{new}\033[0m.")

def warning(text, y):
    print(f"\033[38;5;13m\033[1mwarning:\033[0m \033[38;5;14m\033[1m{y}:\033[0m {text}\n")

def error(text, y):
    print(f"\033[38;5;9m\033[1merror:\033[0m \033[38;5;14m\033[1m{y}:\033[0m {text}\n")
