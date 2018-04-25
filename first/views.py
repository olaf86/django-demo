from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    all_post = Post.objects.filter(published_date__lte=timezone.now())\
                        .order_by('-published_date')
    paginator = Paginator(all_post, 3)

    page = request.GET.get('p')
    posts = paginator.get_page(page)
    return render(request, 'first/post_list.html', {'posts': posts})