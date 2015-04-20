from django.contrib import admin
from models import RSSSourceList,RSSCategory
# Register your models here.
class RSSListAdmin(admin.ModelAdmin):
    list_display = ['category','url','last_update']
class RSSCateAdmin(admin.ModelAdmin):
    pass
admin.site.register(RSSSourceList,RSSListAdmin)
admin.site.register(RSSCategory,RSSCateAdmin)