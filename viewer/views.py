from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    # return HttpResponse("Hello!!!")
    return render(
        request,
        template_name="hello.html",
    )