CASM =	./asm/std.rsm

DEBUG =	./asm/casm.rsm

BINARIES =	std.out \
			casm.out

TESTS =	./test/test_sample_0 \
		./test/test_sample_1 \
		./test/test_sample_2 \
		./test/test_sample_3

PYC =	./src/PyPort/lib/CNEngine/__pycache__ \
	./src/PyPort/lib/CNEngine/src/Component/__pycache__ \
	./src/PyPort/lib/CNEngine/src/HUD/__pycache__ \
	./src/PyPort/lib/CNEngine/src/Objects/__pycache__ \
	./src/PyPort/lib/CNEngine/src/Packages/DBHandler/__pycache__ \
	./src/PyPort/lib/CNEngine/src/Packages/DBHandler/src/CNQL/__pycache__ \
	./src/PyPort/lib/CNEngine/src/Packages/DBHandler/src/__pycache__ \
	./src/PyPort/lib/CNEngine/src/Packages/DBHandler/src/_libs/EZHost/__pycache__ \
	./src/PyPort/lib/CNEngine/src/Packages/EZCNQL/__pycache__ \
	./src/PyPort/lib/CNEngine/src/Packages/GLD/__pycache__ \
	./src/PyPort/lib/CNEngine/src/Packages/__pycache__ \
	./src/PyPort/lib/CNEngine/src/Preset/__pycache__ \
	./src/PyPort/lib/CNEngine/src/Shaders/__pycache__ \
	./src/PyPort/lib/CNEngine/src/__pycache__ \
	./src/PyPort/lib/EZHost/__pycache__ \
	./src/PyPort/lib/RomFF/__pycache__ \
	./src/PyPort/mother_board/__pycache__ \
	./src/PyPort/mother_board/bios_chip/__pycache__ \
	./src/PyPort/mother_board/disk/__pycache__ \
	./src/PyPort/mother_board/external_ports/__pycache__ \
	./src/PyPort/mother_board/external_ports/hdmi0/screen0/__pycache__ \
	./src/PyPort/mother_board/external_ports/usb0/mouse0/__pycache__ \
	./src/PyPort/mother_board/external_ports/usb1/keyboard0/__pycache__ \
	./src/PyPort/mother_board/external_ports/usb2/rom0/__pycache__ \
	./src/PyPort/mother_board/memory/__pycache__ \
	./src/PyPort/mother_board/processor/__pycache__ \
	./src/PyPort/src/config_file/__pycache__ \
	./src/casm_lang/lib/RomFF/__pycache__ \
	./src/casm_lang/__pycache__


ifeq ($(OS),Windows_NT)
    PYTHON_INTERPRETER = py
else
    PYTHON_INTERPRETER = /usr/bin/python3
endif

prepare:
	pip install -r requirements.txt

AC:
	@$(PYTHON_INTERPRETER) ./casm.py $(FILES)

compile_std:
	make AC FILES=$(CASM)

stat:
	$(PYTHON_INTERPRETER) ./tools/stats.py

host:
	$(PYTHON_INTERPRETER) ./src/PyPort/webview.py

compile_debug:
	@make AC FILES=$(DEBUG)

debug:
	@make AC FILES=$(DEBUG)
	$(PYTHON_INTERPRETER) ./src/PyPort/debug.py ./casm.out

tests_run:
	@$(PYTHON_INTERPRETER) ./test_tool.py $(TESTS)

clean:
	make -C ./src/CPort clean
	rm -rf $(PYC)

fclean: clean
	make -C ./src/CPort fclean
	rm -rf $(BINARIES)

build:
	make -C ./src/CPort re
	make compile_debug
	make clean

rom_to_bin: build
		cp ./casm.out ./src/CPort/obj
		make -C ./src/CPort compile_to_exe

.PHONY: build clean fclean tests_run host stat
