from django.urls import path
from . import views
urlpatterns = [
    path("",views.all_api,name="all-api"),
    path("restaurants/",views.restaurants_api,name="restaurants-api"),
    path("restaurants/<str:pk>/",views.restaurant_api,name="restaurant-api"),
    path("dishes",views.dish_api,name="dishes-api"),
    path("dishes/<str:pk>/",views.dish_api,name="dishes-api"),

]
