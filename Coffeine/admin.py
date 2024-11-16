from django.contrib import admin
from Coffeine.models import productModel,categoryModel,messageModel,orderModel,userModel

# Register your models here.
admin.site.register(productModel)
admin.site.register(categoryModel)
admin.site.register(messageModel)
admin.site.register(orderModel)
admin.site.register(userModel)