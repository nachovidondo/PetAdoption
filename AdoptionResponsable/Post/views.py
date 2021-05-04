from django.shortcuts import render
from .models import Post


def post_comments_create_and_list_view(request):
    qs = Post.objects.all()
    
    context = {
        'qs':qs,
        
    }
    return render(request,'Post/main.html', context)
