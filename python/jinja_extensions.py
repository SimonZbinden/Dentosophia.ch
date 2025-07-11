from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from datetime import datetime

def static_url(dir: str, filename: str) -> str:
    """Resolves static file paths (replacement for Flask's url_for)."""
    return f"{dir}/{filename}"

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
    
    return env