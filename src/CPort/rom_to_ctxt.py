def main():
    __l = 0

    with open("obj", "rb") as f:
        __l = len(f.read())

    print('#include "rom_to_exe.h"')
    print("char FILE_COMPILED[] = {\n  ", end='')

    with open("obj", "rb") as f:
        for i in range(__l):
            print(hex(int.from_bytes(f.read(1), "big")), end='')

            if i != __l - 1:
                print(', ', end='')

            if (i % 11 == 10):
                print('\n  ', end='')

    print("\n};")
    print("int SIZE[] = {" + str(__l) + "};")
    return (0)

if __name__ == "__main__":
    exit(main())