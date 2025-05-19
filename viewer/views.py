from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello!!!")

def salutare(request):
    return HttpResponse("Salutare!!!")

# Regular expressions
# def custom(request, genre):
#     return HttpResponse(genre)

# URL Encoding
def custom(request):
    genre = request.GET.get('genre')
    return HttpResponse(genre)