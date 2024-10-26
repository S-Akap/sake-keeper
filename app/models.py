from django.db import models
from django.conf import settings
from datetime import date

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

class RestaurantManager(models.Manager):
    def get_index_list(self, user):
        user_restaurants = self.prefetch_related('bottle_management').filter(
            bottle_management__customer=user
        ).annotate(bottle_count=models.Count('bottle_management__bottle'))

        if user_restaurants.exists():
            return user_restaurants.order_by("-bottle_management__bottle")[:3]

    def get_search_list(self, query=""):
        if query != "":
            query_set = self.filter(models.Q(name__icontains=query)|models.Q(address__icontains=query))
            return query_set
        else:
            return self.prefetch_related('bottle_management').order_by('-pk')

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
    objects = RestaurantManager()

    def __str__(self):
        return self.name

class BottleManagementManager(models.Manager):
    def get_index_list(self, user):
        user_bottle_managements = self.filter(
            customer=user
        ).annotate(bottle_count=models.Count('bottle_management__bottle'))

        if user_bottle_managements.exists():
            return user_bottle_managements.order_by("-bottle_management__bottle")
        else:
            return self.order_by('-pk')

    def get_search_list(self, query=""):
        if query != "":
            query_set = self.filter(models.Q(management_name__icontains=query)|models.Q(restaurant__icontains=query))
            return query_set
        else:
            return self.prefetch_related('bottle_management').order_by('-pk')

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
    # objects = BottleManagementManager()

    def __str__(self):
        return self.management_name

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
        default = date.today()
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