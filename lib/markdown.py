import re

import frontmatter                      # pip install python-frontmatter
from mistune import Renderer, Markdown  # pip install mistune


class StripMarkdownRenderer(Renderer):
    def _handle_html(self, html):
        flags = re.MULTILINE | re.DOTALL
        if re.search(r'<blockquote.*>.*</blockquote>', html, flags):
            return 'BLOCKQUOTE'
        if re.search(r'<iframe.*>.*</iframe>', html, flags):
            return 'EMBEDED'
        else:
            return ''

    def block_code(self, code, lang=None):
        return '\nBLOCK_CODE\n\n'

    def block_quote(self, text):
        return text

    def block_html(self, html):
        return self._handle_html(html)

    def header(self, text, level, raw=None):
        return text

    def hrule(self):
        return '\n'

    def list(self, body, ordered=True):
        return body

    def list_item(self, text):
        return text

    def paragraph(self, text):
        return text + '\n'

    def table(self, header, body):
        return body

    def table_row(self, content):
        return content

    def table_cell(self, content, **flags):
        return content

    def double_emphasis(self, text):
        return text

    def emphasis(self, text):
        return text

    def codespan(self, text):
        return 'CODE'

    def linebreak(self):
        return '\n'

    def strikethrough(self, text):
        return text

    def autolink(self, link, is_email=False):
        return 'LINK'

    def link(self, link, title, text):
        return text

    def image(self, src, title, text):
        return 'IMAGE'

    def inline_html(self, html):
        return self._handle_html(html)

    def footnote_ref(self, key, index):
        return ''

    def footnote_item(self, key, text):
        return text

    def footnotes(self, text):
        return text
