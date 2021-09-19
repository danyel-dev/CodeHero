from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q, Count, Case, When
from django.core.paginator import Paginator
from django.contrib import messages

from .models import Post
from .models import Comentario


def home(request):
    sort = request.GET.get('sort')
    order = 'id' if sort == 'olds' else '-id'

    posts = Post.objects.order_by(order).annotate(
        number_comments = Count(
            Case(
                When(comentario__publicado = True, then = 1)
            )
        )
    ).filter(publicado = True)
    
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'posts/home.html', {'posts': posts})    


def home_search(request):
    search =  request.GET.get('search')

    if not search or search is None:
        return redirect('/')
    
    sort = request.GET.get('sort')
    order = 'id' if sort == 'olds' else '-id'

    posts = Post.objects.order_by(order).annotate(
        number_comments = Count(
            Case(
                When(comentario__publicado = True, then = 1)
            )
        )
    ).filter(
        Q(titulo__icontains = search) | 
        Q(categoria__nome_categoria__iexact = search),
        publicado = True
    )
    
    number_posts = posts.count()
    
    if number_posts:
        messages.error(request, f'{number_posts} post(s) encontrado(s) para: "{search}"')

    paginacao = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginacao.get_page(page)

    return render(request, 'posts/home.html', {'posts': posts})    


def post_detail(request, id_post):
    post = get_object_or_404(Post, id = id_post)
    comments = Comentario.objects.order_by('-id').filter(post = id_post, publicado = True)

    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})
