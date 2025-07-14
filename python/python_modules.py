import yaml
from pathlib import Path
from .jinja_extensions import get_jinja_environment

def import_config(file: Path):
    """
    Load a YAML configuration file.
    Args:
        file (Path): Path to the YAML config file.
    Returns:
        dict: The loaded configuration as a dictionary.
    """
    with open(file, "r", encoding='utf-8') as f:
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

def deep_merge(base, update):
    """Merges dictionaries recursively, preserving unmentioned keys"""
    for key, value in update.items():
        if isinstance(value, dict) and key in base and isinstance(base[key], dict):
            base[key] = deep_merge(base[key], value)
        else:
            base[key] = value
    return base

def render_html(
    output_dir: Path,
    configs_path: Path,
    templates: list[str] | None = None,
    template_dir: str | Path = "templates",
) -> list[Path]:
    """Render Jinja2 templates with custom functions."""
    if not output_dir.exists():
        raise FileNotFoundError(f"Output directory {output_dir} does not exist")
    
    if not templates:
        print("Warning: No templates to render!")
        return []
    
    configs = load_configs(configs_path)

    env = get_jinja_environment(template_dir)
    rendered_files = []
    
    print("Rendering templates:")
    for template in templates:
        try:
            print(f"  - {template}", flush=True)
            
            context = deep_merge(configs["global"], configs.get(template, {}))
            html = env.get_template(f"{template}.html.j2").render(**context)

            output_path = output_dir / f"{template}.html"
            output_path.write_text(html, encoding="utf-8")
            rendered_files.append(output_path)
        except Exception as e:
            print(f"Error rendering {template}: {str(e)}")
            raise

    print(f"Build complete! Rendered {len(rendered_files)} files.")
    return rendered_files