from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
    return render(
        request,
        template_name="main_page.html",
    )