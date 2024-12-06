from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
     path("welcome", views.welcome_view),
     path("persons", views.person_list),
     path("person/<int:id>", views.person_detail),
     path("teams",views.team_list)
]