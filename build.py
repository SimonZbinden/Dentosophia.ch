from pathlib import Path

from python.python_modules import render_html

### LOAD CONFIG ###
configs_path = Path("config/")

### SELECT TEMPLATES ###
templates = [
    "index",
    "impressum",
    "dsb",
    "about",
    "kontakt",
    "kosten",
    "dentosophie",
    'material',
    "cranio",
    #"empty_body",
    #"test",
    "bulma",
    ]

### SET OUTPUT DIRECTORY ###
output_dir = Path('html/')

### RENDER HTML ###
render_html(output_dir, configs_path, templates)


### START VENV in powershell ###
# & .venv/Scripts/Activate.ps1