from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'db', views.TextInputViews, basename='text')

urlpatterns = [
    path("", views.home, name="home"),
    path("view/<int:id>/", views.analyzed, name="view"),
    path("view/", views.list_analyzed, name="list")
]

urlpatterns += router.urls
