import os
import gzip

from jinja2 import Environment, PackageLoader, select_autoescape

TEMPLATE_ENVIRONMENT = Environment(
    loader=PackageLoader('sitemap_builder', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    extensions=['jinja2.ext.do'])

def generate_file_compressed(self, filename, template_filename, context):
    fullpath = os.path.join(self.output_dir, filename)
    with gzip.open(fullpath, 'wb') as f:
        content = self._render_template(template_filename, context)
        #string object into bytes object
        f.write(content.encode())

def generate_file(filename, template_filename, context, output_dir):
    with open(os.path.join(output_dir, filename), 'w') as f:
        html = render_template(template_filename, context)
        f.write(html)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
