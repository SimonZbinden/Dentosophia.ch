from pathlib import Path

from python import render, python_modules

### LOAD CONFIG ###
config_path = Path("config.yaml")
config = python_modules.import_config(config_path)

### SELECT TEMPLATES ###
templates = ["index"]
# prepare templates
templates = [template + ".html.j2" for template in templates]

### SET OUTPUT DIRECTORY ###
output_dir = Path('html/')

### RENDER HTML ###
render.render_html(output_dir, config, templates)