from os.path import abspath, dirname

INSTRUCTIONS: list = {
    0x00: lambda *args, **kwargs: 0x00,
    0x06: lambda *args, **kwargs: 0x04,
    0x0F: lambda *args, **kwargs: kwargs["self"].end
}

class BIOS:
    def __init__(self, processor, chip_data):
        self.processor = processor
        self.chip_data = chip_data

    def start_up(self):
        chip_data = self.chip_data
        processor = self.processor
        index = 0
        while index < len(chip_data):
            size = chip_data[index]
            processor.send_message(*(chip_data[(index+1):(index+size+1)]))
            index += size + 1

    def send_message(self, binary, *args):
        if binary in INSTRUCTIONS:
            return INSTRUCTIONS[binary](*args, self=self)

    def end(self):
        self.chip_data.clear()

def loader(hw):
    with open(dirname(abspath(__file__)) + '/' + "chip0") as f:
        data = f.read().replace('\n', '')
        data = data[0:int(data.split("storage_size:")[1].split(';')[0])]
    find = [item["component"] for item in hw if item["comp"] == 0x02]
    if (find == []): return None
    return BIOS(find[0], [0x01, 0x0])