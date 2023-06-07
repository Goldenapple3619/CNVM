from .casm_display import *
from .casm_constants import *

def warn_using_reg(item, i, prg, defined_vars, functions, vars):
    if (item.keyword == "using_reg"):
        warning(f"using_reg keyword found, i advice you not to use it, writing or depending on registry value can have side or unwanted effect, it's at your own risk.", i + 1)

def warn_using_instruction(item, i, prg, defined_vars, functions, vars):
    if (item.keyword == "using_instructions"):
        warning(f"using_instructions keyword found, i advice you not to use it, using raw instructions have side or unwanted effect, it's at your own risk.", i + 1)

def warn_no_main(item, i, prg, defined_vars, functions, vars):
    if ('main' not in functions):
        warning(f"no main function exist the program will be mapped in rom but never accessed", i + 1)

def warn_instruction_not_in_function(item, i, prg, defined_vars, functions, vars):
    temp = i

    if (not item.keyword.startswith('.') and not item.keyword.endswith('.') and item.keyword not in ('var', 'using_reg', 'using_instructions')):
        while (temp > -1):
            if (prg[temp].keyword.startswith('.')):
                return
            if (prg[temp].keyword.endswith('.')):
                break
            temp -= 1
        warning(f"instructions in program root will be ignored.", i + 1)

def warn_function_not_closed(item, i, prg, defined_vars, functions, vars):
    if (item.keyword.startswith('.')):
        found = 0
        for it in prg[i:]:
            if it.keyword.endswith('.') and it.keyword.startswith(item.keyword[1:]):
                found = 1
        if (not found):
            warning(f"function '{item.keyword[1:]}' is never close in this case", i + 1)

def warn_var_missing_arguments(item, i, prg, defined_vars, functions, vars):
    if (item.keyword == 'var'):
        if (len(item.value) < 1 or item.value[0] == ''):
            warning(f"variable definition with no explicit address, defaulting to 0x0F", i + 1)
            item.value.append('0x0F')
        if (len(item.value) < 2 or item.value[1] == ''):
            warning(f"variable definition at '{item.value[0]}' has no explicit name, defaulting to null.", i + 1)
            item.value.append('null')

def warn_function_call_missing_argument(item, i, prg, defined_vars, functions, vars):
    if (item.keyword in functions):
        if (len([it for it in item.value if it != '']) < len(functions[item.keyword])):
            warning(f"function call '{item.keyword}' has missing explicit arguments ({', '.join(item for item in functions[item.keyword][len([it for it in item.value if it != '']):])}), defaulting to 0x00.", i + 1)
            item.value.append('0x00')

def warn_keyword_missing_argument(item, i, prg, defined_vars, functions, vars):
    if (item.keyword in KEYWORDS and len(KEYWORDS[item.keyword]) != 0 and KEYWORDS[item.keyword][0] != '...' and item.keyword != 'var'):
        if (len([it for it in item.value if it != '']) < len(KEYWORDS[item.keyword])):
            warning(f"keyword '{item.keyword}' has missing explicit arguments ({', '.join(item for item in KEYWORDS[item.keyword][len([it for it in item.value if it != '']):])}), defaulting to 0x00.", i + 1)
            for _ in range (len([it for it in item.value if it != '']) - len(KEYWORDS[item.keyword])):
                item.value.append('0x00')

def warn_set_missing_argument(item, i, prg, defined_vars, functions, vars):
    if (item.keyword in vars):
        if (len([it for it in item.value if it != '']) < 1):
            warning(f"variable set take 1 explicit argument but 0 given, defaulting to 0x00.", i + 1)
            item.value.append('0x00')

