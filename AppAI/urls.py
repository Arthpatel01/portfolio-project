from django.urls import path

from AppAI import views

urlpatterns = [
    path('generate_image', views.generate_image, name="generate_image")
]
