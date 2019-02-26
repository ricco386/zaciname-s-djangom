from django.urls import path
from mailinglist import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:list_id>/', views.mlist, name='mlist'),
    path('<int:list_id>/subscribe/', views.subscribe,
                                      name='subscribe'),
]