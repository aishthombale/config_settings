import flatdict
import yaml
import json
from configparser import ConfigParser


def to_flatdict(file_path):
    raw_file_path = file_path.replace("\t","\\t").replace("\n","\\n").replace("\b","\\b").replace("\f","\\f").replace("\r","\\r")
    try:
        if file_path.endswith(".yaml") or file_path.endswith(".yml") :
            return yaml_to_flatdict(raw_file_path)
        elif file_path.endswith(".cfg"):
            return cfg_to_flatdict(raw_file_path)
    except:
        return "File path or name is not correct, lease check again wirh correct filename."


# yaml to flatdict
def yaml_to_flatdict(file_path):
    with open(file_path) as file:
        documents = yaml.safe_load(file)
    value_yaml = flatdict.FlatDict(documents)
    return value_yaml


# .cfg(.ini) to flatdict
def cfg_to_flatdict(file_path):
    config = ConfigParser()
    config.read(file_path)
    sections = config._sections
    value_cfg = flatdict.FlatDict(sections)
    return value_cfg


# edit the data
def add_key_json(path, key, value):
    new_path = path.replace("\t","\\t").replace("\n","\\n").replace("\b","\\b").replace("\f","\\f").replace("\r","\\r")
    with open(new_path, 'r') as f1:
        config = json.load(f1)
        # print(config)
        config[key] = value

    # write it back to the file
    with open(new_path, 'w') as f:
        json.dump(config, f)

