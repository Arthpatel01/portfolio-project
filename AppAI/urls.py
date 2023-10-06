from django.urls import path

from AppAI import views

urlpatterns = [
    path('generate_image', views.GenerateImageView.as_view(), name="generate_image")
]
