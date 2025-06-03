from django.http import HttpResponse
from django.shortcuts import render
from viewer.models import Movie, Genre
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    FormView,
    UpdateView,
    CreateView,
    DeleteView,
)
from viewer.forms.movie import MovieForm
from viewer.forms.user import UserForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


# View-urile sunt de 2 tipuri: Functional si Class-Based
# --------- Functional View ---------
@login_required
def main_page(request):
    movies = Movie.objects.all()
    return render(request, template_name="main_page.html", context={"movies": movies})


# --------- Class-Based Views ---------
# View - mostenim cea mai generica clasa de View
class MainPageView(LoginRequiredMixin, View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(
            request, template_name="main_page.html", context={"movies": movies}
        )


# 1.TemplateView - O clasa de View pe care o folosim pentru
#                  a lucra mai usor cu Template-uri
class MainPageTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "main_page.html"
    extra_context = {"movies": Movie.objects.all()}


# 2.ListView      - O clasa de View pe care o folosim pentru
#                  a lucra mai usor cu Liste
# class MainPageListView(ListView):
#     template_name = "main_page.html"
#     model = Movie


# http://localhost:8000/movies/?search=aaa
#  Varianta Lista Filme Fara ListView (pentru functionalitatea de SEARCH)
class MainPageListView(LoginRequiredMixin, View):
    def get(self, request):
        search_value = self.request.GET.get("search")

        movies = Movie.objects.all()
        filtered_movies = []

        if search_value:
            filtered_movies = Movie.objects.filter(title__icontains=search_value)
        else:
            filtered_movies = movies

        return render(
            request,
            template_name="main_page.html",
            context={
                "object_list": filtered_movies,
                "search_value": search_value or "",
            },
        )


# 3.FormView      - O clasa de View pe care o folosim pentru
#                  a lucra mai usor cu Form-uri
# class MovieCreateFormView(FormView):
#     template_name = "movie_form.html"
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
class MovieCreateFormView(LoginRequiredMixin, CreateView):
    template_name = "movie_form.html"
    form_class = MovieForm
    success_url = reverse_lazy("movies")
    
class RegisterView(CreateView):
    template_name = "user_form.html"
    form_class = UserForm
    success_url = reverse_lazy("login")


# Update cu FormView
# class MovieUpdateFormView(FormView):
#     template_name = "movie_form.html"
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
class MovieUpdateFormView(LoginRequiredMixin, UpdateView):
    template_name = "movie_form.html"
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("movies")


# Delete cu FormView
class MovieDeleteFormView(LoginRequiredMixin, DeleteView):
    template_name = "movie_confirm_delete.html"
    model = Movie
    success_url = reverse_lazy("movies")


# Custom View for Login
class CustomLoginView(LoginView):
    template_name = 'login.html'