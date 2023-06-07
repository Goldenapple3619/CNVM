def config_file_parser(dest: dict, src: str) -> None:
    for item in src.strip().split('\n'):
        key, value = map(lambda x: x.strip(), item.split(':'))
        dest[key] = value
