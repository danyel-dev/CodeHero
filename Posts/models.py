from django.db import models

from django.contrib.auth.models import User


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50, verbose_name='Categoria')


    def __str__(self):
        return self.nome_categoria


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')

    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, verbose_name='Categoria', blank=True, null=True)

    titulo = models.CharField(max_length=100, verbose_name='Título do Post')
    
    conteudo = models.TextField(verbose_name='Conteúdo') 
    
    imagem = models.ImageField(upload_to='post_img/%Y/%m/%d')

    publicado = models.BooleanField(default=False, verbose_name='Publicar')
    
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')


    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Leitor')

    titulo = models.CharField(max_length=100, verbose_name='Título do comentário')
    
    comentario = models.TextField(verbose_name='Comentário')
    
    data_comentario = models.DateTimeField(auto_now_add=True, verbose_name='Data do comentário')
    
    publicado = models.BooleanField(default=False, verbose_name='Publicar')


    def __str__(self):
        return self.titulo
