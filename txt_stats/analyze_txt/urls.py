from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'db', views.TextInputViews, basename='text')

urlpatterns = [
    path("", views.home, name="home"),
    # path("add-text/", views.TextInputViews.as_view()),
    # path("texts/<int:id>", views.TextInputViews.as_view()),
]

urlpatterns += router.urls
