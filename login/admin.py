from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import PageView, User

# Register your models here.
class PageViewAdmin(admin.ModelAdmin):
    list_display = ['id', 'count']

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'password', 'phone', 'email', 'birthday', 'gender', 'school', 'cus_img']

admin.site.register(Permission)
admin.site.register(PageView, PageViewAdmin)
admin.site.register(User, UserAdmin)