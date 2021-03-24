from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis import admin
from django.utils.html import format_html

from .models import sequences, panoramas, image_object_types, image_objects

@admin.register(panoramas)
class panoramaAdmin(OSMGeoAdmin):

    def eqimage_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.eqimage_thumbnail.url))

    list_display = ['eqimage_tag',]
    list_per_page = 15
    exclude = ('', )

admin.site.register(sequences, admin.OSMGeoAdmin)
admin.site.register(image_object_types)
admin.site.register(image_objects, admin.OSMGeoAdmin)

# Register your models here.
