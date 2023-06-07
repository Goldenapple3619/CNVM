from .config_file_parser import *

def read_config_file(path: str) -> str:
    content: str = ''
    with open(path, 'r') as f:
        content = f.read()
    
    return (content)

def load_config_from_file(path: str):
    config: dict = {}
    content: str = read_config_file(path)

    config_file_parser(config, content)

    return (config)
