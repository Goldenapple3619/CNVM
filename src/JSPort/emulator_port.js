const { get_device } = require("./common.js");

OP = require("./instructions.js");

module.exports = {
    CPU: class {
        constructor() {
            this.id = 0x02;
            this.registries = {
                "x": 0x00,
                "y": 0x00,
                "temp": 0x00,
                "fetched": 0x00,

                "ptr_prg": 0x00,
                "ptr_mem": 0x00,
                "mem_device": 0x01,
                "prg_device": 0x01
            };
            this.instructions = {
                0x00: OP.NULL,
                0x01: OP.ICX,
                0x02: OP.ICY,  
                0x03: OP.ADX,
                0x04: OP.ADY,
                0x05: OP.SUX,
                0x06: OP.IDN,
                0x07: OP.SUY,
                0x08: OP.MUX,
                0x09: OP.MUY,
                0x0A: OP.DIX,
                0x0B: OP.DIY,
                0x0C: OP.MOX,
                0x0D: OP.MOY,
                0x0E: OP.TVF,
                0x0F: OP.END,
                0x10: OP.TVX,
                0x11: OP.TVY,
                0x12: OP.PPX,
                0x13: OP.PPY,
                0x14: OP.MPX,
                0x15: OP.MPY,
                0x16: OP.DMX,
                0x17: OP.DMY,
                0x18: OP.DPX,
                0x19: OP.DPY,
                0x1A: OP.XVY,
                0x1B: OP.YVX,
                0x1C: OP.XVT,
                0x1D: OP.YVT,
                0x1E: OP.XVF,
                0x1F: OP.YVF,
                0x20: OP.MVX,
                0x21: OP.MVY,
                0x22: OP.RDM,
                0x23: OP.TMX,
                0x24: OP.TMY,
                0x25: OP.ANX,
                0x26: OP.ANY,
                0x27: OP.ORX,
                0x28: OP.ORY,
                0x29: OP.XOX,
                0x2A: OP.XOY,
                0x2B: OP.LSX,
                0x2C: OP.LSY,
                0x2D: OP.RSX,
                0x2E: OP.RSY,
                0x2F: OP.EQX,
                0x30: OP.EQY,
                0x31: OP.NQX,
                0x32: OP.NQY,
                0x33: OP.SPX,
                0x34: OP.SPY,
                0x35: OP.INX,
                0x36: OP.INY,
                0x37: OP.IEX,
                0x38: OP.IEY,
                0x39: OP.SEX,
                0x3A: OP.SEY,
                0x3B: OP.NOX,
                0x3C: OP.NOY,
                0x3D: OP.CNE,
                0x3E: OP.HALT,
                0x3F: OP.XPP,
                0x40: OP.YPP,
                0x41: OP.SWX,
                0x42: OP.SWY,
                0x43: OP.REX,
                0x44: OP.REY,
                0x45: OP.XMP,
                0x46: OP.YMP,
                0x47: OP.STX,
                0x48: OP.STY,
                0xFF: OP.LOG          
            };
        }
        send_message(motherboard, instruction) {
            if (!(instruction in this.instructions))
                instruction = 0x00;
            return (this.instructions[instruction](motherboard, this));
        }
        clock(motherboard) {
            let dev = get_device(motherboard, 0x01);
            let instruction = 0x00;

            if (dev != undefined)
                instruction = dev.read(this.registries["ptr_prg"]);
            this.send_message(motherboard, instruction);
            this.registries["ptr_prg"] += 1;
        }
    },
    RAM: class {
        constructor(size) {
            this.id = 0x01;
            this.memory = new Array(size);
            for (let i = 0; i < size; ++i) {
                this.memory[i] = 0x00;
            }
        }
        send_message(motherboard, instruction) {
            return (0x00);
        }
        read(addr) {
            if (addr < 0x00 || addr > this.memory.length)
                return (0x00);
            return (this.memory[addr]);
        }
        write(addr, value) {
            if (addr < 0x00 || addr > this.memory.length)
                return (0x01);
            this.memory[addr] = value;
            return (0x00);
        }
    },
    MotherBoard: class {
        constructor() {
            this.id = 0x00;
            this.connected_dev = [
                new module.exports.RAM(1024),
                new module.exports.CPU()
            ];
        }
    }
}
