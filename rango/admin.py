from django.contrib import admin
from rango.models import Category, Page,UserProfile
class pageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
admin.site.register(Category)
admin.site.register(Page,pageAdmin)
admin.site.register(UserProfile)

# Register your models here.
