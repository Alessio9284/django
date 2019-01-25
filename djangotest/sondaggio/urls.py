from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:domanda_id>/', views.dettagli, name = 'detail'),
    path('<int:domanda_id>/risultati/', views.risultati, name = 'results'),
    path('<int:domanda_id>/voto/', views.voto, name = 'vote'),
]