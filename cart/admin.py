from django.contrib import admin
from cart.models import Cart,CartItem


# Register your models here.

class CartAdmin(admin.ModelAdmin):
    pass

class CartItemAdmin(admin.ModelAdmin):
    pass