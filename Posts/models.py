from django.db import models

from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
import os


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


    def save(self, *args, **kwargs):
        # self.titulo = f'{self.titulo} hello'
        super().save(*args, **kwargs)
        # self.resize_image(self.imagem.name, 800)


    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size

        if width <= new_width:
            img.close()
            return

        new_height = round((new_width * height) / width)

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(img_path, optimize = True, quality=60)
        new_img.close()



class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    titulo = models.CharField(max_length=100, verbose_name='Título do comentário')
    
    comentario = models.TextField(verbose_name='Comentário')
    
    data_comentario = models.DateTimeField(auto_now_add=True, verbose_name='Data do comentário')
    
    publicado = models.BooleanField(default=False, verbose_name='Publicar')


    def __str__(self):
        return self.titulo
