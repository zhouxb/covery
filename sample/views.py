from coffin.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def index(request):
    return render_to_response('sample/index.html', {'Hello':'Word'}, context_instance=RequestContext(request))

