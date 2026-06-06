from django.shortcuts import render


def home(request):
    lessons = [
        "manage.py runs Django commands.",
        "config/settings.py controls installed apps, templates, static files, and database.",
        "config/urls.py sends browser URLs to app URL files.",
        "pages/views.py chooses which template to render.",
        "templates/ holds HTML files.",
        "static/ holds CSS, images, and JavaScript.",
    ]
    return render(request, "pages/home.html", {"lessons": lessons})


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")
