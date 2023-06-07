#              ___________________             #
##############/    Informations   \#############
#            |        /-@-\        |           #
#            |        | | |        |           #
###################   Header   #################
#                                              #
#  ##     Mappers     ##  ##     Magic     ##  #
#  #                   #  #                 #  #
#  # 0 - Absolute addr #  # hex - 0xFA 0xBA #  #
#  # 1 - Dynamic  addr #  # int - 250  186  #  #
#  # 2 - Multidev addr #  # str - ú    º    #  #
#  #                   #  #                 #  #
#  ##     Mappers     ##  ##     Magic     ##  #
#                                              #
################################################
#            |        | | |        |           #
##################   Registry   ################
#                                              #
#  ##                                      ##  #
#  #   - mem_device: int                    #  #
#  #   - x:    int         - ptr_mem: addr  #  #
#  #   - y:    int         - ptr_pgr: addr  #  #
#  #   - temp: int         - fetched: int   #  #
#  #   - prg_device: int                    #  #
#  ##                                      ##  #
#                                              #
################################################
#            |        | | |        |           #
###################    Body    #################
#                                              #
#  ##       Ram       ##  ##      Prg      ##  #
#  #                   #  #                 #  #
#  # 0 - addr: val     #  # 0 - addr: val   #  #
#  # 1 - addr: val,reg #  # 1 - addr: val,re#  #
#  # 2 - addr: val,dev #  # 2 - addr: val,de#  #
#  #                   #  #                 #  #
#  ##       Ram       ##  ##      Prg      ##  #
#                                              #
################################################
#            |    [R]__[O]__[M]    |           #
#            | [F]__[I]___[L]__[E] |           #
#############\_____________________/############


