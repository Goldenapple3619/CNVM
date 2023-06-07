#include <stdio.h>
#include <stdlib.h>

#include "emulator_port.h"
#include "rom_file_format.h"

void show_rom(rom_t *rom)
{
	printf("magic: %x%x\n", rom->magic[0], rom->magic[1]);
	printf("mapper: %x\n", rom->memory_mapper);
	printf("registries:\n");
	printf("  x: %x\n", rom->registries->x);
	printf("  y: %x\n", rom->registries->y);
	printf("  temp: %x\n", rom->registries->temp);
	printf("  fetched: %x\n", rom->registries->fetched);
	printf("  ptr_prg: %x\n", rom->registries->ptr_prg);
	printf("  ptr_mem: %x\n", rom->registries->ptr_mem);
	printf("  prg_device: %x\n", rom->registries->prg_device);
	printf("  mem_device: %x\n\n", rom->registries->mem_device);
	printf("prg_memory:\n");
	for (int i = 0; rom->prg_memory && rom->prg_memory[i]; ++i) {
		if (i % 17 == 16)
			printf("\n");
		printf("$%x: %x\t", rom->prg_memory[i][0], rom->prg_memory[i][1]);
	}
	printf("\n\nram_memory:\n");
	for (int i = 0; rom->ram_memory && rom->ram_memory[i]; ++i) {
		if (i % 17 == 16)
			printf("\n");
		printf("$%x: %x\t", rom->ram_memory[i][0], rom->ram_memory[i][1]);
	}
	printf("\n");
}

void load_rom_to_ram(mother_board_t *mother_board, rom_t *rom)
{
	for (int i = 0; rom->prg_memory[i]; ++i) {
		if (rom->prg_memory[i][1] != 0)
			mother_board->ram->write(rom->prg_memory[i][0], rom->prg_memory[i][1], mother_board->ram);
	}
	for (int i = 0; rom->ram_memory[i]; ++i) {
		if (rom->ram_memory[i][1] != 0)
			mother_board->ram->write(rom->ram_memory[i][0], rom->ram_memory[i][1], mother_board->ram);
	}
	mother_board->cpu->registries->x = rom->registries->x;
	mother_board->cpu->registries->y = rom->registries->y;
	mother_board->cpu->registries->temp = rom->registries->temp;
	mother_board->cpu->registries->fetched = rom->registries->fetched;
	mother_board->cpu->registries->ptr_prg = rom->registries->ptr_prg;
	mother_board->cpu->registries->ptr_mem = rom->registries->ptr_mem;
	mother_board->cpu->registries->prg_device = rom->registries->prg_device;
	mother_board->cpu->registries->mem_device = rom->registries->mem_device;
}

int main(int argc, char **argv)
{
	if (argc == 1)
		return (1);
	mother_board_t *mb = create_mother_board();
	rom_t *rom = rom_from_file(argv[1]);

	if (!mb|| !mb->cpu || !mb->ram || !mb->cpu->registries || !mb->ram->memory ||
		!rom || !rom->registries || !rom->prg_memory || !rom->ram_memory)
		return (1);
	load_rom_to_ram(mb, rom);
	while (mb->ram->read(mb->cpu->registries->ptr_prg, mb->ram) != 0x3E) {
		mb->cpu->clock(mb, mb->cpu);
	}

	destroy_mother_board(mb);
	destroy_rom(rom);
	return (0);
}