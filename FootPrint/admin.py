from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.site_header = '我的足迹管理后台'
admin.site.site_title = '我的足迹管理后台'



@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    # raw_id_fields = ['substation']
    list_display = ['id', 'name', 'text', 'mark','img','marker_image','create', 'update']

    def img(self, obj):
        div = f"<img src='{obj.marker_image}' width='32px'>" if obj.marker_image and obj.marker_image !=''   else ''
        return mark_safe(div)

@admin.register(MarkerImage)
class MarkerImageAdmin(admin.ModelAdmin):
    # raw_id_fields = ['substation']
    list_display = ['id', 'normal_image', 'passed_image','create', 'update']