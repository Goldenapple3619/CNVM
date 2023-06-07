const fs = require("fs");

module.exports = {
    ROM: class {
        constructor(memory_mapper) {
            this.magic = [0xFA, 0xBA];
            this.memory_mapper = memory_mapper;

            this.registries = {
                "x": 0x00,
                "y": 0x00,
                "temp": 0x00,
                "fetched": 0x00,
                "ptr_prg": 0x00,
                "ptr_mem": 0x00,
                "prg_device": 0x01,
                "mem_device": 0x01
            };

            this.prg_memory = {};
            this.ram_memory = {};
        }

        save_to_file(path) {

        }

        load_from_file(path) {
            const buffer = Buffer.alloc(0x02, 0x00);
            const fd = fs.openSync(path, "r", null);

            if (fd <= 0)
                throw `cannot open file ${path}.`;

            fs.readSync(fd, buffer, 0, 2);
            console.log(buffer);
            fs.readSync(fd, buffer, 0, 2);
            console.log(buffer);
        }
    }
}
