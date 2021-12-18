from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Post
from django.db.models import Q
from .forms import MakePostForm, CommentForm

# Create your views here.


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        'posts': paged_products,
    }
    return render(request, 'index.html', context)


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            posts = Post.objects.order_by('-date_created').filter(Q(body__icontains=keyword) | Q(title__icontains=keyword) | Q(subtitle__icontains=keyword) | Q(author__icontains=keyword))
            post_count = posts.count()
    context = {
        'posts': posts,
        'post_count': post_count,
    }
    return render(request, 'search.html', context)


def make_post(request):
    form = MakePostForm
    return render(request, 'index', {'form': form})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')




