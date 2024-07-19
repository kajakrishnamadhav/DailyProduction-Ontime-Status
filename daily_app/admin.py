from django.contrib import admin
from . models import *

class DayWiseDataAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'date', 'sub_category'
    )
    list_display_links = ('id',)  # Optionally make 'id' field clickable
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(DayWiseData,DayWiseDataAdmin)
