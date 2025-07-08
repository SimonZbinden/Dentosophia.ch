from pathlib import Path
from python import modules

# load config
config_path = Path("/config.yaml")
config = modules.import_config(config_path)