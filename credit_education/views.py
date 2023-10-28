from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello!! Capital One, Credit Education!")
