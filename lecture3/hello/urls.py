from django.urls import path

from . import views

urlpatterns = [
   path("", views.index, name="index"), 
   path("jan", views.jan, name="jan"),
   path("strager", views.strager, name="strager"),
   path("<str:name>", views.greet, name="greet"),

        ]
