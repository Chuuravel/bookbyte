from django.urls import path
from book import views

app_name = "book"
urlpatterns = [
    path("", views.best_seller, name="best_seller"),
    path("bestseller/", views.best_seller, name="best_seller"),
    path("recmdbook/", views.recommended_book, name="recommended_book"),
    path("showall/", views.show_all_book, name = "show_all_book"),
]