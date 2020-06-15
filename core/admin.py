from django.contrib import admin
from core.models import Product,Category,UserProfile
# Register your models here.



# admin.site.register(Product,ProductAdmin)
# below is same as above

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    pass
