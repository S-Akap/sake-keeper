from django.db import models
from django.conf import settings

LIQUOR_TYPE = [
    ("gi", "Gin"),
    ("vo", "Vodka"),
    ("te", "Tequila"),
    ("ru", "Rum"),
    ("wi", "Whisky"),
    ("br", "Brandy"),
    ("sh", "Shochu"),
    ("ot", "Other")
]

class Restaurant(models.Model):
    name = models.CharField(
        verbose_name="店名",
        unique=True,
        max_length=20
    )
    address = models.CharField(
        verbose_name="住所",
        unique=True,
        max_length=50
    )
    create_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="ユーザー",
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name

class BottleManagement(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="ユーザー",
        on_delete=models.CASCADE
    )
    restaurant = models.ForeignKey(
        Restaurant,
        verbose_name="飲食店",
        on_delete=models.PROTECT,
        related_name="bottle_management"
    )
    management_name = models.CharField(
        verbose_name="管理用ID",
        max_length=10
    )

    def __str__(self):
        return f"{self.customer}_{self.management_name}"

class Bottle(models.Model):
    management = models.ForeignKey(
        BottleManagement,
        verbose_name="管理用ID",
        on_delete=models.CASCADE,
        related_name="bottle"
    )
    liquor_type = models.CharField(
        verbose_name="アルコール種類",
        choices=LIQUOR_TYPE,
        max_length=2
    )
    bottle_name = models.CharField(
        verbose_name="酒名",
        max_length=20
    )
    purchase_date = models.DateField(
        verbose_name="ボトル購入日",
        auto_now=True
    )
    storage_period = models.DateField(
        verbose_name="預かり期日",
        null=True,
        blank=True
    )
    is_empty = models.BooleanField(
        verbose_name="空ボトルか？",
        default=False
    )

    def __str__(self):
        return self.bottle_name