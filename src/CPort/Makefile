CFLAGS = -W

NAME = emulator_port_cli
NAME_EXE = emulated

SRC_CLI =	./emulator_port_cli.c

SRC =	./emulator_port.c	\
		./instructions.c	\
		./rom_file_format.c

SRC_EXE =	./rom_to_exe.c

OBJ = $(SRC:.c=.o)

OBJ_CLI = $(SRC_CLI:.c=.o)

OBJ_EXE = $(SRC_EXE:.c=.o)

ifeq ($(OS),Windows_NT)
    EXT = exe
else
    EXT = out
endif

$(NAME): compile
	gcc $(OBJ) $(OBJ_CLI) -o $(NAME).$(EXT)

compile_to_exe: $(OBJ) $(OBJ_EXE)
	py ./rom_to_ctxt.py > crom.c
	gcc -c crom.c -o crom.o
	gcc $(OBJ) $(OBJ_EXE) ./crom.o -o $(NAME_EXE).$(EXT)

compile: $(OBJ) $(OBJ_CLI)

clean:
	rm -f $(OBJ) $(OBJ_CLI) $(OBJ_EXE)

fclean: clean
		rm -f $(NAME).$(EXT) $(NAME_EXE).$(EXT)

re: clean $(NAME)

.PHONY: re
