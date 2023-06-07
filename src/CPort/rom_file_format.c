#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "emulator_port.h"
#include "rom_file_format.h"

rom_t *create_rom(void)
{
    rom_t *rom = malloc(sizeof(rom_t));

    if (!rom)
        return (NULL);
    rom->magic[0] = 0xFA;
    rom->magic[1] = 0xBA;
    rom->memory_mapper = 0x00;
    rom->registries = create_registries();

    rom->ram_memory = NULL;
    rom->prg_memory = NULL;
    return (rom);
}

void destroy_rom(rom_t *rom)
{
    int i = 0;

    if (!rom)
        return;
    if (rom->registries)
        free(rom->registries);
    if (rom->ram_memory) {
        for (i = 0; rom->ram_memory[i]; ++i) {
            free(rom->ram_memory[i]);
        }
        free(rom->ram_memory);
    }
    if (rom->prg_memory) {
        for (i = 0; rom->prg_memory[i]; ++i) {
            free(rom->prg_memory[i]);
        }
        free(rom->prg_memory);
    }
    free(rom);
}

unsigned char *read_n(FILE *fd, int size)
{
    unsigned char *buffer = malloc(sizeof(unsigned char) * (size + 1));
    int i = 0;

    if (!buffer)
        return (NULL);
    fread(buffer, size, 1, fd);

    buffer[size] = 0;
    return (buffer);
}

void append_str(char **str, char new_char)
{
    int len = (*str ? strlen(*str) : 0);
    char *temp = malloc(sizeof(char) * (len + 2));

    for (int i = 0; str && i < len; ++i) {
        temp[i] = (*str)[i];
    }
    if (*str)
        free(*str);
    *str = temp;
    temp[len] = new_char;
    temp[len + 1] = 0;
}

int int_from_bytes(unsigned char *bytes, int size)
{
    int result = 0;

    for (int i = 0; i < size; i++) {
        result |= (int)bytes[i] << (8 * (size - 1 - i));
    }
    return (result);
}

void fill_registry(registries_t *registries, char *entry, int value)
{
    if (!strcmp(entry, "x"))
        registries->x = value;
    if (!strcmp(entry, "y"))
        registries->y = value;
    if (!strcmp(entry, "temp"))
        registries->temp = value;
    if (!strcmp(entry, "fetched"))
        registries->fetched = value;
    if (!strcmp(entry, "ptr_prg"))
        registries->ptr_prg = value;
    if (!strcmp(entry, "ptr_mem"))
        registries->ptr_mem = value;
    if (!strcmp(entry, "prg_device"))
        registries->prg_device = value;
    if (!strcmp(entry, "mem_device"))
        registries->mem_device = value;
}

void write_rom_to_file(rom_t *rom, char *path)
{
    FILE *fd = fopen(path, "rb");

    fclose(fd);
}

void fill_rom(rom_t *rom, char *path)
{
    FILE *fd = fopen(path, "rb");
    unsigned char  *buffer;
    int temp;
    char *str;
    int size = 0;

    buffer = read_n(fd, 2);
    rom->magic[0] = ((int)buffer[0] << 8) | (int)buffer[1];
    free(buffer);
    buffer = read_n(fd, 2);
    rom->magic[1] = ((int)buffer[0] << 8) | (int)buffer[1];
    free(buffer);
    free(read_n(fd, 1));
    buffer = read_n(fd, 1);
    rom->memory_mapper = (int)buffer[1];
    free(buffer);
    free(read_n(fd, 1));
    buffer = read_n(fd, 1);
    temp = buffer[0];
    free(buffer);
    free(read_n(fd, 1));

    for (int i = 0; i < temp; ++i) {
        unsigned char temp_char = 0;
        str = NULL;

        while (temp_char != ':') {
            buffer = read_n(fd, 1);
            temp_char = buffer[0];
            if (temp_char != ':')
                append_str(&str, temp_char);
            free(buffer);
        }
        buffer = read_n(fd, 1);
        size = buffer[0];
        free(buffer);
        buffer = read_n(fd, size);
        fill_registry(rom->registries, str, int_from_bytes(buffer, size));
        free(buffer);
        free(str);
    }
    free(read_n(fd, 1));

    buffer = read_n(fd, 1);
    size = buffer[0];
    free(buffer);

    buffer = read_n(fd, size);
    temp = int_from_bytes(buffer, size);
    free(buffer);

    free(read_n(fd, 1));
    rom->ram_memory = malloc(sizeof(int *) * (temp + 1));
    for (int i = 0; i < temp; ++i) {
        rom->ram_memory[i] = malloc(sizeof(int) * 2);

        buffer = read_n(fd, 1);
        size = buffer[0];
        free(buffer);
        buffer = read_n(fd, size);
        rom->ram_memory[i][0] = int_from_bytes(buffer, size);
        free(buffer);

        buffer = read_n(fd, 1);
        size = buffer[0];
        free(buffer);
        buffer = read_n(fd, size);
        rom->ram_memory[i][1] = int_from_bytes(buffer, size);
        free(buffer);
    }
    rom->ram_memory[temp] = NULL;

    free(read_n(fd, 1));

    buffer = read_n(fd, 1);
    size = buffer[0];
    free(buffer);

    buffer = read_n(fd, size);
    temp = int_from_bytes(buffer, size);
    free(buffer);

    free(read_n(fd, 1));
    rom->prg_memory = malloc(sizeof(int *) * (temp + 1));
    for (int i = 0; i < temp; ++i) {
        rom->prg_memory[i] = malloc(sizeof(int) * 2);

        buffer = read_n(fd, 1);
        size = buffer[0];
        free(buffer);
        buffer = read_n(fd, size);
        rom->prg_memory[i][0] = int_from_bytes(buffer, size);
        free(buffer);

        buffer = read_n(fd, 1);
        size = buffer[0];
        free(buffer);
        buffer = read_n(fd, size);
        rom->prg_memory[i][1] = int_from_bytes(buffer, size);
        free(buffer);
    }
    rom->prg_memory[temp] = NULL;

    fclose(fd);
}

