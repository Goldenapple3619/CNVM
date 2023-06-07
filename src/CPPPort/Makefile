CFLAGS = -W

NAME = emulator_port_cli

SRC_CLI =	./emulator_port_cli.cpp

SRC =	./emulator_port.cpp	\
		./instructions.cpp

OBJ = $(SRC:.cpp=.o)

OBJ_CLI = $(SRC_CLI:.cpp=.o)

ifeq ($(OS),Windows_NT)
    EXT = exe
else
    EXT = out
endif

$(NAME): compile
	g++ $(OBJ) $(OBJ_CLI) -o $(NAME).$(EXT)

compile: $(OBJ) $(OBJ_CLI)

clean:
	rm -f $(OBJ) $(OBJ_CLI)

fclean: clean
		rm -f $(NAME).$(EXT)

re: clean $(NAME)

.PHONY: re
