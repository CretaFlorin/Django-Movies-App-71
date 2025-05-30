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

from viewer.views import main_page, MainPageView, MainPageTemplateView, MainPageListView, MovieCreateFormView,MovieUpdateFormView, MovieDeleteFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', main_page),
    # path('', MainPageView.as_view()),
    # path('', MainPageTemplateView.as_view(), name='main_page'),
    path('', MainPageListView.as_view(), name='main_page'),
    path('movies/', MainPageListView.as_view(), name='movies'),
    path('movies/create/', MovieCreateFormView.as_view(), name='movie_create'),
    path('movies/update/<pk>', MovieUpdateFormView.as_view(), name='movie_update'),
    path('movies/delete/<pk>', MovieDeleteFormView.as_view(), name='movie_delete'),
]