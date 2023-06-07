def null(*args, **kwargs) -> int:
    return (0x00)

def ADX(self) -> int:
    self.registries["x"] = self.registries["x"] + self.registries["temp"]

def ADY(self) -> int:
    self.registries["y"] = self.registries["y"] + self.registries["temp"]

def SUX(self) -> int:
    self.registries["x"] = self.registries["x"] - self.registries["temp"]

def SUY(self) -> int:
    self.registries["y"] = self.registries["y"] - self.registries["temp"]

def MUX(self) -> int:
    self.registries["x"] = self.registries["x"] * self.registries["temp"]

def MUY(self) -> int:
    self.registries["y"] = self.registries["y"] * self.registries["temp"]

def DIX(self) -> int:
    self.registries["x"] = self.registries["x"] // self.registries["temp"]

def DIY(self) -> int:
    self.registries["y"] = self.registries["y"] // self.registries["temp"]

def MOX(self):
    self.registries["x"] = self.registries["x"] % self.registries["temp"]

def MOY(self):
    self.registries["y"] = self.registries["y"] % self.registries["temp"]

def ICX(self) -> int:
    self.registries["x"] += 1

def ICY(self) -> int:
    self.registries["y"] += 1

def TVX(self):
    self.registries["temp"] = self.registries["x"]

def TVY(self):
    self.registries["temp"] = self.registries["y"]

def PPX(self) -> int:
    self.registries["ptr_prg"] = self.registries["x"]
    self.registries["ptr_prg"] -= 1

def PPY(self) -> int:
    self.registries["ptr_prg"] = self.registries["y"]
    self.registries["ptr_prg"] -= 1

def MPX(self) -> int:
    self.registries["ptr_mem"] = self.registries["x"]

def MPY(self) -> int:
    self.registries["ptr_mem"] = self.registries["y"]

def XPP(self) -> int:
    self.registries["x"] = self.registries["ptr_prg"]

def YPP(self) -> int:
    self.registries["y"] = self.registries["ptr_prg"]

def XMP(self) -> int:
    self.registries["x"] = self.registries["ptr_mem"]

def YMP(self) -> int:
    self.registries["y"] = self.registries["ptr_mem"]

def DMX(self):
    self.registries["mem_device"] = self.registries["x"]

def DMY(self):
    self.registries["mem_device"] = self.registries["y"]

def DPX(self):
    self.registries["prg_device"] = self.registries["x"]

def DPY(self):
    self.registries["prg_device"] = self.registries["y"]

def XVY(self):
    self.registries["x"] = self.registries["y"]

def YVX(self):
    self.registries["y"] = self.registries["x"]

def XVT(self):
    self.registries["x"] = self.registries["temp"]

def YVT(self):
    self.registries["y"] = self.registries["temp"]

def XVF(self):
    self.registries["x"] = self.registries["fetched"]

def YVF(self):
    self.registries["y"] = self.registries["fetched"]

def TVF(self):
    self.registries["temp"] = self.registries["fetched"]

def MVX(self) -> int:
    mem = [item for item in self.connected if item["comp"] == self.registries["mem_device"] and item['status'] == 1]
    if (len(mem) > 0):
        mem = mem[0]["component"]
        mem.write(self.registries["ptr_mem"], self.registries["x"])

def MVY(self) -> int:
    mem = [item for item in self.connected if item["comp"] == self.registries["mem_device"] and item['status'] == 1]
    if (len(mem) > 0):
        mem = mem[0]["component"]
        mem.write(self.registries["ptr_mem"], self.registries["y"])

def RDM(self) -> int:
    mem = [item for item in self.connected if item["comp"] == self.registries["mem_device"] and item['status'] == 1]
    if (len(mem) > 0):
        mem = mem[0]["component"]
        self.registries["fetched"] = mem.read(self.registries["ptr_mem"])

