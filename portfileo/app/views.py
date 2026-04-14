from django.shortcuts import render


PROJECTS = [
    {
        "title": "concept crafter",
        "description": "A web application built with React",
        "tags": ["Django", "Python", "PostgreSQL"],
        "link": "https://github.com/Manjunath-L/final-year-project",
    },
]

SKILLS = [
    "Python",
    "Django",
    "JavaScript",
    "HTML & CSS",
    "PostgreSQL",
]


def home(request):
    return render(
        request,
        "home.html",
        {
            "projects": PROJECTS[:2],
            "skills": SKILLS,
        },
    )


def about(request):
    return render(
        request,
        "about.html",
        {
            "skills": SKILLS,
        },
    )


def projects(request):
    return render(
        request,
        "projects.html",
        {
            "projects": PROJECTS,
        },
    )


def contact(request):
    return render(request, "contact.html")
