from pathlib import Path

from .jinja_extensions import get_jinja_environment

def render_html(
    output_dir: Path,
    configs: dict,
    templates: list[str] | None = None,
    template_dir: str | Path = "templates",
) -> list[Path]:
    """Render Jinja2 templates with custom functions."""
    if not output_dir.exists():
        raise FileNotFoundError(f"Output directory {output_dir} does not exist")
    
    if not templates:
        print("Warning: No templates to render!")
        return []

    env = get_jinja_environment(template_dir)
    rendered_files = []
    
    print("Rendering templates:")
    for template in templates:
        try:
            print(f"  - {template}", flush=True)
            
            context = {**configs["global"], **configs.get(template, {})}
            html = env.get_template(f"{template}.html.j2").render(**context)

            output_path = output_dir / f"{template}.html"
            output_path.write_text(html, encoding="utf-8")
            rendered_files.append(output_path)
        except Exception as e:
            print(f"Error rendering {template}: {str(e)}")
            raise

    print(f"Build complete! Rendered {len(rendered_files)} files.")
    return rendered_files