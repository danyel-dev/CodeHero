from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q, Count, Case, When
from django.core.paginator import Paginator
from django.contrib import messages
from django.db import connection

from .models import Post
from .models import Comentario

from .forms import ComentarioForm


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
    
    posts = posts.select_related('categoria')

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

    posts = posts.select_related('categoria')
    
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
    comments = comments.select_related('user')

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        
        if form.is_valid():
            form = form.save(commit=False)
            form.post = post
            form.user = request.user
            form.publicado = True
            form.save()
            
            form = ComentarioForm()

            return render(request, 'posts/post_detail.html', {'post': post, 'comments': 
            comments, 'form': form})
    
    form = ComentarioForm()

    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def delete_comment(request, id_comment):
    comment = get_object_or_404(Comentario, pk=id_comment)
    comment.delete()
    messages.success(request, 'Seu comentário foi deletado com sucesso')
    return redirect('post-detail', comment.post.id)
