from django.shortcuts import render


def search_result(request):
    return render(request, 'search.html', {})
