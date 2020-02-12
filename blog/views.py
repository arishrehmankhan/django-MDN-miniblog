from django.shortcuts import render
from .models import Blog, Author, Comment
from django.http import HttpResponse
from django.views import generic

# Create your views here.
def index(request):
    num_blogs = Blog.objects.all().count()
    num_bloggers = Author.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits +1

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 2

class BlogDetailView(generic.DetailView):
    model = Blog