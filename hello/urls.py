from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="hello"),
    path("<str:name>", views.greet),
]
