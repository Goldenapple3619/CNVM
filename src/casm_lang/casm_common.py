from .casm_constants import *
from .casm_err import *
from .casm_warn import *

ERROR_HANDLERS = (
    err_invalid_using_reg,
    err_double_function_definition,
    err_nested_function,
    err_unknow_keyword,
    err_double_variable_definition,
    err_too_many_argument_in_function_call,
    err_variable_not_exist,
    err_keyword_too_many_argument,
    err_variable_set,
    err_main_argument
)

WARNING_HANDLERS = (
    warn_using_reg,
    warn_using_instruction,
    warn_function_not_closed,
    warn_var_missing_arguments,
    warn_function_call_missing_argument,
    warn_keyword_missing_argument,
    warn_set_missing_argument,
    warn_instruction_not_in_function
)

def read_program(path: str) -> str:
    data = ''

    with open(path) as f:
        data = f.read()
    return (data)

def show_warn(prg):
    functions = {item.keyword[1:]: item.value for item in prg if item.keyword.startswith('.')}
    vars = {*{item.value[1] for item in prg if item.keyword == 'var'}, *{i for item in prg if item.keyword.startswith('.') for i in item.value}}
    defined_vars = (*[item.keyword[1:] for item in prg if item.keyword.startswith('.')], *[item.value[1] for item in prg if item.keyword == 'var'])

    any(tuple(
        obj for item in
        map(
            lambda item: list(
                map(
                    lambda func: func(item[1], item[0], prg, defined_vars, functions, vars),
                    WARNING_HANDLERS
                )
            ),
            enumerate(prg)
        )
        for obj in item
    ))
    warn_no_main(None, len(prg), prg, defined_vars, functions, vars)

def show_errors(prg):
    defined_vars = (*[item.keyword[1:] for item in prg if item.keyword.startswith('.')], *[item.value[1] for item in prg if item.keyword == 'var'])
    functions = {item.keyword[1:]: item.value for item in prg if item.keyword.startswith('.')}
    vars = {*{item.value[1] for item in prg if item.keyword == 'var'}, *{i for item in prg if item.keyword.startswith('.') for i in item.value}}

    return any(tuple(
        obj for item in
        map(
            lambda item: list(
                map(
                    lambda func: func(item[1], item[0], prg, defined_vars, functions, vars),
                    ERROR_HANDLERS
                )
            ),
            enumerate(prg)
        )
        for obj in item
    ))

def get_content_function(prg):
    inside = 0
    actual = None
    functions = {}

    for item in prg:
        if (item.keyword.startswith('.')):
            inside = 1
            actual = item.keyword[1:]
            functions[actual] = []
        elif (item.keyword.endswith('.')):
            inside = 0
            actual = None
        elif actual != None:
            if (item.keyword != 'var' and item.keyword != 'using_reg' and item.keyword != 'using_instructions'):
                functions[actual].append(item)

    return functions