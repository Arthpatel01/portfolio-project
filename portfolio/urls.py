from django.urls import path
from django.views.generic import TemplateView

from portfolio import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='portfolio.html')),
    path('2', views.IndexView.as_view(), name="index2")
]
