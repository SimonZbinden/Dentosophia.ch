from pathlib import Path

from python import render, python_modules

### LOAD CONFIG ###
configs_path = Path("config/")
configs = python_modules.load_configs(configs_path)

### SELECT TEMPLATES ###
templates = [
    "index",
    "impressum",
    ]

### SET OUTPUT DIRECTORY ###
output_dir = Path('html/')

### RENDER HTML ###
render.render_html(output_dir, configs, templates)