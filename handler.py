from hug import get, directive
from hug.types import comma_separated_list, text
import json

@directive()
def who_header(request, **kwargs):
    return request.headers.get('X-WHO', None)

@get('/hello')
def hello(hug_who_header, who = None):
    who = who or hug_who_header or 'World'
    who = ', '.join(who) if isinstance(who, list) else who
    return 'Hello %s' % who
