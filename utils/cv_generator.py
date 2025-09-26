from fpdf import FPDF
from jinja2 import Template

def render_cv_html(employee, logo_path):
    with open("templates/cv_template.html") as f:
        template = Template(f.read())
    return template.render(employee=employee, logo_path=logo_path)

def generate_cv_pdf(employee, logo_path):
    from xhtml2pdf import pisa
    html = render_cv_html(employee, logo_path)
    with open("data/cv_output.pdf", "wb") as result_file:
        pisa.CreatePDF(html, dest=result_file)
