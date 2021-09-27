from django import template


register = template.Library()


@register.filter(name='plural_comments')
def plural_comments(num_comments):
    if num_comments == 0:
        return 'Nenhum Comentário'
    elif num_comments == 1:
        return '1 Comentário'

    return f'{num_comments} Comentários'
