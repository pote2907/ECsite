from django.http import HttpResponse


def all_products(request):
    return HttpResponse('This is a Top Page')