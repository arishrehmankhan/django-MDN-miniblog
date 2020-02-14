import datetime

from django.shortcuts import render
from .models import Blog, Author, Comment
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.all().order_by('-pub_date_time')

class BlogDetailView(generic.DetailView):
    model = Blog
    
class BloggerListView(generic.ListView):
    model = Author
    paginate_by = 5

class BloggerDetailView(generic.DetailView):
    model = Author

@login_required
def commentCreate(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment()
            comment.text = form.cleaned_data['comment_text']
            comment.pub_date_time = datetime.datetime.now()
            comment.author = request.user
            comment.blog = Blog.objects.get(id=pk)
            comment.save()

            return HttpResponseRedirect(reverse('blog-detail', args=[pk]))
    
    else :
        form = CommentForm()

    blog = Blog.objects.get(id=pk)
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, 'blog/comment_form.html', context)
