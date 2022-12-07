from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

class AboutView(TemplateView):
    template_name = 'about.html'