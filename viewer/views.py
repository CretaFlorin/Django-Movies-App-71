from django.http import HttpResponse
from django.shortcuts import render
from viewer.models import Movie, Genre
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, UpdateView, CreateView, DeleteView
from viewer.forms.movie import MovieForm
from django.urls import reverse_lazy

# View-urile sunt de 2 tipuri: Functional si Class-Based


# --------- Functional View ---------
def main_page(request):
    movies = Movie.objects.all()
    return render(request, template_name="main_page.html", context={"movies": movies})


# --------- Class-Based Views ---------
# View - mostenim cea mai generica clasa de View
class MainPageView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(
            request, template_name="main_page.html", context={"movies": movies}
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

# 3.FormView      - O clasa de View pe care o folosim pentru
#                  a lucra mai usor cu Form-uri
# class MovieCreateFormView(FormView):
#     template_name = "movie_create.html"
#     form_class = MovieForm
#     success_url = reverse_lazy('movies')

#     def form_valid(self, form):
#         result = super().form_valid(form)
       
#         # Salvam filmul in DB    
#         data = form.cleaned_data
#         new_movie = Movie(
#             title=data["title"],
#             genre=data["genre"],
#             rating=data["rating"],
#             released=data["released"],
#             description=data["description"],
#         )
#         new_movie.save()
#         return result

# Create cu CreateView
class MovieCreateFormView(CreateView):
    template_name = "movie_create.html"
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    
# Update cu FormView
# class MovieUpdateFormView(FormView):
#     template_name = "movie_create.html"
#     form_class = MovieForm
#     success_url = reverse_lazy('movies')

#     def form_valid(self, form):
#         result = super().form_valid(form)
       
#         # Updatam filmul in DB    
#         pk = self.kwargs['pk']
        
#         data = form.cleaned_data
#         try:
#             movie = Movie.objects.get(pk=pk) 
        
#             movie.title=data["title"]
#             movie.genre=data["genre"]
#             movie.rating=data["rating"]
#             movie.released=data["released"]
#             movie.description=data["description"]
#             movie.save()
        
#             return result
#         except:
#             return HttpResponse(f"There is no movie with id={pk}")
        
# Update cu UpdateView
class MovieUpdateFormView(UpdateView):
    template_name = "movie_create.html"
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movies')


# Delete cu FormView
class MovieDeleteFormView(DeleteView):
    template_name = "movie_confirm_delete.html"
    model = Movie
    success_url = reverse_lazy('movies')