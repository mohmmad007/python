from django.contrib import admin
from .models import signin_model
# Register your models here.

@admin.register(signin_model)
class PostAdmin(admin.ModelAdmin):
    pass


# @admin.register(suggestion_model)
# class PostAdmin(admin.ModelAdmin):
#     pass
