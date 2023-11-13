from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='shopHome'),
    path("about/",views.about,name='AboutUs'),
    path("contact/",views.contact,name='contactUs'),
    path("tracker/",views.tracker,name='trackingStatus'),
    path("search/",views.search,name='search'),
    path("productview/",views.productView,name='prodView'),
    path("checkout/",views.checkout,name='checkout'),
    path("tracker/",views.tracker,name='tracker'),
    path("moreinfo/",views.moreinfo,name='moreinfo'),
    path("payment/",views.payment,name='payment'),
    path("products/<int:myid>", views.productView, name="ProductView"),

]  
