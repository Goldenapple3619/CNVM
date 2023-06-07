from .casm_display   import *
from .casm_common    import *
from .casm_constants import *
from .casm_abc       import *
from .casm_lexer     import *
from .casm_compile   import *

from os.path import isfile

def casm_cli(argc: int, argv: list) -> int:
    if (argc == 1):
        error("missing argument 'file'", 0)
        return (1)

    if (not all(map(isfile, argv[1:]))):
        error("invalid file found", 0)
        return (1)

    has_extension = all(map(lambda x: x == 'rsm', map(lambda x: x.split('.')[-1], argv[1:])))

    if (not has_extension):
        error("invalid extension found.", 0)
        return (1)

    lexed = casm_lex_program(argv)
    name = ('.'.join(argv[1].split('.')[:-1])).split('\\')[-1].split('/')[-1]

    show_warn(lexed)
    if (show_errors(lexed)):
        return (1)

    casm_compile(lexed).save_to_file(name + '.out')

    for it in argv[1:]:
        nice(it, name + '.out')

    return (0)
