from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe

from userauths.models import User


STATUS = (
    ("process", "Processing"),
    ("cooking", "Cooking"),
    ("packed", "Packed"),
    ("sent", "Sent"),
    ("delivered", "Delivered"),
)


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    image = models.ImageField(upload_to="category")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))


class Dish(models.Model):
    dish_id = ShortUUIDField(unique=True, length=10, max_length=15, prefix="dish", alphabet="abcdef1234")
    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    amount = models.CharField(max_length=50, verbose_name='Вес или размер')
    photo = models.ImageField(upload_to='menu_items', verbose_name='Фото', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    is_recommended = models.BooleanField(default=False, verbose_name='Рекомендовано')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    def dish_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.photo.url))

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ['created_at']


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=30, default="cooking")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"

    def order_image(self):
        return mark_safe('<img src="/media/%s" width="50" height="50"/>' % (self.image))


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"











