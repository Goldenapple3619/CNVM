from .casm_abc import *
from .casm_common import *

def casm_lex_program(argv):
    temp: list = []

    for it in argv[1:]:
        prg: str = read_program(it)
        prg_split: list = [item.split('//')[0].strip() for item in prg.replace('\\\n', '').split('\n') if item.split('//')[0].replace(' ', '').replace('\t', '') != '']
        temp += [Token(item.split(' ')[0], [i.strip() for i in (' '.join(item.split(' ')[1:])).split(',')]) for item in prg_split]
    return (temp)
