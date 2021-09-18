from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin

from .models import Post, Categoria, Comentario


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria',)
    list_display_links = ('id', 'nome_categoria',)
    search_fields = ('id', 'nome_categoria',)
    
    list_per_page = 5


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = 'conteudo'
    
    list_display = ('id', 'titulo', 'autor', 'categoria', 'publicado', 'data_criacao')
    list_display_links = ('id', 'titulo')
    list_editable = ('autor', 'categoria', 'publicado')
    list_filter = ('publicado', 'publicado')
    # ordering = ('titulo')
    search_fields = ('id', 'titulo')
    
    list_per_page = 5

    summernote_fields = ('conteudo',)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)
