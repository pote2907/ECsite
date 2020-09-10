from .models import MediumCategory


def menu_links(request):
    """カテゴリーのリンクを返す"""
    links = MediumCategory.objects.all()
    return dict(links=links)
