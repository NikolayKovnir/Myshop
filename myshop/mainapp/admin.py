from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)

admin.site.site_title = "Тест Магазин"
admin.site.site_header = "Тест Магазин"
