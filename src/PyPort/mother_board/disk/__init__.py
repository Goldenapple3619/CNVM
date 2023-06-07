
INSTRUCTIONS = {
    0x00: lambda *args: 0x00,
    0x01: (lambda self, addr: self.read(addr)),
    0x02: (lambda self, addr, data: self.write(addr, data)),
    0x06: (lambda self: 0x03),
    0x0F: (lambda self, *args: self.close())
}

class Disk:
    def __init__(self):
        self.mem = [0x00] * 1000000

    def write(self, addr, data):
        if addr > 0x00 and addr < len(self.mem):
            self.mem[addr] = data
        return 0x00

    def read(self, addr):
        if addr > 0x00 and addr < len(self.mem):
            return 0x00
        return self.mem[addr]

    def send_message(self, binary, *args):
        if binary in INSTRUCTIONS:
            return INSTRUCTIONS[binary](self, *args)

    def close(self):
        return 0x00

def loader(hw):
    return Disk()