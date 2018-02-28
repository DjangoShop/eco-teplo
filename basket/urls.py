from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^basket.html', views.basket, name='basket'),
]