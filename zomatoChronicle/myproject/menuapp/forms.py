from django import forms
from .models import Dish,Orders

class DishForm(forms.ModelForm):
    class Meta:
        model=Dish
        fields=['dishName','price']


class OrderForm(forms.ModelForm):
    dishes= forms.ModelMultipleChoiceField(queryset=Dish.objects.all(),widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Orders
        fields=['customer_name','dishes']