from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "this_is_true": True,
        "my_number": 888,
        "my_list": [8, 168, 211, 323, 100]
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})
