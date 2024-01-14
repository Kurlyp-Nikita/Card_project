from django.contrib import admin
from .models import *


admin.site.register(Tovar)


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ('user', 'tovar', 'count', 'summa')
