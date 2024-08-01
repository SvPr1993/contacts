from django.shortcuts import render
from .models import Shops


def shops_views(request):
    shops_list = Shops.objects.all()
    context = {'shops_list': shops_list, 'title': 'Shops'}
    return render(request, 'shops.html', context)
