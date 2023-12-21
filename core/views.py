from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from core.models import *
from django.shortcuts import render, redirect
from django.contrib import messages


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
    all_category = Category.objects.all()
    category = Category.objects.get(id=cid)
    dishes = Dish.objects.filter(is_published=True, category=category)

    context = {
        "category": category,
        "all_category": all_category,
        "dishes": dishes,
    }

    return render(request, "core/category-dishes-list.html", context)


def add_to_cart(request):
    cart_dish = {}

    cart_dish[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'photo': request.GET['photo'],
        'dish_id': request.GET['dish_id'],
    }

    # if 'cart-data-obj' in request.session:
    #     if str(request.GET['id']) in request.session['cart-data-obj']:
    #         cart_data = request.session['cart_data_obj']
    #         cart_data[str(request.GET['id'])]['qty'] = int(cart_dish[str(request.GET['id'])]['qty'])
    #         cart_data.update(cart_data)
    #         request.session['cart_data_obj'] = cart_data
    #     else:
    #         cart_data = request.session['cart_data_obj']
    #         cart_data.update(cart_dish)
    #         request.session['cart_data_obj'] = cart_data
    # else:
    #     request.session['cart_data_obj'] = cart_dish
    if 'cart_data_obj' in request.session:
        cart_data = request.session['cart_data_obj']

        if str(request.GET['id']) in cart_data:
            cart_data[str(request.GET['id'])]['qty'] = int(cart_dish[str(request.GET['id'])]['qty'])
        else:
            cart_data[str(request.GET['id'])] = cart_dish[str(request.GET['id'])]

        request.session['cart_data_obj'] = cart_data
    else:
        request.session['cart_data_obj'] = cart_dish
    return JsonResponse({"data": request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})


def cart_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for d_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'].replace(',', '.'))
        return render(request, "core/cart.html", {"cart_data": request.session['cart_data_obj'],
                                                  'totalcartitems': len(request.session['cart_data_obj']),
                                                  'cart_total_amount': cart_total_amount})
    else:
        messages.warning(request, "Your cart is empty")
        return redirect("core:home")


def delete_item_from_cart(request):
    d_id = str(request.GET['id'])
    if 'cart_data_obj' in request.session:
        if d_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            del request.session['cart_data_obj'][d_id]
            request.session['cart_data_obj'] = cart_data

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for d_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'].replace(',', '.'))

    context = render_to_string("core/async/cart-list.html", {"cart_data": request.session['cart_data_obj'],
                                                              'totalcartitems': len(request.session['cart_data_obj']),
                                                              'cart_total_amount': cart_total_amount})
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})

