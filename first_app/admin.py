from django.contrib import admin
from .models import back_mart
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class back_martAdmin(ImportExportModelAdmin):
    list_display=['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']

admin.site.register(back_mart, back_martAdmin)