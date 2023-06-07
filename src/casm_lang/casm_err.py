from .casm_display import *
from .casm_constants import *

def err_invalid_using_reg(item, i, prg, defined_vars, functions, vars):
    if (item.keyword == "using_reg"):
        for reg in item.value:
            if reg not in ('x', 'y', 'temp', 'fetched', 'prg_device', 'mem_device', 'ptr_prg', 'ptr_mem'):
                error(f"registry '{reg}' does not exist.", i + 1)
                return (1)
    return (0)

def err_double_function_definition(item, i, prg, defined_vars, functions, vars):
    if (item.keyword.startswith('.')):
        for j, it in enumerate(prg[i + 1:]):
            if it.keyword.startswith('.') and it.keyword[1:] == item.keyword[1:]:
                error(f"double definition of function '{item.keyword[1:]}' -> {j + i + 2}", i + 1)
                return (1)
    return (0)

def err_nested_function(item, i, prg, defined_vars, functions, vars):
    if (item.keyword.startswith('.')):
        for j, it in enumerate(prg[i + 1:]):
            if it.keyword.endswith('.') and it.keyword.startswith(item.keyword[1:]):
                break
            if it.keyword.startswith('.'):
                error(f"you cannot nest functions ('{item.keyword[1:]}' -> '{it.keyword[1:]}').", j + i + 1 + 1)
                return (1)
    return (0)

def err_unknow_keyword(item, i, prg, defined_vars, functions, vars):
    if (not item.keyword.startswith('.') and not item.keyword.endswith('.') and item.keyword not in KEYWORDS and item.keyword not in defined_vars):
        error(f"unknow keyword / variable '{item.keyword}'.", i + 1)
        return (1)
    return (0)

def err_double_variable_definition(item, i, prg, defined_vars, functions, vars):
    if (item.keyword == "var"):
        for j, it in enumerate(prg[i + 1:]):
            if it.keyword == "var" and item.value[1] == it.value[1]:
                error(f"double definition of variable '{item.value[1]}' -> {j + i + 2}", i + 1)
                return (1)
    return (0)

def err_too_many_argument_in_function_call(item, i, prg, defined_vars, functions, vars):
    if (item.keyword in functions):
        if (len([it for it in item.value if it != '']) > len(functions[item.keyword])):
            error(f"function call '{item.keyword}' has too many argument ({len([it for it in item.value if it != ''])} > {len(functions[item.keyword])})", i + 1)
            return (1)
    return (0)

def err_variable_not_exist(item, i, prg, defined_vars, functions, vars):
    for j, it in enumerate(item.value):
        if (it.startswith('$') and it[1:] not in vars):
            error(f"variable '{it[1:]}' does not exist.", i + 1)
            return (1)
    return (0)

def err_keyword_too_many_argument(item, i, prg, defined_vars, functions, vars):
    if (item.keyword in KEYWORDS and (KEYWORDS[item.keyword] == () or KEYWORDS[item.keyword][-1] != '...')):
        if (len([it for it in item.value if it != '']) > len(KEYWORDS[item.keyword])):
            error(f"keyword '{item.keyword}' take only {len(KEYWORDS[item.keyword])} arguments ({', '.join(item for item in KEYWORDS[item.keyword])}), but {len([it for it in item.value if it != ''])} given.", i + 1)
            return (1)
    return (0)

def err_variable_set(item, i, prg, defined_vars, functions, vars):
    if (item.keyword in vars):
        if (len([it for it in item.value if it != '']) > 1):
            error(f"variable set only take 1 argument, but {len([it for it in item.value if it != ''])} given.", i + 1)
            return (1)
    return (0)

def err_main_argument(item, i, prg, defined_vars, functions, vars):
    if item.keyword.startswith('.') and item.keyword[1:] == 'main':
        if (len([it for it in item.value if it != '']) != 0):
            error(f"main function should have no argument but in this case it take {len([it for it in item.value if it != ''])}.", i + 1)
            return (1)
    return (0)
