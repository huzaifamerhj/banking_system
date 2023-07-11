from django.views.generic import TemplateView
from django.shortcuts import render



class HomeView(TemplateView):
    template_name = 'core/index.html'

def aboutus(request):
    return render(request, 'core/about_us.html')