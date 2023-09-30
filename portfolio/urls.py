from django.urls import path
from django.views.generic import TemplateView

from portfolio import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('resume1', TemplateView.as_view(template_name='portfolio.html')),
]
