from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello!!!")

def salutare(request):
    return HttpResponse("Salutare!!!")