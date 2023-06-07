
from processor.operations import INSTRUCTIONS

CORES_COUNTER = 4

class CPUHandler:
    def __init__(self, connected):
        self.connected = connected

        self.registries = {
            "x": 0x00,
            "y": 0x00,
            "temp": 0x00,
            "ptr_mem": 0x00,
            "ptr_prg": 0x00,
            "mem_device": 0x01,
            "prg_device": 0x01,
            "fetched": 0x00
        }

    def load_workers(self):
        for i in range(CORES_COUNTER):
            pass

    def send_message(self, binary, *args):
        ret = 0x00

        with open("./temp/debug", "a") as f:
            f.write('$' + hex(self.registries["ptr_prg"]).split("x")[-1].upper().zfill(4) + ':  ' + INSTRUCTIONS[binary].__name__ + '\n')

        if binary in INSTRUCTIONS:
            ret = INSTRUCTIONS[binary](self=self)

        return ret

    def clock(self):
        ram = [item["component"] for item in self.connected if item["comp"] == self.registries["prg_device"]][0]
        self.send_message(ram.read(self.registries["ptr_prg"]))
        self.registries["ptr_prg"] += 1

def loader(hw):
    C = CPUHandler(hw)

    return (C)