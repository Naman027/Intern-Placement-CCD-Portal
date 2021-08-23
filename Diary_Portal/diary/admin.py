from django.contrib import admin
from .models import company,remarks
# Register your models here.


class remarksInline(admin.StackedInline):
    model = remarks

class courseadmin(admin.ModelAdmin):
    inlines = [remarksInline,]
admin.site.register(company)
admin.site.register(remarks)