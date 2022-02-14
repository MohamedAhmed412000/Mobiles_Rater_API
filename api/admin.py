from django.contrib import admin
from .models import Mobile, Rating

# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'mobile', 'stars']
    list_filter = ['user', 'mobile']

class MobileAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'name', 'price']
    search_fields = ['company', 'name']
    list_filter = ['company']

admin.site.register(Mobile, MobileAdmin)
admin.site.register(Rating, RatingAdmin)
