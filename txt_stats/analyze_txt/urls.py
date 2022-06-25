from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-text/", views.TextInputViews.as_view()),
    path("texts/<int:id>", views.TextInputViews.as_view()),
]
