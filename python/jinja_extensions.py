from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from datetime import datetime
import json

### FILTERS ###
def tojson_filter(data: str, *, indent: int=2):
    return json.dumps(data, indent=indent)

def background_style(background_img: dict):
    """Generates CSS for background images"""
    if not background_img:
        return ""
    
    # possible extensions
    """
    if background_img.get('type') == 'video':
        return generate_video_bg(background_img)
    elif background_img.get('gradient'):
        return generate_gradient(background_img)
    """
    
    file_path = f"{background_img['dir']}/{background_img['file']}"
    return (
        f"background: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), "
        f"url('{file_path}') center/cover fixed;"
        "min-height: 100vh;"
    )

### FUNCTIONS ###
def static_url(dir: str, file: str) -> str:
    """Resolves static file paths (replacement for Flask's url_for)."""
    return f"{dir}/{file}" if dir else file

def current_year() -> int:
    """Returns the current year (for copyright footers)."""
    return datetime.now().year


### ENVIRONMENT ###
def get_jinja_environment(template_dir: str | Path) -> Environment:
    """Create a Jinja2 Environment with custom globals/filters."""
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # Add custom functions to all templates
    env.globals.update({
        "static_url": static_url,
        "current_year": current_year,
    })

    # Add custom filters
    env.filters['tojson'] = tojson_filter
    env.filters['background_style'] = background_style
    
    return env