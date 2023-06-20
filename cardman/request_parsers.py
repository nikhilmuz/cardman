from rest_framework.parsers import BaseParser


class PlainTextParser(BaseParser):
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read().decode(parser_context.get('encoding', 'utf-8'))
