from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('title',)
	list_per_page = 20


admin.site.register(Service, ServiceAdmin)
