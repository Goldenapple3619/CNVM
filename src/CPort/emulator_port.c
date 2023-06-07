#include <stdio.h>
#include <stdlib.h>

#include "emulator_port.h"

int cpu_req(int code, mother_board_t *mother_board, cpu_t *self)
{
	int i = 0;
	int (*instruction)(struct mother_board_s *mother_board, void *dev) = &NUL;

	for (i; (OP_CPU[i]->instruction != NULL || OP_CPU[i]->id != -1) && OP_CPU[i]; ++i) {
		if (OP_CPU[i]->id == code)
			instruction = OP_CPU[i]->instruction;
	}
	return (instruction(mother_board, self));
}

void clock(mother_board_t *mother_board, cpu_t *cpu)
{
	if (cpu->registries->prg_device == mother_board->ram->id)
		cpu->req(mother_board->ram->read(cpu->registries->ptr_prg, mother_board->ram), mother_board, cpu);
	cpu->registries->ptr_prg += 1;
}

int read_ram(int addr, ram_t *ram)
{
	if (!ram)
		return (0x00);
	if (addr < 0x00 || addr >= ram->size)
		return (0x00);
	return ram->memory[addr];
}

int write_ram(int addr, int value, ram_t *ram)
{
	if (!ram)
		return (0x00);
	if (addr < 0x00 || addr >= ram->size)
		return (0x00);
	ram->memory[addr] = value;
	return (0x01);
}

registries_t *create_registries(void)
{
	registries_t *reg = malloc(sizeof(registries_t));

	if (!reg)
		return (NULL);
	reg->x = 0x00;
	reg->y = 0x00;
	reg->temp = 0x00;
	reg->fetched = 0x00;

	reg->ptr_prg = 0x00;
	reg->ptr_mem = 0x00;
	reg->prg_device = 0x01;
	reg->mem_device = 0x01;
	return (reg);
}

cpu_t *create_cpu(void)
{
	cpu_t *cpu = malloc(sizeof(cpu_t));

	if (!cpu)
		return (NULL);
	cpu->req = &cpu_req;
	cpu->id = 0x02;
	cpu->clock = &clock;
	cpu->registries = create_registries();
	return (cpu);
}

ram_t *create_ram(int size)
{
	ram_t *ram = malloc(sizeof(ram_t));

	if (!ram)
		return (NULL);
	ram->memory = malloc(sizeof(int) * size);
	ram->size = size;
	ram->id = 0x01;
	ram->read = &read_ram;
	ram->write = &write_ram;
	if (!ram->memory)
		return (ram);
	for (int i = 0; i < size; ++i)
		ram->memory[i] = 0x00;
	return (ram);
}

mother_board_t *create_mother_board(void)
{
	mother_board_t *mb = malloc(sizeof(mother_board_t));

	if (!mb)
		return (NULL);
	mb->cpu = create_cpu();
	mb->ram = create_ram(8 * 1024);
	return (mb);
}

void destroy_ram(ram_t *ram)
{
	if (!ram)
		return;
	if (ram->memory)
    	free(ram->memory);
	free(ram);
}

void destroy_cpu(cpu_t *cpu)
{
	if (!cpu)
		return;
	if (cpu->registries)
		free(cpu->registries);
	free(cpu);
}

void destroy_mother_board(mother_board_t *mb)
{
	if (!mb)
		return;
	destroy_ram(mb->ram);
	destroy_cpu(mb->cpu);
	free(mb);
}
