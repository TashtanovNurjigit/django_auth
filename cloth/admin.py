from django.contrib import admin
from . import models

admin.site.register(models.CustomerCL)
admin.site.register(models.TagCL)
admin.site.register(models.ProductCL)
admin.site.register(models.OrderCL)
