from django.http import HttpResponse
from core.models import *
from django.shortcuts import render


def index(request):
    # dishes = Dish.objects.all().order_by("category_id")
    dishes = Dish.objects.filter(is_published=True)
    categories = Category.objects.all()
    context = {
        "dishes": dishes,
        "categories": categories,
    }
    return render(request, "core/index.html", context)


def dishes_list_view(request):
    dishes = Dish.objects.filter(is_published=True)

    context = {
        "dishes": dishes
    }

    return render(request, "core/dishes_list.html", context)


def category_list_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, "core/category_list.html", context)


def dishes_list_category_view(request, cid):
    category = Category.objects.get(id=cid)
    dishes = Dish.objects.filter(is_published=True, category=category)

    context = {
        "category": category,
        "dishes": dishes,
    }

    return render(request, "core/category-dishes-list.html", context)
