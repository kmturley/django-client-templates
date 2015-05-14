from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'people': [
            {"name": "John Doe"},
            {"name": "Sally Taylor"},
            {"name": "David Smith"}
        ],
    })
    return HttpResponse(template.render(context))