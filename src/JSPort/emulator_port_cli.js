modules = [
    "./rom_file_format.js",
    "./emulator_port.js",
    "./instructions.js",
    "./common.js"
]

function load_modules()
{
    var arr = Array();

    modules.forEach(element => {
        arr[element.slice(2, element.length).split('.')[0]] = require(element);
    });
    return (arr);
}

function main(argc, argv)
{
    const loaded_modules = load_modules();
    let temp = new (loaded_modules["emulator_port"]).MotherBoard();
    let ram = loaded_modules["common"].get_device(temp, 0x01);
    let cpu =  loaded_modules["common"].get_device(temp, 0x02);
    let rom = new (loaded_modules["rom_file_format"]).ROM(0);

    if (argc < 3)
        return (1);
    rom.load_from_file(argv[2]);


    ram.write(0x01, 0x01);
    cpu.clock(temp);
    cpu.clock(temp);

    return (0);
}

process.exit(main(process.argv.length, process.argv));
