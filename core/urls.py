from django.urls import path
from core.views import *

app_name = "core"

urlpatterns = [
    path("", index, name="home"),
    path("dishes/", dishes_list_view, name="dishes_list"),
    path("category/", index, name="category_list"),
    path("category/<cid>", dishes_list_category_view, name="category-dishes-list"),
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    path("cart/", cart_view, name="cart"),
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),
]