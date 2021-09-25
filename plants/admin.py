from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Place, Plant, Category
from django.contrib import admin

admin.site.site_header = "Proyecto Desarrollo de software II"
admin.site.site_title = "Proyecto Desarrollo de software II"
admin.site.index_title = "Proyecto Desarrollo de software II"


@admin.register(Place)
class PlaceAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'latitude',)
    list_display_links = ('pk',)
    search_fields = ('latitude',)
    list_filter = ('latitude',)
    class PlaceResource(resources.ModelResource):
       class Meta:
        model = Place

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    search_fields = ('name',)
    list_filter = ('name',)
    class CategoryResource(resources.ModelResource):
       class Meta:
        model = Category

@admin.register(Plant)
class PlantAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    search_fields = ('name',)
    list_filter = ('name',)

    class PlantResource(resources.ModelResource):
        class Meta:
         model = Plant