#ifndef ROM_FILE_FORMAT_H_
    #define ROM_FILE_FORMAT_H_

    #include "emulator_port.h"

    typedef struct rom_s {
        int magic[2];
        int memory_mapper;
        registries_t *registries;

        int **ram_memory;
        int **prg_memory;
    } rom_t;

    rom_t *rom_from_file(char *path);
    void fill_rom(rom_t *rom, char *path);
    void destroy_rom(rom_t *rom);
    rom_t *create_rom(void);
    rom_t *rom_from_fp(FILE *fp);
    void fill_rom_from_fp(rom_t *rom, FILE *fp);

#endif /* ROM_FILE_FORMAT_H_ */
