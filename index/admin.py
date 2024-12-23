from django.contrib import admin
from index.models import Contact,Service

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=("title",)
