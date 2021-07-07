from django.urls import path

from translate import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
]