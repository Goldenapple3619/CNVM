from mother_board.handling_hw import *
from lib.RomFF import *

from sys import argv
from random import randint

def run_program(path):
    get_connected_hardware(["external_ports"])
    rom = Rom(0)
    rom.load_from_file(path)
    cpu = [item["component"] for item in POWERED_COMPONENT if item["comp"] == 0x02 and item['status'] == 1][0]
    ram = [item["component"] for item in POWERED_COMPONENT if item["comp"] == 0x01 and item['status'] == 1][0]
    for item in rom.ram_memory:
        ram.write(item, rom.ram_memory[item])
    for item in rom.prg_memory:
        ram.write(item, rom.prg_memory[item])
    for item in rom.registries:
        cpu.registries[item] = rom.registries[item]
    while (ram.read(cpu.registries["ptr_prg"]) != 0x3E):
        cpu.clock()
    
    power_off_hw()
    return (0)

def main() -> int:
    get_connected_hardware()
    [item["component"] for item in POWERED_COMPONENT if item["comp"] == 0x04][0].start_up()
    power_off_hw()
    return (0)

if __name__ == "__main__":
    exit(run_program(argv[1]))