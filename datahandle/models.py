from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Categories'


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="medicine_pic")
    desc = models.TextField(max_length=200, verbose_name='description')
    price = models.FloatField(max_length=30)
    in_stock = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    order_in_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone
































