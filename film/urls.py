from django.urls import path
from film import views

urlpatterns = [
    path('', views.FilmList.as_view()),
]
