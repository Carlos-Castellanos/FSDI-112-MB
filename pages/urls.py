from django.urls import path
from .views import (
    TemplateIndexView, 
    TemplateAboutView,
)

urlpatterns = [
    path('',TemplateIndexView.as_view(), name="home"),
    path('about/',TemplateAboutView.as_view(), name="about"),
]
