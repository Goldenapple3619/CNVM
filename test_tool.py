from sys import argv
import sys
from importlib import import_module
from os.path import isfile

OK = "\033[38;5;10m\033[1mOK\033[0m"
FAIL = "\033[38;5;9m\033[1mFAIL\033[0m"
CRASH = "\033[38;5;9m\033[1mCRASH!\033[0m"

class Token:
    def __init__(self, balise, values) -> None:
        self.values = values
        self.balise = balise

    def __repr__(self) -> str:
        return self.balise + ':\n    ' + '\n    '.join([f'{item} -> {self.values[item]}' for item in self.values])

def read_program(path: str) -> str:
    data = ''

    with open(path) as f:
        data = f.read().strip()
    return (data)

def run_test(tests: list):
    status = {"pass": 0, "fail": 0, 'crash': 0, 'total': len(tests)}
    for item in tests:
        global_vars = {'test': 0}
        if ('name' in item.values):
            print(f'running: {item.values["name"]}:')
        if ('imports' in item.values):
            for it in item.values["imports"].split(','):
                it = it.strip()
                print(f'  importing: {it}...\b\b\b', end='', flush=True)
                try:
                    if ('.' in it):
                        global_vars[it.split('.')[-1]] = getattr(import_module('.'.join(it.split('.')[:-1])), it.split('.')[-1])
                    else:
                        global_vars[it] = import_module(it)
                    print(f' - [{OK}]')
                except Exception as e:
                    print(f' - [{FAIL}] {e}')
        if ('run' in item.values):
            local = {'test': 0}
            print(f'  running tests ({len(item.values["run"].split(";"))}l)...\b\b\b', end='', flush=True)
            prg = 'def main():' + '\n'.join(['    ' + it for it in item.values['run'].split(';')]) + '\ntest = main()'
            temp = sys.stdout
            try:
                ret = exec(prg, global_vars, local)
                sys.stdout = temp
                print(f' - [{OK if not local["test"] else FAIL}]\n')
                if not local["test"]:
                    status['pass'] += 1
                else:
                    status["fail"] += 1
            except Exception as e:
                sys.stdout = temp
                print(f' - [{CRASH}] {e}\n')
                status['crash'] += 1
    print(f'Result: [{status["pass"]}/{status["total"]}] {format(round(status["pass"] * 100 / status["total"], 2), ".2f")}% - [\033[38;5;10m\033[1mPASSED\033[0m: {status["pass"]} | \033[38;5;11m\033[1mFAIL\033[0m: {status["fail"]} | \033[38;5;9m\033[1mCRASH\033[0m: {status["crash"]}]')

def lexer(raw_program):
    tokens = []
    balise = None
    values = {}

    for item in raw_program:
        if item == '[/end]' and balise is not None:
            tokens.append(Token(balise, values))
            balise = None
            values = {}
        elif item.startswith('[') and item.endswith(']') and balise is None:
            balise = ']'.join(('['.join(item.split('[')[1:])).split(']')[:-1]).strip()
        elif balise is not None:
            values[item.split(':')[0].strip()] = ':'.join(item.split(':')[1:]).strip()

    return (tokens)


def test_cli(argc, argv):
    tokens: list = []

    if (argc < 2):
        return (1)
    
    for item in argv[1:]:
        print(f"reading: {item}...\b\b\b", end='', flush=True)
        if (isfile(item)):
            temp = read_program(item).replace('\\\n', '').split('\n')
            temp_tokens = lexer(temp)
            tokens += temp_tokens
            print(f" - [{OK}]")
        else:
            print(f' - [{FAIL}]')
    print('')
    run_test([item for item in tokens if item.balise == 'test'])


if __name__ == "__main__":
    exit(test_cli(len(argv), argv))