def TMX(self):
    dev = [item for item in self.connected if item["comp"] == self.registries["temp"] and item['status'] == 1]
    if (len(dev) > 0):
        dev = dev[0]["component"]
        self.registries["fetched"] = dev.send_message(self.registries["x"])

def TMY(self):
    dev = [item for item in self.connected if item["comp"] == self.registries["temp"] and item['status'] == 1]
    if (len(dev) > 0):
        dev = dev[0]["component"]
        self.registries["fetched"] = dev.send_message(self.registries["y"])

def ANX(self):
    self.registries["x"] = self.registries["x"] & self.registries["temp"]

def ANY(self):
    self.registries["y"] = self.registries["y"] & self.registries["temp"]

def ORX(self):
    self.registries["x"] = self.registries["x"] | self.registries["temp"]

def ORY(self):
    self.registries["y"] = self.registries["y"] | self.registries["temp"]

def XOX(self):
    self.registries["x"] = self.registries["x"] ^ self.registries["temp"]

def XOY(self):
    self.registries["y"] = self.registries["y"] ^ self.registries["temp"]

def LSX(self):
    self.registries["x"] = self.registries["x"] << self.registries["temp"]

def LSY(self):
    self.registries["y"] = self.registries["y"] << self.registries["temp"]

def RSX(self):
    self.registries["x"] = self.registries["x"] >> self.registries["temp"]

def RSY(self):
    self.registries["y"] = self.registries["y"] >> self.registries["temp"]

def EQX(self):
    self.registries["x"] = self.registries["x"] == self.registries["temp"]

def EQY(self):
    self.registries["y"] = self.registries["y"] == self.registries["temp"]

def NQX(self):
    self.registries["x"] = self.registries["x"] != self.registries["temp"]

def NQY(self):
    self.registries["y"] = self.registries["y"] != self.registries["temp"]

def SPX(self):
    self.registries["x"] = self.registries["x"] > self.registries["temp"]

def SPY(self):
    self.registries["y"] = self.registries["y"] > self.registries["temp"]

def INX(self):
    self.registries["x"] = self.registries["x"] < self.registries["temp"]

def INY(self):
    self.registries["y"] = self.registries["y"] < self.registries["temp"]

def IEX(self):
    self.registries["x"] = self.registries["x"] <= self.registries["temp"]

def IEY(self):
    self.registries["y"] = self.registries["y"] <= self.registries["temp"]

def SEX(self):
    self.registries["x"] = self.registries["x"] >= self.registries["temp"]

def SEY(self):
    self.registries["y"] = self.registries["y"] >= self.registries["temp"]

def NOX(self):
    self.registries["x"] = ~self.registries["x"]

def NOY(self):
    self.registries["y"] = ~self.registries["y"]

def CNE(self):
    if (self.registries['temp']):
        return
    else:
        self.registries["ptr_prg"] += 1

def HALT(self):
    self.registries["ptr_prg"] -= 1

def SWX(self):
    self.registries["x"], self.registries["temp"] = self.registries["temp"], self.registries["x"]

def SWY(self):
    self.registries["y"], self.registries["temp"] = self.registries["temp"], self.registries["y"]

def REX(self):
    self.registries["x"] = 0x00

def REY(self):
    self.registries["y"] = 0x00

def STX(self):
    prg = [item for item in self.connected if item["comp"] == self.registries["prg_device"] and item['status'] == 1]
    if (len(prg) > 0):
        prg = prg[0]["component"]
        self.registries["x"] = prg.read(self.registries["ptr_prg"] + 1)
        self.registries["ptr_prg"] += 1

def STY(self):
    prg = [item for item in self.connected if item["comp"] == self.registries["prg_device"]]
    if (len(prg) > 0):
        prg = prg[0]["component"]
        self.registries["y"] = prg.read(self.registries["ptr_prg"] + 1)
        self.registries["ptr_prg"] += 1

def LOG(self):
    print(chr(self.registries["temp"]), end='', flush=True)

def idn(*args, **kwargs):
    return 0x02

def end(*args, **kwargs):
    return 0x00