import yaml
from pathlib import Path

def import_config(file: Path):
    with open(file, "r") as f:
        config = yaml.safe_load(f)
    return config

def load_config(page: str) -> dict:
    with open(f"config/{page}.yaml") as f:
        return yaml.safe_load(f)