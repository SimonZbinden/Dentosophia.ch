import yaml
from pathlib import Path

def import_config(file: Path):
    with open(file, "r") as f:
        config = yaml.safe_load(f)
    return config