from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from reviewCWapp.models import Cocktail


# Create your views here.


def index(request):
    render(request, 'reviewCWapp/index.html')
    return HttpResponse('index')


def page2(request, pageID):
    render(request, 'reviewCWapp/page2.html')
    return HttpResponse('page2')


def page3(request, pageID):
    render(request, 'reviewCWapp/page3.html')
    return HttpResponse('page3')


def page4(request, pageID):
    render(request, 'reviewCWapp/page4.html')
    return HttpResponse('page4')


def page5(request, pageID):
    render(request, 'reviewCWapp/page5.html')
    return HttpResponse('page5')


def create(request):
    newObj = Cocktail.object.create(name='Long Island', alcoholPercentage=20, servingGlass='tall')
    newObj1 = Cocktail.object.create(name='Whiskey Sour', alcoholPercentage=20, servingGlass='short')
    newObj2 = Cocktail.object.create(name='7 and 7', alcoholPercentage=20, servingGlass='short')
    list = Cocktail.objects.all()
    context = [
        "list":list,
    ]

    return render(request, 'reviewCWapp/cocktails.html', context)
