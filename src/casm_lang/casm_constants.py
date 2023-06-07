KEYWORDS = {
    "using_reg": ('...',),
    "using_instructions": ('...',),
    "halt": (),
    "var": ('__addr','__name'),
    "log": ('__value',),
    "_set": ('__addr',),
    "_get": ('__addr',),
    "sub": ('__dest', '__src'),
    "add": ('__dest', '__src'),
    "if": ('__value',)
}

BINARIES = {
    "_get": (
        0x47, # set next prg_ptr as x
        '__addr', # value arg
        0x14, # set memory ptr to x
        0x43, # reset x
        0x22, # read memory ptr mem
        0x1E  # move fetched to x
    ),
    "_set": (
        0x10, # move x to temp
        0x47, # set next prg_ptr as x
        '__addr', # addr arg
        0x14, # set memory ptr to x
        0x41, # swap temp and x
        0x20  # write x in mem at memory ptr
    ),
    "_goback": (
        '_get',
        0xCF,
        0x12
    ),
    '_main': (
        0x47,
        '__addr',
        '_set',
        0xCF,
        0x47,
        '__new_addr',
        0x12,
        0x3E # halt
    ),
    "sub": (
        '_get', # read value next
        '__src', # src arg
        0x10, # move x to temp
        '_get', # get value next
        '__dest', # dest arg
        0x05,  # sub x with temp
        '_set', # write x to next
        '__dest' # dest arg
    ),
    "add": (
        '_get', # read value next
        '__src', # src arg 
        0x10, # move x to temp
        '_get', # read value next
        '__dest', # dest arg 
        0x03,  # sub x with temp
        '_set', # write x to next
        '__dest' # dest arg 
    ),
    "if": (
    
    ),
    "log": (
        0x47, # set next prg_ptr as x
        '__value', # value arg
        0x10, # move x to temp
        0xFF  # log temp
    ),
    "halt": (
        0x3E, # halt
    )
}