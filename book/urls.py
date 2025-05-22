from django.urls import path
from book import views

app_name = "book"
urlpatterns = [
    path("", views.best_seller, name="best_seller"),
    path("bestseller/", views.best_seller, name="best_seller"),
]