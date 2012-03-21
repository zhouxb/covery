from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

def index(request):
    return render_to_response('sample/index.html', {'Hello':'Word'}, context_instance=RequestContext(request))

def demo(request, template_name='sample/demo.html'):

    return render(request, template_name)

def demo1(request, template_name='sample/demo1.html'):

    return render(request, template_name)

