from django.contrib import admin

from .models import *
from .forms import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProdectAdminForm

    list_display = ('name', 'price', 'old_price', 'create_time', 'update_time',)
    # list_display_links 提供一个超链接
    list_display_links = ('name',)
    prepopulated_fields = {'slug':('name',)}
    # 每页显示数据条数
    list_per_page = 50

    ordering = ['-create_time']
    search_fields = ('name', 'description', 'meta_keywords', 'meta_description')

    # exclude表示 !=
    exclude = ('create_time', 'update_time')




@admin.register(Category)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time', 'update_time',)
    list_display_links = ('name',)
    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}
    ordering = ['name']
    search_fields = ('name', 'description', 'meta_keywords', 'meta_description')
    exclude = ('create_time', 'update_time')