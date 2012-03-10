from django.http import HttpResponse
from django.template import RequestContext
from coffin import shortcuts

from anyjson import serialize

def render_to_string(template, context, request=None):
    if request:
        context_instance = RequestContext(request)
    else:
        context_instance = None

    return shortcuts.render_to_string(template, context, context_instance)

def render(request, template, context={}, mimetype='text/html'):
    response = render_to_string(template, context, request)

    return HttpResponse(response, mimetype=mimetype)

def json_response(response):
    return HttpResponse(serialize(response), mimetype='application/json')

