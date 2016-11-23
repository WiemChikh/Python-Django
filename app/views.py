from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.http import HttpResponse

from .models import Post

def index(request):
    return render(request, 'app/index.html') #liaison entre index et view pour afficher e contenu de index ds le navigateur
def contact(request):
    return render(request, 'app/contact.html')
class PostList(ListView):
    model = Post
#create our views here
class PostDetail(DetailView):
    model = Post