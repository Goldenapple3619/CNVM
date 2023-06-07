from mother_board.handling_hw import *
from random import randint
from lib.RomFF import *
from lib.CNEngine import *
from src.config_file import *

class ShowRegister(Container):
    def __init__(self, x, y, color, cpu):
        super().__init__(x, y, None)
        self.cpu = cpu
        self.text = TextBox(5, 5, text="loading...", color=color, font=font.SysFont("Consolas", 12), scrollable=True)
        self.add_hud(self.text)

    def event(self, event):
        return super().event(event)

    def update(self, parent):
        data = '\n'.join([item + ':  ' + hex(self.cpu.registries[item]).split('x')[-1].upper().zfill(2) for item in self.cpu.registries])
        self.text.set_text('\n' + data)
        super().update(parent)

    def draw(self, screen: object):
        super().draw(screen)

class ShowProgram(Container):
    def __init__(self, x, y, color):
        super().__init__(x, y, None)
        self.text = TextBox(5, 5, text="loading...", color=color, font=font.SysFont("Consolas", 12), scrollable=True)
        self.add_hud(self.text)

    def event(self, event):
        return super().event(event)

    def update(self, parent):
        with open("./temp/debug", 'r') as f:
            data = f.read()
        self.text.set_text('\n' + data)
        super().update(parent)

    def draw(self, screen: object):
        super().draw(screen)

class ShowRam(Container):
    def __init__(self, x, y, ram, color):
        super().__init__(x, y, None)
        self.ram = ram
        self.text = TextBox(5, 5, text="loading...", color=color, font=font.SysFont("Consolas", 12), scrollable=True)
        self.add_hud(self.text)

    def event(self, event):
        return super().event(event)

    def update(self, parent):
        ram = self.ram
        data = ''.join([(f'\n${hex(item).split("x")[-1].upper().zfill(4)}:  ' if item % 16 == 0 else '  ') + hex(ram.read(item)).split('x')[-1].upper().zfill(2) for item in range(ram.size)])
        self.text.set_text(data)
        super().update(parent)

    def draw(self, screen: object):
        super().draw(screen)

def load_binary(cpu, ram, file, pos=100) -> None:
    rom = Rom()
    rom.load_from_file(file)
    for item in rom.ram_memory:
        ram.write(item, rom.ram_memory[item])
    for item in rom.prg_memory:
        ram.write(item, rom.prg_memory[item])
    for item in rom.registries:
        cpu.registries[item] = rom.registries[item]

def hex_to_rgb(color: str) -> tuple:
    colors = [color[i:i+2] for i in range(0, len(color), 2)]
    rgb = [0x00, 0x00, 0x00, 0xFF]

    for i, item in enumerate(colors):
        rgb[i] = int(item, 16)
    return (rgb)

def main(argc, argv) -> int:
    if (argc == 1):
        return (1)

    with open("./temp/debug", 'w+'):
        pass

    conf = load_config_from_file("./themes/emulator_debug_default.conf" if argc == 2 else argv[2])
    if ("fullscreen" not in conf or conf["fullscreen"] not in ("1", "0")):
        conf["fullscreen"] = "1"
    if ("text-color" not in conf or len(conf["text-color"]) != 8):
        conf["text-color"] = "ffffffff"
    if ("title-color" not in conf or len(conf["title-color"]) != 8):
        conf["title-color"] = "ffffffff"
    if ("background-color" not in conf) or len(conf["background-color"]) != 8:
        conf["background-color"] = "000080ff"
    if ("size" not in conf or len(conf["size"].split('x')) != 2 or not all(map(lambda x: x.isnumeric(), conf["size"].split("x")))):
        conf["size"] = "1330x700"

    get_connected_hardware()
    load_binary([item["component"] for item in POWERED_COMPONENT if item["comp"] == 0x02][0], [item["component"] for item in POWERED_COMPONENT if item["comp"] == 0x01][0], argv[1])
    #[item["component"] for item in POWERED_COMPONENT if item["comp"] == 0x04][0].start_up()

    init_engine()

    G = create_game("PyDebug", fullscreen=int(conf["fullscreen"]), size=tuple(map(int, conf["size"].split('x'))), color=hex_to_rgb(conf["background-color"]))
    T = Text(10, 10, "Ram:", hex_to_rgb(conf["title-color"]), font.Font("./assets/font/SourceCodePro-Regular.otf", 16), False)
    T1 = Text(550, 10, "Processor:", hex_to_rgb(conf["title-color"]), font.Font("./assets/font/SourceCodePro-Regular.otf", 16), False)
    T2 = Text(700, 10, "Registries:", hex_to_rgb(conf["title-color"]), font.Font("./assets/font/SourceCodePro-Regular.otf", 16), False)

    add_hud_to_game(G, T)
    add_hud_to_game(G, T1)
    add_hud_to_game(G, T2)
    add_hud_to_game(G, ShowRam(10, 30, [item["component"] for item in POWERED_COMPONENT if item["comp"] == 0x01][0], hex_to_rgb(conf["text-color"])))
    add_hud_to_game(G, ShowProgram(550, 30, hex_to_rgb(conf["text-color"])))
    add_hud_to_game(G, ShowRegister(700, 30, hex_to_rgb(conf["text-color"]), [item["component"] for item in POWERED_COMPONENT if item["comp"] == 0x02][0]))

    temp = [item["component"] for item in POWERED_COMPONENT if item["comp"] == 0x02][0]
    add_script_to_game(G, lambda *args: temp.clock() if get_pressed()[K_c] else None)

    C = Camera(0,0,12)
    add_camera_to_game(G, C)

    try:
        G.run()
    except KeyboardInterrupt:
        pass

    power_off_hw()
    return (0)

if __name__ == "__main__":
    exit(main(len(argv), argv))