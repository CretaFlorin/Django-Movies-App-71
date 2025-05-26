from django.http import HttpResponse
from django.shortcuts import render
from viewer.models import Movie

def main_page(request):
    movies=Movie.objects.all()
    return render(
        request,
        template_name="main_page.html",
        context={
            "movies":movies
        }
    )
