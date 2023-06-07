from .functions import *

INSTRUCTIONS = {
    0x00: null,
    0x01: ICX,
    0x02: ICY,
    0x03: ADX,
    0x04: ADY,
    0x05: SUX,
    0x06: idn,
    0x07: SUY,
    0x08: MUX,
    0x09: MUY,
    0x0A: DIX,
    0x0B: DIY,
    0x0C: MOX,
    0x0D: MOY,
    0x0E: TVF,
    0x0F: end,
    0x10: TVX,
    0x11: TVY,
    0x12: PPX,
    0x13: PPY,
    0x14: MPX,
    0x15: MPY,
    0x16: DMX,
    0x17: DMY,
    0x18: DPX,
    0x19: DPY,
    0x1A: XVY,
    0x1B: YVX,
    0x1C: XVT,
    0x1D: YVT,
    0x1E: XVF,
    0x1F: YVF,
    0x20: MVX,
    0x21: MVY,
    0x22: RDM,
    0x23: TMX,
    0x24: TMY,
    0x25: ANX,
    0x26: ANY,
    0x27: ORX,
    0x28: ORY,
    0X29: XOX,
    0x2A: XOY,
    0x2B: LSX,
    0x2C: LSY,
    0x2D: RSX,
    0x2E: RSY,
    0x2F: EQX,
    0x30: EQY,
    0x31: NQX,
    0x32: NQY,
    0x33: SPX,
    0x34: SPY,
    0x35: INX,
    0x36: INY,
    0x37: IEX,
    0x38: IEY,
    0x39: SEX,
    0x3A: SEY,
    0x3B: NOX,
    0x3C: NOY,
    0x3D: CNE,
    0x3E: HALT,
    0x3F: XPP,
    0x40: YPP,
    0x41: SWX,
    0x42: SWY,
    0x43: REX,
    0x44: REY,
    0x45: XMP,
    0x46: YMP,
    0x47: STX,
    0x48: STY,
    0xFF: LOG
}