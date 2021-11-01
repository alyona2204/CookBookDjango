from .views import home, detail
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("<int:pk>/", detail, name="detail"),
]