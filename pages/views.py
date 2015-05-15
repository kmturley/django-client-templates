from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader


def index(request):
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
    
    
def angular(request):
    content_type = request.META.get('HTTP_ACCEPT').split(',')[0]
    if content_type == 'application/json':
        data = {
            "items": [
                {"name": "Dynamic data 1", "desc": "Dynamic Lorem ipsum dolor sit amet, consectetur adipiscing elit. 1" },
                {"name": "Dynamic data 2", "desc": "Dynamic Lorem ipsum dolor sit amet, consectetur adipiscing elit. 2" },
                {"name": "Dynamic data 3", "desc": "Dynamic Lorem ipsum dolor sit amet, consectetur adipiscing elit. 3"}
            ]
        }
        return JsonResponse(data)
    else:
        template = loader.get_template('angular/index.html')
        context = RequestContext(request, {
            'items': [
                {"name": "Static data 1", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. 1"},
                {"name": "Static data 2", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. 2"},
                {"name": "Static data 3", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. 3"}
            ],
        })
        return HttpResponse(template.render(context))

    
def plate(request):
    content_type = request.META.get('HTTP_ACCEPT').split(',')[0]
    if content_type == 'application/json':
        data = {
            "items": [
                {"name": "Dynamic data 1", "desc": "Dynamic Lorem ipsum dolor sit amet, consectetur adipiscing elit. 1" },
                {"name": "Dynamic data 2", "desc": "Dynamic Lorem ipsum dolor sit amet, consectetur adipiscing elit. 2" },
                {"name": "Dynamic data 3", "desc": "Dynamic Lorem ipsum dolor sit amet, consectetur adipiscing elit. 3"}
            ]
        }
        return JsonResponse(data)
    else:
        template = loader.get_template('plate/index.html')
        context = RequestContext(request, {
            'items': [
                {"name": "Static data 1", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. 1"},
                {"name": "Static data 2", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. 2"},
                {"name": "Static data 3", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. 3"}
            ],
        })
        return HttpResponse(template.render(context))