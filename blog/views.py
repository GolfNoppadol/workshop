from django.shortcuts import render_to_response
from blog.models import BlogPost

# Create your views here.


def homepage(request):
    blog_list = BlogPost.objects.all()
    data = {
        'title': 'This is title',
        'data1': 'Hooooorey!',
        'blog_list': blog_list,
    }
    return render_to_response('index.html', data)