class Rom(object):
    def __init__(self, mapper: int = 0) -> None:
        self.magic: tuple = (0xFA, 0xBA)

        self.memory_mapper: int = mapper

        self.registries: dict = {
            "x": 0x00,
            "y": 0x00,
            "temp": 0x00,
            "ptr_mem": 0x00,
            "ptr_prg": 0x00,
            "mem_device": 0x01,
            "prg_device": 0x01,
            "fetched": 0x00
        }

        self.ram_memory: dict = {}
        self.prg_memory: dict = {}

    def __repr__(self) -> str:
        temp: str = '\n'

        return f"""Header:
 magic: {''.join(map(lambda x: hex(x).split('x')[-1], self.magic))}
 mapper: {self.memory_mapper}

Registries: \n  - {f"{temp}  - ".join([item + ': ' + hex(self.registries[item]) for item in self.registries])}

Body:
 prg: {"".join([(f'{temp}  - ' if i % 5 == 0 else '  ') + '$' + hex(item).split('x')[-1] + ': ' + hex(self.prg_memory[item]) for i, item in enumerate(self.prg_memory)])}

 ram: {"".join([(f'{temp}  - ' if i % 5 == 0 else '  ') + '$' + hex(item).split('x')[-1] + ': ' + hex(self.ram_memory[item]) for i, item in enumerate(self.ram_memory)])}
"""

    @staticmethod
    def read_byte_from_fd(fd, size: int):
        data = fd.read(size)
        return int.from_bytes(data, byteorder='big', signed=True)

    @staticmethod
    def write_byte_to_fd(fd, data: str):
        fd.write(data + b'\n')

    @staticmethod
    def get_required_size(number: int):
        return (8 + (number + (number < 0)).bit_length()) // 8

    @staticmethod
    def int_to_bytes(number: int) -> bytes:
        return number.to_bytes(length=(8 + (number + (number < 0)).bit_length()) // 8, byteorder='big', signed=True)

    @staticmethod
    def int_from_bytes(binary_data: bytes):
        return int.from_bytes(binary_data, byteorder='big', signed=True)

    def copy(self):
        cpy: Rom = Rom(self.memory_mapper)

        cpy.magic = self.magic

        cpy.prg_memory = self.prg_memory.copy()
        cpy.ram_memory = self.ram_memory.copy()

        cpy.registries = self.registries.copy()

        return (cpy)

    def load_from_file(self, path: str):
        with open(path, 'rb') as fd:
            self.magic = (self.read_byte_from_fd(fd, 2), self.read_byte_from_fd(fd, 2))
            self.read_byte_from_fd(fd, 1)
            self.memory_mapper = self.read_byte_from_fd(fd, 1)
            self.read_byte_from_fd(fd, 1)
            nb = int(self.read_byte_from_fd(fd, 1))
            self.read_byte_from_fd(fd, 1)
            for i in range(nb):
                c = '\0'
                while (c[-1] != ':'):
                    c += chr(self.read_byte_from_fd(fd, 1))
                self.registries[c[1:-1]] = self.read_byte_from_fd(fd, int(self.read_byte_from_fd(fd, 1)))
            self.read_byte_from_fd(fd, 1)
            nb = int(self.read_byte_from_fd(fd, int(self.read_byte_from_fd(fd, 1))))
            self.read_byte_from_fd(fd, 1)
            for i in range(nb):
                pos = self.read_byte_from_fd(fd, int(self.read_byte_from_fd(fd, 1)))
                value = int(self.read_byte_from_fd(fd, 1))
                self.ram_memory[pos] = self.read_byte_from_fd(fd, value)

            self.read_byte_from_fd(fd, 1)
            nb = int(self.read_byte_from_fd(fd, int(self.read_byte_from_fd(fd, 1))))
            self.read_byte_from_fd(fd, 1)
            for i in range(nb):
                pos = self.read_byte_from_fd(fd, int(self.read_byte_from_fd(fd, 1)))
                value = int(self.read_byte_from_fd(fd, 1))
                self.prg_memory[pos] = self.read_byte_from_fd(fd, value)
            self.read_byte_from_fd(fd, 1)
        self.prg_memory = dict(sorted(self.prg_memory.items()))
        self.ram_memory = dict(sorted(self.ram_memory.items()))

    def save_to_file(self, path: str) -> None:
        with open(path, 'wb') as fd:
            self.write_byte_to_fd(fd, b''.join(map(self.int_to_bytes, self.magic)))
            self.write_byte_to_fd(fd, self.int_to_bytes(self.memory_mapper))
            self.write_byte_to_fd(fd, self.int_to_bytes(len(self.registries)))
            self.write_byte_to_fd(fd, b''.join([bytes(item, "utf-8") + b':' + self.int_to_bytes(self.get_required_size(self.registries[item])) + self.int_to_bytes(self.registries[item]) for item in self.registries]))
            self.write_byte_to_fd(fd, self.int_to_bytes(self.get_required_size(len(self.ram_memory))) + self.int_to_bytes(len(self.ram_memory)))
            self.write_byte_to_fd(fd, b''.join([self.int_to_bytes(self.get_required_size(item)) + self.int_to_bytes(item) + self.int_to_bytes(self.get_required_size(self.ram_memory[item])) + self.int_to_bytes(self.ram_memory[item]) for item in self.ram_memory]))
            self.write_byte_to_fd(fd, self.int_to_bytes(self.get_required_size(len(self.prg_memory))) + self.int_to_bytes(len(self.prg_memory)))
            self.write_byte_to_fd(fd, b''.join([self.int_to_bytes(self.get_required_size(item)) + self.int_to_bytes(item) + self.int_to_bytes(self.get_required_size(self.prg_memory[item])) + self.int_to_bytes(self.prg_memory[item]) for item in self.prg_memory]))

    def __eq__(self, __value: object) -> bool:
        return self.magic == __value.magic and \
                self.registries == __value.registries and \
                self.memory_mapper == __value.memory_mapper and \
                self.ram_memory == __value.ram_memory and \
                self.prg_memory == __value.prg_memory

if __name__ == "__main__":
    #r = Rom()
    #r.save_to_file('./test_rom.rom')
    t = Rom()
    t.load_from_file("./casm.out")
    #print(r)
    print(t)
    #print(r == t)