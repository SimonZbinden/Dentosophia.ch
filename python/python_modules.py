import yaml
from pathlib import Path

def import_config(file: Path):
    """
    Load a YAML configuration file.
    Args:
        file (Path): Path to the YAML config file.
    Returns:
        dict: The loaded configuration as a dictionary.
    """
    with open(file, "r") as f:
        config = yaml.safe_load(f)
    return config
    
def load_configs(configs_path: Path) -> dict:
    """
    Load all YAML configuration files from the specified directory.

    Args:
        configs_path (Path): Path to the directory containing YAML config files.

    Returns:
        dict: A dictionary where keys are config names (without .yaml) and values are the loaded configurations.
    """
    configs = {}
    for config_file in configs_path.glob("*.yaml"):
        config_name = config_file.stem
        configs[config_name] = import_config(config_file)
    return configs