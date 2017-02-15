from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request):
    html = "<!DOCTYPE html><html><head></head><body>Hello Django</body></html>"
    return HttpResponse(html)
