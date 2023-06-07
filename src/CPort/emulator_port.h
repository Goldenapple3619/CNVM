#ifndef EMULATOR_PORT_H
    #define EMULATOR_PORT_H

    #include "instructions.h"

    #include <stdlib.h>

    struct mother_board_s;

    typedef struct registries_s {
        int x;
        int y;
        int temp;
        int fetched;

        int ptr_prg;
        int ptr_mem;
        int prg_device;
        int mem_device;
    } registries_t;

    typedef struct op_s {
        int id;

        int (*instruction)(struct mother_board_s *mother_board, void *dev);
    } op_t;

    typedef struct ram_s {
        int id;

        int (*req)(int code, struct mother_board_s *mother_board, struct ram_s *self);
        int (*read)(int addr, struct ram_s *self);
        int (*write)(int addr, int value, struct ram_s *self);

        int *memory;

        int size;
    } ram_t;

    typedef struct cpu_s {
        int id;
    
        int (*req)(int code, struct mother_board_s *mother_board, struct cpu_s *self);

        void (*clock)(struct mother_board_s *mother_board, struct cpu_s *self);

        registries_t *registries;
    } cpu_t;

    typedef struct mother_board_s {
        ram_t *ram;
        cpu_t *cpu;
    } mother_board_t;

    static const op_t OP_CPU[][2] = {
        {0x00, &NUL},
        {0x01, &ICX},
        {0x02, &ICY},
        {0x03, &ADX},
        {0x04, &ADY},
        {0x05, &SUX},
        {0x06, &IDN},
        {0x07, &SUY},
        {0x08, &MUX},
        {0x09, &MUY},
        {0x0A, &DIX},
        {0x0B, &DIY},
        {0x0C, &MOX},
        {0x0D, &MOY},
        {0x0E, &TVF},
        {0x0F, &END},
        {0x10, &TVX},
        {0x11, &TVY},
        {0x12, &PPX},
        {0x13, &PPY},
        {0x14, &MPX},
        {0x15, &MPY},
        {0x16, &DMX},
        {0x17, &DMY},
        {0x18, &DPX},
        {0x19, &DPY},
        {0x1A, &XVY},
        {0x1B, &YVX},
        {0x1C, &XVT},
        {0x1D, &YVT},
        {0x1E, &XVF},
        {0x1F, &YVF},
        {0x20, &MVX},
        {0x21, &MVY},
        {0x22, &RDM},
        {0x23, &TMX},
        {0x24, &TMY},
        {0x25, &ANX},
        {0x26, &ANY},
        {0x27, &ORX},
        {0x28, &ORY},
        {0x29, &XOX},
        {0x2A, &XOY},
        {0x2B, &LSX},
        {0x2C, &LSY},
        {0x2D, &RSX},
        {0x2E, &RSY},
        {0x2F, &EQX},
        {0x30, &EQY},
        {0x31, &NQX},
        {0x32, &NQY},
        {0x33, &SPX},
        {0x34, &SPY},
        {0x35, &INX},
        {0x36, &INY},
        {0x37, &IEX},
        {0x38, &IEY},
        {0x39, &SEX},
        {0x3A, &SEY},
        {0x3B, &NOX},
        {0x3C, &NOY},
        {0x3D, &CNE},
        {0x3E, &HALT},
        {0x3F, &XPP},
        {0x40, &YPP},
        {0x41, &SWX},
        {0x42, &SWY},
        {0x43, &REY},
        {0x44, &REX},
        {0x45, &XMP},
        {0x46, &YMP},
        {0x47, &STX},
        {0x48, &STY},
        {0xFF, &LOG},
        {-1, NULL}
    };

    int cpu_req(int code, mother_board_t *mother_board, cpu_t *self);
    void clock(mother_board_t *mother_board, cpu_t *cpu);
    int read_ram(int addr, ram_t *ram);
    int write_ram(int addr, int value, ram_t *ram);
    registries_t *create_registries(void);
    cpu_t *create_cpu(void);
    ram_t *create_ram(int size);
    mother_board_t *create_mother_board(void);
    void destroy_ram(ram_t *ram);
    void destroy_cpu(cpu_t *cpu);
    void destroy_mother_board(mother_board_t *mb);

#endif /* EMULATOR_PORT_H */
