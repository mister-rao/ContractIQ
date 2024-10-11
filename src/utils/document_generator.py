from jinja2 import Template
from IPython.display import display, Markdown, Latex
from weasyprint import HTML
import markdown


class TextDocumentGenerator:
    _template: Template

    def __init__(self, template_path):
        with open(template_path, "r", encoding="utf-8") as file:
            self._content = file.read()

        # Create a Jinja2 template object

        self._template = Template(self._content)

    def update(self, data):
        # replace placeholders with corresponding values in the content
        return self._template.render(data)

    @staticmethod
    def generate_pdf(text: str):
        html = markdown.markdown(text)
        HTML(string=html).write_pdf("nda.pdf")
