from django.shortcuts import render


def home_view(request):
    return render(request, "portfolio/home.html")


def about_view(request):
    return render(request, "portfolio/about.html")


def projects_view(request):
    return render(request, "portfolio/projects.html")


def skills_view(request):
    return render(request, "portfolio/skills.html")


def journey_view(request):
    return render(request, "portfolio/journey.html")


def contacts_view(request):
    return render(request, "portfolio/contacts.html")
