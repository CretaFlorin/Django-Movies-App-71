"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from viewer.views import (
    main_page,
    MainPageView,
    MainPageTemplateView,
    MainPageListView,
    MovieCreateFormView,
    MovieUpdateFormView,
    MovieDeleteFormView,
    CustomLoginView,
    RegisterView
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', main_page),
    path("accounts/login/", CustomLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("register/", RegisterView.as_view(), name='register'),
    path("movies/", MainPageListView.as_view(), name="movies"),
    path("movies/create/", MovieCreateFormView.as_view(), name="movie_create"),
    path("movies/update/<pk>", MovieUpdateFormView.as_view(), name="movie_update"),
    path("movies/delete/<pk>", MovieDeleteFormView.as_view(), name="movie_delete"),
]


"""

[1,4,6,8,9,12,23,45,56,67]

d = {
 1-> 1: True,
 2-> 4: True,
 3-> 6: True,
 4-> 8: True,
    ...
 8-> 56: True,
 9-> 67: True, 700:True, 344:True, 345:True, 98:True
}


hash(67) -> 9
hash(8) -> 4
hash(700) -> 9
"""
