from django.urls import path
import siteapp.views as views
urlpatterns = [
    path("", views.reviews, name = "reviews"),
]