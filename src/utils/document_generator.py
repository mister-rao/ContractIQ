from jinja2 import Template


class TextDocumentGenerator:
    template: Template

    def __init__(self, template_path):
        with open(template_path, "r", encoding="utf-8") as file:
            self.content = file.read()

        # Create a Jinja2 template object

        self.template = Template(self.content)

    def update(self, data):
        # replace placeholders with corresponding values in the content
        for key, value in data.items():
            self.content = self.content.replace(key, value)
