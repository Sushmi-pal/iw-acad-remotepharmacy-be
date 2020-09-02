from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Categories'

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="medicine_pic")
    desc = models.TextField()
    price = models.CharField(max_length=30)
    in_stock = models.CharField(max_length=30)
    prod = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Cart(models.Model):
    usercart = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    order_in_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    num_of_items_purchased = models.IntegerField()
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)































