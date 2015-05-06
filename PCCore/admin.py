from django.contrib import admin
from PCWebService.models import Member
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ["user", "email", "app_key", "UUID"]
admin.site.register(Member,MemberAdmin)