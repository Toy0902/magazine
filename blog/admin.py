from django.contrib import admin
from blog.models import Email

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['email']
# Register your models here.
