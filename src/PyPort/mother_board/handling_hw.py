from importlib import import_module
from os.path import isdir, abspath, dirname
from sys import path

POWERED_COMPONENT: list = []
HARDWARE_PLACEMENT: tuple = (
    "memory",
    "processor",
    "graphical_card",
    "external_ports",
    "disk",
    "network_cards",
    "bios_chip"
)

def is_connected(hw: str):
    return isdir(dirname(abspath(__file__)) + '/' + hw)

def connect_responding_hardware(hardware):
    path.append(dirname(abspath(__file__)))
    for item in hardware:
        item = item.replace('\\', '/')
        loading = import_module(item.replace('/','.'))

        if not hasattr(loading, "loader"):
            POWERED_COMPONENT.append({"component": None, "status": False, "name": item, "message": "invalid component or missing component", "comp": 0x00})
            continue

        loaded = loading.loader(POWERED_COMPONENT)

        if loaded is not None and loaded.send_message(0x00) == 0x00:
            POWERED_COMPONENT.append({"component": loaded, "status": True, "name": item, "message": "OK", "comp": loaded.send_message(0x06)})
            continue;

        if loaded is None:
            POWERED_COMPONENT.append({"component": None, "status": False, "name": item, "message": "component cannot be powered", "comp": 0x00})
            continue;

        POWERED_COMPONENT.append({"component": None, "status": False, "name": item, "message": "component do not respond propelry to instruction 0x00", "comp": 0x00})

def power_off_hw():
    for item in POWERED_COMPONENT:
        if not hasattr(item["component"], "send_message"):
            continue
        if item["component"].send_message(0x0F) == 0x00:
            item["status"] = False
            item['message'] = "OFF"

def get_connected_hardware(exclude = []):
    connect_responding_hardware([position for position in HARDWARE_PLACEMENT if is_connected(position) and position not in exclude])
