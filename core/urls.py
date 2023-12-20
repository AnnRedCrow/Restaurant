from django.urls import path
from core.views import *

app_name = "core"

urlpatterns = [
    path("", index, name="home"),
    path("category/", category_list_view, name="category_list"),
]