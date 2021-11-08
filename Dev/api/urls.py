from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, ),
    path('getAllStates/', views.get_all_states, )
]