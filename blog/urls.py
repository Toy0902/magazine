from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('404/', h404, name="404"),
    path('about/', about,name="about"),
    path('cart/', cart,name="cart"),
    path('checkout/', checkout,name="checkout"),
    path('contact/', contact,name="contact"),
    path('index_2/', index_2,name="index_2"),
    path('news/', news,name="news"),
    path('shop/', shop,name="shop"),
    path('single_news/', single_news,name="single_news"),
    path('single_product/', single_product,name="single_product"),
    ]
