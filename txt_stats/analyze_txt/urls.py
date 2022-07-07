from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

router = DefaultRouter()
router.register(r'api', views.TextInputViews, basename='api')

urlpatterns = [
    path("", views.create, name="create"),
    path("create/", views.create, name="create"),
    path("view/<int:id>/", views.analyzed, name="view"),
    path("view/", views.list_analyzed, name="list"),
    path("account/", views.account, name="account"),
    path("account/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

urlpatterns += router.urls