void fill_rom_from_fp(rom_t *rom, FILE *fp)
{
    unsigned char  *buffer;
    int temp;
    char *str;
    int size = 0;

    buffer = read_n(fp, 2);
    rom->magic[0] = ((int)buffer[0] << 8) | (int)buffer[1];
    free(buffer);
    buffer = read_n(fp, 2);
    rom->magic[1] = ((int)buffer[0] << 8) | (int)buffer[1];
    free(buffer);
    free(read_n(fp, 1));
    buffer = read_n(fp, 1);
    rom->memory_mapper = (int)buffer[1];
    free(buffer);
    free(read_n(fp, 1));
    buffer = read_n(fp, 1);
    temp = buffer[0];
    free(buffer);
    free(read_n(fp, 1));

    for (int i = 0; i < temp; ++i) {
        unsigned char temp_char = 0;
        str = NULL;

        while (temp_char != ':') {
            buffer = read_n(fp, 1);
            temp_char = buffer[0];
            if (temp_char != ':')
                append_str(&str, temp_char);
            free(buffer);
        }
        buffer = read_n(fp, 1);
        size = buffer[0];
        free(buffer);
        buffer = read_n(fp, size);
        fill_registry(rom->registries, str, int_from_bytes(buffer, size));
        free(buffer);
        free(str);
    }
    free(read_n(fp, 1));

    buffer = read_n(fp, 1);
    size = buffer[0];
    free(buffer);

    buffer = read_n(fp, size);
    temp = int_from_bytes(buffer, size);
    free(buffer);

    free(read_n(fp, 1));
    rom->ram_memory = malloc(sizeof(int *) * (temp + 1));
    for (int i = 0; i < temp; ++i) {
        rom->ram_memory[i] = malloc(sizeof(int) * 2);

        buffer = read_n(fp, 1);
        size = buffer[0];
        free(buffer);
        buffer = read_n(fp, size);
        rom->ram_memory[i][0] = int_from_bytes(buffer, size);
        free(buffer);

        buffer = read_n(fp, 1);
        size = buffer[0];
        free(buffer);
        buffer = read_n(fp, size);
        rom->ram_memory[i][1] = int_from_bytes(buffer, size);
        free(buffer);
    }
    rom->ram_memory[temp] = NULL;

    free(read_n(fp, 1));

    buffer = read_n(fp, 1);
    size = buffer[0];
    free(buffer);

    buffer = read_n(fp, size);
    temp = int_from_bytes(buffer, size);
    free(buffer);

    free(read_n(fp, 1));
    rom->prg_memory = malloc(sizeof(int *) * (temp + 1));
    for (int i = 0; i < temp; ++i) {
        rom->prg_memory[i] = malloc(sizeof(int) * 2);

        buffer = read_n(fp, 1);
        size = buffer[0];
        free(buffer);
        buffer = read_n(fp, size);
        rom->prg_memory[i][0] = int_from_bytes(buffer, size);
        free(buffer);

        buffer = read_n(fp, 1);
        size = buffer[0];
        free(buffer);
        buffer = read_n(fp, size);
        rom->prg_memory[i][1] = int_from_bytes(buffer, size);
        free(buffer);
    }
    rom->prg_memory[temp] = NULL;

    fclose(fp);
}

rom_t *rom_from_file(char *path)
{
    rom_t *rom = create_rom();

    if (!rom)
        return (NULL);
    fill_rom(rom, path);
    return (rom);
}

rom_t *rom_from_fp(FILE *fp)
{
    rom_t *rom = create_rom();

    if (!rom || !fp)
        return (NULL);
    fill_rom_from_fp(rom, fp);
    return (rom);
}
