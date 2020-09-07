from .models import Category


def menu_links(request):
    """カテゴリーのリンクを返す"""
    links = Category.objects.all()
    return dict(links=links)
