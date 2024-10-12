from jinja2 import Template
from weasyprint import HTML
import markdown


class TextDocumentGenerator:
    _template: Template
    content: str

    def __init__(self, template_path):
        with open(template_path, "r", encoding="utf-8") as file:
            self._content = file.read()

        # Create a Jinja2 template object
        self._template = Template(self._content)

    def update(self, data):
        # replace placeholders with corresponding values in the content
        self.content = self._template.render(data)

    def generate_pdf(self, filename):
        html = markdown.markdown(self.content)
        HTML(string=html).write_pdf(f"{filename}.pdf")
