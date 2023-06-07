const { get_device } = require("./common.js");

module.exports = {
    NULL: function (motherboard, self) {
        return (0x00);
    },

    ICX: function (motherboard, self) {
        self.registries["x"] += 1;
        return (0x00);
    },

    ICY: function (motherboard, self) {
        self.registries["y"] += 1;
        return (0x00);
    },

    ADX: function (motherboard, self) {
        self.registries["x"] += self.registries["temp"];
        return (0x00);
    },

    ADY: function (motherboard, self) {
        self.registries["y"] += self.registries["temp"];
        return (0x00);
    },

    SUX: function (motherboard, self) {
        self.registries["x"] -= self.registries["temp"];
        return (0x00);
    },

    IDN: function (motherboard, self) {
        return (self.id);
    },

    SUY: function (motherboard, self) {
        self.registries["y"] -= self.registries["temp"];
        return (0x00);
    },

    MUX: function (motherboard, self) {
        self.registries["x"] *= self.registries["temp"];
        return (0x00);
    },

    MUY: function (motherboard, self) {
        self.registries["y"] *= self.registries["temp"];
        return (0x00);
    },

    DIX: function (motherboard, self) {
        self.registries["x"] = Math.round(self.registries["x"] / self.registries["temp"]);
        return (0x00);
    },

    DIY: function (motherboard, self) {
        self.registries["y"] = Math.round(self.registries["y"] / self.registries["temp"]);
        return (0x00);
    },

    MOX: function (motherboard, self) {
        self.registries["x"] %= self.registries["temp"];
        return (0x00);
    },

    MOY: function (motherboard, self) {
        self.registries["y"] %= self.registries["temp"];
        return (0x00);
    },

    TVF: function (motherboard, self) {
        self.registries["temp"] = self.registries["fetched"];
        return (0x00);
    },

    END: function (motherboard, self) {
        return (0x00);
    },

    TVX: function (motherboard, self) {
        self.registries["temp"] = self.registries["x"];
        return (0x00);
    },

    TVY: function (motherboard, self) {
        self.registries["temp"] = self.registries["y"];
        return (0x00);
    },

    PPX: function (motherboard, self) {
        self.registries["ptr_prg"] = self.registries["x"];
        self.registries["ptr_prg"] -= 1;
        return (0x00);
    },

    PPY: function (motherboard, self) {
        self.registries["ptr_prg"] = self.registries["y"];
        self.registries["ptr_prg"] -= 1;
        return (0x00);
    },

    MPX: function (motherboard, self) {
        self.registries["ptr_mem"] = self.registries["x"];
        return (0x00);
    },

    MPY: function (motherboard, self) {
        self.registries["ptr_mem"] = self.registries["y"];
        return (0x00);
    },

    DMX: function (motherboard, self) {
        self.registries["mem_device"] = self.registries["x"];
        return (0x00);
    },

    DMY: function (motherboard, self) {
        self.registries["mem_device"] = self.registries["y"];
        return (0x00);
    },

    DPX: function (motherboard, self) {
        self.registries["mem_device"] = self.registries["x"];
        return (0x00);
    },

    DPY: function (motherboard, self) {
        self.registries["mem_device"] = self.registries["y"];
        return (0x00);
    },

    XVY: function (motherboard, self) {
        self.registries["x"] = self.registries["y"];
        return (0x00);
    },

    YVX: function (motherboard, self) {
        self.registries["y"] = self.registries["x"];
        return (0x00);
    },

    XVT: function (motherboard, self) {
        self.registries["x"] = self.registries["temp"];
        return (0x00);
    },

    YVT: function (motherboard, self) {
        self.registries["y"] = self.registries["temp"];
        return (0x00);
    },

    XVF: function (motherboard, self) {
        self.registries["x"] = self.registries["fetched"];
        return (0x00);
    },

    YVF: function (motherboard, self) {
        self.registries["y"] = self.registries["fetched"];
        return (0x00);
    },

    MVX: function (motherboard, self) {
        var dev = get_device(motherboard, self.registries["mem_device"]);

        if (dev == undefined)
            return (0x01);
        dev.write(self.registries["ptr_mem"], self.registries["x"]);
        return (0x00);
    },

    MVY: function (motherboard, self) {
        var dev = get_device(motherboard, self.registries["mem_device"]);

        if (dev == undefined)
            return (0x01);
        dev.write(self.registries["ptr_mem"], self.registries["y"]);
        return (0x00);
    },

    RDM: function (motherboard, self) {
        var dev = get_device(motherboard, self.registries["mem_device"]);

        if (dev == undefined)
            return (0x01);
            self.registries["fetched"] = dev.read(self.registries["ptr_mem"]);
        return (0x00);
    },

    TMX: function (motherboard, self) {
        var dev = get_device(motherboard, self.registries["temp"]);

        if (dev == undefined)
            return (0x01);
        self.registries["fetched"] = dev.send_message(motherboard, self.registries["x"]);
        return (0x00);
    },

    TMY: function (motherboard, self) {
        var dev = get_device(motherboard, self.registries["temp"]);

        if (dev == undefined)
            return (0x01);
        self.registries["fetched"] = dev.send_message(motherboard, self.registries["y"]);
        return (0x00);
    },

    ANX: function (motherboard, self) {
        self.registries["x"] &= self.registries["temp"];
        return (0x00);
    },

    ANY: function (motherboard, self) {
        self.registries["y"] &= self.registries["temp"];
        return (0x00);
    },

    ORX: function (motherboard, self) {
        self.registries["x"] |= self.registries["temp"];
        return (0x00);
    },

    ORY: function (motherboard, self) {
        self.registries["y"] |= self.registries["temp"];
        return (0x00);
    },

    XOX: function (motherboard, self) {
        self.registries["x"] ^= self.registries["temp"];
        return (0x00);
    },

    XOY: function (motherboard, self) {
        self.registries["y"] ^= self.registries["temp"];
        return (0x00);
    },

    LSX: function (motherboard, self) {
        self.registries["x"] <<= self.registries["temp"];
        return (0x00);
    },

    LSY: function (motherboard, self) {
        self.registries["y"] <<= self.registries["temp"];
        return (0x00);
    },

    RSX: function (motherboard, self) {
        self.registries["x"] >>= self.registries["temp"];
        return (0x00);
    },

    RSY: function (motherboard, self) {
        self.registries["y"] >>= self.registries["temp"];
        return (0x00);
    },

    EQX: function (motherboard, self) {
        self.registries["x"] = self.registries["x"] == self.registries["temp"];
        return (0x00);
    },

    EQY: function (motherboard, self) {
        self.registries["y"] = self.registries["y"] == self.registries["temp"];
        return (0x00);
    },

    NQX: function (motherboard, self) {
        self.registries["x"] = self.registries["x"] != self.registries["temp"];
        return (0x00);
    },

    NQY: function (motherboard, self) {
        self.registries["y"] = self.registries["y"] != self.registries["temp"];
        return (0x00);
    },
    
    SPX: function (motherboard, self) {
        self.registries["x"] = self.registries["x"] > self.registries["temp"];
        return (0x00);
    },

    SPY: function (motherboard, self) {
        self.registries["y"] = self.registries["y"] > self.registries["temp"];
        return (0x00);
    },

    INX: function (motherboard, self) {
        self.registries["x"] = self.registries["x"] < self.registries["temp"];
        return (0x00);
    },

    INY: function (motherboard, self) {
        self.registries["y"] = self.registries["y"] < self.registries["temp"];
        return (0x00);
    },

    IEX: function (motherboard, self) {
        self.registries["x"] = self.registries["x"] <= self.registries["temp"];
        return (0x00);
    },

    IEY: function (motherboard, self) {
        self.registries["y"] = self.registries["y"] <= self.registries["temp"];
        return (0x00);
    },

    SEX: function (motherboard, self) {
        self.registries["x"] = self.registries["x"] >= self.registries["temp"];
        return (0x00);
    },

    SEY: function (motherboard, self) {
        self.registries["y"] = self.registries["y"] >= self.registries["temp"];
        return (0x00);
    },

    NOX: function (motherboard, self) {
        self.registries["x"] = ~self.registries["x"];
        return (0x00);
    },

    NOY: function (motherboard, self) {
        self.registries["y"] = ~self.registries["y"];
        return (0x00);
    },

    CNE: function (motherboard, self) {
        if (!self.registries["temp"])
            self.registries["ptr_prg"] += 1;
        return (0x00);
    },

    HALT: function (motherboard, self) {
        self.registries["ptr_prg"] -= 1;
        return (0x00);
    },

    XPP: function (motherboard, self) {
        self.registries["x"] = self.registries["ptr_prg"];
        return (0x00);
    },

    YPP: function (motherboard, self) {
        self.registries["y"] = self.registries["ptr_prg"];
        return (0x00);
    },
    
    SWX: function (motherboard, self) {
        self.registries["x"], self.registries["temp"] = self.registries["temp"], self.registries["x"];
        return (0x00);
    },

    SWY: function (motherboard, self) {
        self.registries["y"], self.registries["temp"] = self.registries["temp"], self.registries["y"];
        return (0x00);
    },

    REX: function (motherboard, self) {
        self.registries["x"] = 0x00;
        return (0x00);
    },

    REY: function (motherboard, self) {
        self.registries["y"] = 0x00;
        return (0x00);
    },

    XMP: function (motherboard, self) {
        self.registries["x"] = self.registries["ptr_mem"];
        return (0x00);
    },

    YMP: function (motherboard, self) {
        self.registries["y"] = self.registries["ptr_mem"];
        return (0x00);
    },

    STX: function (motherboard, self) {
        var dev = get_device(motherboard, self.registries["prg_device"]);

        self.registries["ptr_prg"] += 1;
        if (dev == undefined)
            return (0x01);
            self.registries["x"] = dev.read(self.registries["ptr_prg"]);
        return (0x00);
    },

    STY: function (motherboard, self) {
        var dev = get_device(motherboard, self.registries["prg_device"]);

        self.registries["ptr_prg"] += 1;
        if (dev == undefined)
            return (0x01);
            self.registries["y"] = dev.read(self.registries["ptr_prg"]);
        return (0x00);
    },

    LOG: function (motherboard, self) {
        console.log(self.registries["temp"]);
        return (0x00);
    }
}
