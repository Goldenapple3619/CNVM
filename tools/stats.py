from os import walk, stat
from sys import argv

VALUES = [("Go", 1000000000), ("Mo", 1000000), ("Ko", 1000)]

COLORS = {
        "end"      : '\33[0m',
        "bold"     : '\33[1m',
        "italic"   : '\33[3m',
        "url"      : '\33[4m',
        "blink"    : '\33[5m',
        "blink2"   : '\33[6m',
        "selected" : '\33[7m',

        "black"  : '\33[30m',
        "red"    : '\33[31m',
        "green"  : '\33[32m',
        "yellow" : '\33[33m',
        "blue"   : '\33[34m',
        "violet" : '\33[35m',
        "beige"  : '\33[36m',
        "white"  : '\33[37m',

        "blackbg"  : '\33[40m',
        "redbg"    : '\33[41m',
        "greenbg"  : '\33[42m',
        "yellowbg" : '\33[43m',
        "bluebg"   : '\33[44m',
        "violetbg" : '\33[45m',
        "beigebg"  : '\33[46m',
        "whitebg"  : '\33[47m',

        "grey"    : '\33[90m',
        "red2"    : '\33[91m',
        "green2"  : '\33[92m',
        "yellow2" : '\33[93m',
        "blue2"   : '\33[94m',
        "violet2" : '\33[95m',
        "beige2"  : '\33[96m',
        "white2"  : '\33[97m',

        "greybg"    : '\33[100m',
        "redbg2"    : '\33[101m',
        "greenbg2"  : '\33[102m',
        "yellowbg2" : '\33[103m',
        "bluebg2"   : '\33[104m',
        "violetbg2" : '\33[105m',
        "beigebg2"  : '\33[106m',
        "whitebg2"  : '\33[107m'
}

EXTS = {
    "py"        :   "Python"           ,
    "html"      :   "HTML"             ,
    "js"        :   "JavaScript"       ,
    "ts"        :   "TypeScript"       ,
    "cnd"       :   "CNDataBase"       ,
    "cql"       :   "CNQueryLang"      ,
    "sql"       :   "SQL"              ,
    "css"       :   "StyleSheet"       ,
    "c"         :   "CLang"            ,
    "h"         :   "CHeader"          ,
    "cpp"       :   "C++"              ,
    "hpp"       :   "C++ Header"       ,
    "cs"        :   "CSharp"           ,
    "asm"       :   "Assembly"         ,
    "txt"       :   "PlainText"        ,
    "makefile"  :   "MakeFile"         ,
    "gld"       :   "GameStorageLoad"  ,
    "rb"        :   "Ruby"             ,
    "rs"        :   "Rust"             ,
    "php"       :   "PHP"              ,
    "lua"       :   "LUA"              ,
    "o"         :   "ObjectFile"       ,
    "so"        :   "SharedObjectFile" ,
    "dll"       :   "DLLFile"          ,
    "jar"       :   "JavaExecutable"   ,
    "pyc"       :   "PythonCache"      ,
    "exe"       :   "WindowsExecutable",
    "bat"       :   "DosCommand"       ,
    "sh"        :   "UnixCommand"      ,
    "ps"        :   "powershell"       ,
    "java"      :   "Java"             ,
    "pde"       :   "Processing"       ,
    "go"        :   "GoLang"           ,
    "pl"        :   "Pearl"            ,
    "toml"      :   "CargoFile"        ,
    "rsm"       :   "RsAsm"            ,
    "out"       :   "CompiledFile"     ,
    "rom"       :   "RomFile"          ,
    "pl"        :   "Pascal"           ,
    "json"      :   "JSON"             ,
    "xml"       :   "XML"              ,
    "vbs"       :   "VisualBasicScript",
    "vba"       :   "VisualBasic"      ,
    "Makefile"  :   "MakeFile"         ,
    "Dockerfile":   "DockerFile"       ,
    "yml"       :   "YAML"             ,
    "conf"       :  "Config"           ,
}

def _make_gen(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024*1024)
    return b

def get_lines(files: list):
    lines = 0
    buf_size = 1024 * 1024

    for file in files:
        if get_ext(ext_from_name(file)) in ("other", "PythonCache"):
            continue
        f = open(file, 'rb')
        read_f = f.raw.read
        buf = read_f(buf_size)

        while buf:
            lines += buf.count(b'\n')
            buf = read_f(buf_size)

        f.close()

    return lines

def size_to_val(size):
    index = 0
    ref = "o"
    while index < len(VALUES):
        s_t = size/VALUES[index][1]
        if s_t > 1:
            size = s_t
            ref = VALUES[index][0]

        else:
            index += 1

    return str(round(size, 2)) + ref

def get_ext(ext: str):
    return EXTS[ext] if ext in EXTS else "other"

def ext_from_name(file_name: str):
    return file_name.split('.')[-1].split('/')[-1]

def get_all(path: str) -> list:
    return list(walk(path))

def get_all_files(pool: list):
    return [file for item in pool for file in item[2]]

def get_all_folder(pool: list):
    return [folder for item in pool for folder in item[1]]

def detail_number(file_pool: list):
    dats = {}
    for file in file_pool:
        ext = get_ext(ext_from_name(file))
        if ext not in dats:
            dats[ext] = 0

        dats[ext] += 1
    return dats

def detail_percents(details: list, number: int):
    percents = {}
    for item in details:
        if item == "other":
            continue
        percents[item] = round((details[item]*100) / number, 2)
    return percents


def get_number_file_lang(details: list):
    nb = 0
    for item in details:
        if item == "other":
            continue
        nb += details[item]
    return nb

def get_size_all(pool: list):
    f = 0
    for file in pool:
        f += stat(file).st_size

    return size_to_val(f)

def get_file_path(pool: list):
    return [item[0] + '/' + file for item in pool for file in item[2]]


def main(args: tuple) -> int:
    elements             = {}

    project_name         = "Project Emulator"
    pool                 = get_all(f"./")

    folders              = get_all_folder(pool)
    files                = get_all_files(pool )

    detailed_file_type   = detail_number(files)
    number_file_lang     = get_number_file_lang(detailed_file_type)
    percents             = detail_percents(detailed_file_type, number_file_lang)

    project_size         = get_size_all(get_file_path(pool))
    number_of_lines      = get_lines(get_file_path(pool))

    string_detailed      = '\n' + '\n'.join(f"  {COLORS['blue']}{key}{COLORS['end']}: " + ' '*(17-len(key)) + f"{value} " + " "*(8-len(str(value))) + f"{COLORS['red2']}{percents[key]}{COLORS['end']} " + " "*(6-len(str(percents[key]))) + "%" if key != "other" else f"  {COLORS['blue']}{key}{COLORS['end']}: " + ' '*(17-len(key)) + f"{value} " for key, value in sorted(detailed_file_type.items(), key=lambda item: item[1], reverse=True))

    elements["Project name"]     = project_name
    elements["Number of folders"] = len(folders)
    elements["Number of files"]  = len( files )
    elements["Size"]             = project_size
    elements["Number of lines"]  = number_of_lines
    elements["Details"]          = string_detailed

    print("\n".join(f"{COLORS['beige']}{key}{COLORS['end']}: {value}" for key, value in elements.items()))


    return 0


if __name__ == "__main__":
    exit(main(argv[1:]))