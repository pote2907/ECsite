from .models import MediumCategory, LargeCategory


def medium_menu_links(request):
    """中カテゴリーのリンクを返す"""
    medium_links = MediumCategory.objects.all()
    return dict(medium_links=medium_links)

def large_menu_links(request):
    """大カテゴリーのリンクを返す"""
    large_links = LargeCategory.objects.all()
    return dict(large_links=large_links)