from .casm_common import *

from .lib.RomFF import Rom

def casm_compile(prg):
    functions = get_content_function(prg)
    vars = {item.value[1]: item.value[0] for item in prg if item.keyword == 'var'}
    using = {it for item in prg if item.keyword == "using_reg" for it in item.value}
    func_args = {item.keyword[1:]: item.value for item in prg if item.keyword.startswith('.')}
    func_args.update(KEYWORDS)

    compiled_functions = {}

    for item in functions:
        compiled_functions[item] = []
        for it in functions[item]:
            if it.keyword in BINARIES:
                compiled_functions[item] += list(int(i) if i not in func_args[it.keyword] else int(it.value[func_args[it.keyword].index(i)]) for i in BINARIES[it.keyword])
                
    rom: Rom = Rom(0)
    function_allocation = {}
    rom.prg_memory = {i: 0x00 for i in range((200))}
    rom.ram_memory = {i: 0x00 for i in range((250))}
    ptr_prg = 0x00
    ptr_ram = 0x00
    skip = 0

    for item in compiled_functions:
        ptr_prg += 4
        function_allocation[item] = ptr_prg
        for op in compiled_functions[item]:
            rom.prg_memory[ptr_prg] = op
            ptr_prg += 1
        for i, op in enumerate(BINARIES['_goback']):
            if (skip):
                skip -= 1
                continue
            if isinstance(op, str) and op in BINARIES:
                for it in BINARIES[op]:
                    if (it == '__addr'):
                        it = BINARIES['_goback'][i + skip + 1]
                        skip += 1
                    rom.prg_memory[ptr_prg] = it
                    ptr_prg += 1
            else:
                rom.prg_memory[ptr_prg] = op
                ptr_prg += 1

    rom.prg_memory[ptr_prg] = op

    if ('main' in function_allocation):
        rom.ram_memory[0xCF] = function_allocation['main']
        ptr_prg += 4
        rom.registries['ptr_prg'] = ptr_prg
        for i, op in enumerate(BINARIES['_main']):
            if (skip):
                skip -= 1
                continue
            if op == '__addr':
                op = ptr_prg + 10
            if op == '__new_addr':
                op = function_allocation['main']
            if isinstance(op, str) and op in BINARIES:
                for it in BINARIES[op]:
                    if (it == '__addr'):
                        it = BINARIES['_main'][i + skip + 1]
                        skip += 1
                    rom.prg_memory[ptr_prg] = it
                    ptr_prg += 1
            else:
                rom.prg_memory[ptr_prg] = op
                ptr_prg += 1

    return (rom)