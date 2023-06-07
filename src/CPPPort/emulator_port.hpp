#ifndef EMULATOR_PORT_HPP_
    #define EMULATOR_PORT_HPP_

    class Registries {
        public:
            int x;
            int y;
            int temp;
            int fetched;

            int ptr_prg;
            int ptr_mem;
            int mem_device;
            int prg_device;

            Registries(int _x, int _y, int _temp, int _ptr_prg, int _ptr_mem) {
                x = _x;
                y = _y;
                temp = _temp;
                fetched = 0x00;

                ptr_prg = _ptr_prg;
                ptr_mem = _ptr_mem;

                mem_device = 0x00;
                prg_device = 0x00;
            }
    };

    class CPU {
        public:
            int id;
            Registries *registries;
        
            CPU() {
                id = 0x02;
                registries = new Registries(0x00, 0x00, 0x00, 0x00, 0x00);
            }
    };

#endif /* EMULATOR_PORT_HPP_ */