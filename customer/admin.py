from django.contrib import admin
from .models import Customer, Testimonial


class CustomerAdmin(admin.ModelAdmin):
	fields = []
	list_display = ('name',)
	list_display_links = ('name',)
	list_filter = ('name',)
	search_fields = ('name',)
	list_per_page = 3


class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('customer', 'profession')
	list_display_links = ('customer', )
	list_filter = ('customer', 'profession')
	search_fields = ('customer', 'profession')
	list_per_page = 5


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
