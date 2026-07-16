from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

TEMPLATES_DIR = Path(__file__).parent / "templates"
_env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=True)


def render_cv_pdf(cv_data: dict) -> bytes:
    template = _env.get_template("cv_pdf_template.html")
    html_content = template.render(**cv_data)
    return HTML(string=html_content, base_url=str(TEMPLATES_DIR)).write_pdf()
