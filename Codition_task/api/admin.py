from django.contrib import admin
from . models import Product , Category

admin.site.register(Category),
admin.site.register(Product)
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_select_related = ('category')
    class Meta:
        model = Product

class CategoryAdmin(admin.ModelAdmin):
    list_select_related = ('parent',)
    list_display = ('name', 'parent', )
    class Meta:
        model = Category