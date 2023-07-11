from django.views.generic import TemplateView
from django.shortcuts import render

from . import views

def aboutus(request):
    return render(request,'core/about_us.html')
    





class HomeView(TemplateView):
    template_name = 'core/index.html'

