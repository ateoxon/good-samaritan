from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

# admin.site.register(item)
@admin.register(Foods, Drinks, MiscObjects)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
