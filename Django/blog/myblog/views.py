from django.shortcuts import render
from .models import Articles

def show_home(request):
    posts = Articles.objects.all()
    context = { 'posts': posts}
    return render(request, 'home.html', context)
