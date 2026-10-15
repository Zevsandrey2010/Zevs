from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("projects/", views.projects_view, name="projects"),
    path("skills/", views.skills_view, name="skills"),
    path("journey/", views.journey_view, name="journey"),
    path("contacts/", views.contacts_view, name="contacts"),
]
