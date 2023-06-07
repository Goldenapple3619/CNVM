from os import listdir
from os.path import dirname, abspath
from importlib import import_module

PORTS = (
    "hdmi0",
    "usb0",
    "usb1",
    "usb2"
)

def get_external_port():
    return ["external_ports/" + item + '/' + listdir(dirname(abspath(__file__)) + '/' + item)[0] for item in PORTS if len(listdir(dirname(abspath(__file__)) + '/' + item)) != 0]

def loader(hw):
    for item in get_external_port():
        item = item.replace('\\', '/')
        loading = import_module(item.replace('/','.'))

        if not hasattr(loading, "loader"):
            hw.append({"component": None, "status": False, "name": item, "message": "invalid component or missing component", "comp": 0x00})
            continue
        loaded = loading.loader(hw)

        if loaded is not None and loaded.send_message(0x00) == 0x00:
            hw.append({"component": loaded, "status": True, "name": item, "message": "OK", "comp": loaded.send_message(0x06)})
            continue;

        if loaded is None:
            hw.append({"component": None, "status": False, "name": item, "message": "component cannot be powered", "comp": 0x00})
            continue;

        hw.append({"component": None, "status": False, "name": item, "message": "component do not respond propelry to instruction 0x00", "comp": 0x00})