from django.contrib.auth.models import UserManager
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    objects = UserManager()

    class Meta:
        permissions = (("can_put_on_sale", "Put product on sale"),)

    def __str__(self):
        return self.name
