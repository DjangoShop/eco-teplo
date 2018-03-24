from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^basket.html', views.basket, name='basket'),

    url(r'^remove/(?P<product_id>\d+)/$', views.BasketRemove, name='BasketRemove'),
    url(r'^add/(?P<product_id>\d+)/$', views.BasketAdd, name='BasketAdd'),
    url(r'^$', views.BasketDetail, name='BasketDetail'),

]