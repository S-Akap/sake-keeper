from django import forms
from .models import Restaurant, BottleManagement, Bottle

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name", "address")

class BottleManagementForm(forms.ModelForm):
    class Meta:
        model = BottleManagement
        fields = ("management_name", "restaurant")

class BottleForm(forms.ModelForm):
    class Meta:
        model = Bottle
        fields = ("management", "liquor_type", "bottle_name")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields["management"].queryset = BottleManagement.objects.filter(customer=user)