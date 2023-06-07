#include "emulator_port.h"

#include <stdio.h>

int NUL(mother_board_t *mother_board, void *dev)
{
    return (0x00);
}

int ICX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x += 1;
    return (0x00);
}

int ICY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y += 1;
    return (0x00);
}

int ADX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x += casted_dev->registries->temp;
    return (0x00);
}

int ADY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y += casted_dev->registries->temp;
    return (0x00);
}

int SUX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x -= casted_dev->registries->temp;
    return (0x00);
}

int SUY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y -= casted_dev->registries->temp;
    return (0x00);
}

int MUX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x *= casted_dev->registries->temp;
    return (0x00);
}

int MUY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y *= casted_dev->registries->temp;
    return (0x00);
}

int DIX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x /= casted_dev->registries->temp;
    return (0x00);
}

int DIY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x /= casted_dev->registries->temp;
    return (0x00);
}

int MOX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x %= casted_dev->registries->temp;
    return (0x00);
}

int MOY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y %= casted_dev->registries->temp;
    return (0x00);
}


int TVF(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->temp = casted_dev->registries->fetched;
    return (0x00);
}

int END(mother_board_t *mother_board, void *dev)
{
    return (0x00);
}

int TVX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->temp = casted_dev->registries->x;
    return (0x00);
}

int TVY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->temp = casted_dev->registries->y;
    return (0x00);
}

int PPX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->ptr_prg = casted_dev->registries->x;
    casted_dev->registries->ptr_prg -= 1;
    return (0x00);
}

int PPY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->ptr_prg = casted_dev->registries->y;
    casted_dev->registries->ptr_prg -= 1;
    return (0x00);
}

int MPX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->ptr_mem = casted_dev->registries->x;
    return (0x00);
}

int MPY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->ptr_mem = casted_dev->registries->y;
    return (0x00);
}

int DMX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->mem_device = casted_dev->registries->x;
    return (0x00);
}

int DMY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->mem_device = casted_dev->registries->y;
    return (0x00);
}

int DPX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->prg_device = casted_dev->registries->x;
    return (0x00);
}

int DPY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->prg_device = casted_dev->registries->y;
    return (0x00);
}

int XVY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = casted_dev->registries->y;
    return (0x00);
}

int YVX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = casted_dev->registries->x;
    return (0x00);
}

int XVT(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = casted_dev->registries->temp;
    return (0x00);
}

int YVT(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = casted_dev->registries->temp;
    return (0x00);
}

int XVF(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = casted_dev->registries->fetched;
    return (0x00);
}

int YVF(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = casted_dev->registries->fetched;
    return (0x00);
}

int MVX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    if (mother_board->ram->id == casted_dev->registries->mem_device)
        mother_board->ram->write(casted_dev->registries->ptr_mem, casted_dev->registries->x, mother_board->ram);
    return (0x00);
}

int MVY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    if (mother_board->ram->id == casted_dev->registries->mem_device)
        mother_board->ram->write(casted_dev->registries->ptr_mem, casted_dev->registries->y, mother_board->ram);
    return (0x00);
}

int RDM(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    if (mother_board->ram->id == casted_dev->registries->mem_device)
        casted_dev->registries->fetched = mother_board->ram->read(casted_dev->registries->ptr_mem, mother_board->ram);
    return (0x00);
}

int TMX(mother_board_t *mother_board, void *dev)
{
    printf("TMX not implemented.\n");
    return (0x00);
}

int TMY(mother_board_t *mother_board, void *dev)
{
    printf("TMX not implemented.\n");
    return (0x00);
}

int ANX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x &= casted_dev->registries->temp;
    return (0x00);
}

int ANY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y &= casted_dev->registries->temp;
    return (0x00);
}

int ORX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x |= casted_dev->registries->temp;
    return (0x00);
}

int ORY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y |= casted_dev->registries->temp;
    return (0x00);
}

int XOX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x ^= casted_dev->registries->temp;
    return (0x00);
}

int XOY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y ^= casted_dev->registries->temp;
    return (0x00);
}

int LSX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x <<= casted_dev->registries->temp;
    return (0x00);
}

int LSY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y <<= casted_dev->registries->temp;
    return (0x00);
}

int RSX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x >>= casted_dev->registries->temp;
    return (0x00);
}

int RSY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y >>= casted_dev->registries->temp;
    return (0x00);
}

int EQX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = casted_dev->registries->x == casted_dev->registries->temp;
    return (0x00);
}

int EQY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = casted_dev->registries->y == casted_dev->registries->temp;
    return (0x00);
}

int NQX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = casted_dev->registries->x != casted_dev->registries->temp;
    return (0x00);
}

int NQY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = casted_dev->registries->y != casted_dev->registries->temp;
    return (0x00);
}

int SPX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = casted_dev->registries->x > casted_dev->registries->temp;
    return (0x00);
}

int SPY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = casted_dev->registries->y > casted_dev->registries->temp;
    return (0x00);
}

int INX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = casted_dev->registries->x < casted_dev->registries->temp;
    return (0x00);
}

int INY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = casted_dev->registries->y < casted_dev->registries->temp;
    return (0x00);
}

int IEX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = casted_dev->registries->x <= casted_dev->registries->temp;
    return (0x00);
}

int IEY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = casted_dev->registries->y <= casted_dev->registries->temp;
    return (0x00);
}

int SEX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = casted_dev->registries->x >= casted_dev->registries->temp;
    return (0x00);
}

int SEY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = casted_dev->registries->y >= casted_dev->registries->temp;
    return (0x00);
}

int NOX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = ~casted_dev->registries->x;
    return (0x00);
}

int NOY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = ~casted_dev->registries->y;
    return (0x00);
}

int CNE(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    if (!casted_dev->registries->temp)
        casted_dev->registries->ptr_prg += 1;
    return (0x00);
}

int HALT(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->ptr_prg -= 1;
    return (0x00);
}

int XPP(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = casted_dev->registries->ptr_prg;
    return (0x00);
}

int YPP(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = casted_dev->registries->ptr_prg;
    return (0x00);
}

int SWX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;
    int temp;

    temp = casted_dev->registries->temp;
    casted_dev->registries->temp = casted_dev->registries->x;
    casted_dev->registries->x = temp;
    return (0x00);
}

int SWY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;
    int temp;

    temp = casted_dev->registries->temp;
    casted_dev->registries->temp = casted_dev->registries->y;
    casted_dev->registries->y = temp;
    return (0x00);
}

int REX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = 0x00;
    return (0x00);
}

int REY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = 0x00;
    return (0x00);
}

int XMP(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->x = casted_dev->registries->ptr_mem;
    return (0x00);
}

int YMP(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->y = casted_dev->registries->ptr_mem;
    return (0x00);
}

int STX(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->ptr_prg += 1;
    if (mother_board->ram->id == casted_dev->registries->prg_device)
        casted_dev->registries->x = mother_board->ram->read(casted_dev->registries->ptr_prg, mother_board->ram);
    return (0x00);
}

int STY(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    casted_dev->registries->ptr_prg += 1;
    if (mother_board->ram->id == casted_dev->registries->prg_device)
        casted_dev->registries->y = mother_board->ram->read(casted_dev->registries->ptr_prg, mother_board->ram);
    return (0x00);
}

int LOG(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    printf("%c", casted_dev->registries->temp);
    return (0x00);
}

int IDN(mother_board_t *mother_board, void *dev)
{
    cpu_t *casted_dev = (cpu_t *)dev;

    return (casted_dev->id);
}
