PATH = "templates/nda.md"
from src.utils import TextDocumentGenerator
from IPython.display import display, Markdown, Latex
import markdown
from weasyprint import HTML

generator = TextDocumentGenerator(PATH)


def generate_pdf(text):
    html = markdown.markdown(text)
    HTML(string=html).write_pdf("nda.pdf")


data = {
    "day": "15th",
    "month": "October",
    "year": "2024",
    "role": "Intern",
    "company_name": "ArkVerse Private Limited",
    "survival_period": 5,
    "post_binding_agreement_period": 2,
    "governing_laws": "India",
    "jurisdiction_city": "Bangalore",
    "arbitration_act": "Indian Arbitration & Conciliation Act, 1996",
    "arbitration_city": "Bangalore",
    "arbitration_language": "English",
    "authorized_signatory_name": "Ganesh Prasad Rao",
    "authorized_signatory_date": "08/05/2023",
    "employee_name": "",
    "employee_date": "",
}


output = generator.template.render(data)
generate_pdf(output)
Markdown(output)
