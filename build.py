from pathlib import Path

from python.python_modules import render_html

### LOAD CONFIG ###
configs_path = Path("config/")

### SELECT TEMPLATES ###
templates = [
    "index",
    #"impressum",
    #"dsb",
    "about",
    "kontakt",
    #"philosophie",
    #"dentosophie",
    #"cranio",
    "empty_body",
    "test",
    ]

### SET OUTPUT DIRECTORY ###
output_dir = Path('html/')

### RENDER HTML ###
render_html(output_dir, configs_path, templates)