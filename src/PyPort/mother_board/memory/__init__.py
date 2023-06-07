
INSTRUCTIONS = {
    0x0000: lambda *args: 0x0000,
    0x0001: (lambda self, addr: self.read(addr)),
    0x0002: (lambda self, addr, data: self.write(addr, data)),
    0x0006: (lambda self: 0x0001),
    0x000F: (lambda self, *args: self.close())
}

class Memory:
    def __init__(self):
        self.size = (1024 * 8)
        self.mem = [0x00] * (1024 * 8)

    def write(self, addr, data):
        if addr > 0x00 and addr < len(self.mem):
            self.mem[addr] = data

    def read(self, addr):
        if addr < 0x00 or addr >= len(self.mem):
            return 0x00
        return self.mem[addr]

    def send_message(self, binary, *args):
        if binary in INSTRUCTIONS:
            return INSTRUCTIONS[binary](self, *args)

    def close(self):
        self.mem.clear()
        return 0x00

def loader(hw):
    M = Memory()
    return M