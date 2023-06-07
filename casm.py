from sys import (argv, exit)

from src.casm_lang import *

if __name__ == "__main__":
    exit(casm_cli(len(argv), argv))
