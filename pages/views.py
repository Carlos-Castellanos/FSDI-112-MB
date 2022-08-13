from django.shortcuts import render

# from django.shortcuts import render
from django.views.generic import TemplateView


class TemplateIndexView(TemplateView):
    template_name = "index.html"    

class TemplateAboutView(TemplateView):
    template_name = "about.html"  
