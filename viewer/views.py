from django.http import HttpResponse
from django.shortcuts import render
from viewer.models import Movie, Genre
from django.views import View
from django.views.generic import TemplateView, ListView

# View-urile sunt de 2 tipuri: Functional si Class-Based

# --------- Functional View ---------
def main_page(request):
    movies = Movie.objects.all()
    return render(
        request,
        template_name="main_page.html",
        context={
            "movies": movies
        }
    )

# --------- Class-Based Views ---------
# View - mostenim cea mai generica clasa de View
class MainPageView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(
            request,
            template_name="main_page.html",
            context={
                "movies": movies
            }
        )
        
# 1.TemplateView - O clasa de View pe care o folosim pentru
#                  a lucra mai usor cu Template-uri
class MainPageTemplateView(TemplateView):
    template_name = "main_page.html"
    extra_context = {"movies": Movie.objects.all()}

# 2.ListView      - O clasa de View pe care o folosim pentru
#                  a lucra mai usor cu Liste
class MainPageListView(ListView):
    template_name = "main_page.html"
    model = Movie