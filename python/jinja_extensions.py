from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from datetime import datetime
import json

def tojson_filter(data: str, *, indent: int=2):
    return json.dumps(data, indent=indent)

def static_url(dir: str, file: str) -> str:
    """Resolves static file paths (replacement for Flask's url_for)."""
    return f"{dir}/{file}"

def current_year() -> int:
    """Returns the current year (for copyright footers)."""
    return datetime.now().year

def get_jinja_environment(template_dir: str | Path) -> Environment:
    """Create a Jinja2 Environment with custom globals/filters."""
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # Add custom functions to all templates
    env.globals.update({
        "static_url": static_url,  # Usage: {{ static_url('figure1.svg') }}
        "current_year": current_year,
    })

    # Add custom filters
    env.filters['tojson'] = tojson_filter
    
    return env