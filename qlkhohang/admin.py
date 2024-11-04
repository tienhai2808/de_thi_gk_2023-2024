from django.contrib import admin
from .models import *

# Register your models here.
class KhoHangHoaAdmin(admin.ModelAdmin):
  list_display = ('hang_hoa', 'kho', 'so_luong')
  list_filter = ('kho', 'so_luong')


admin.site.register(Kho)
admin.site.register(HangHoa)
admin.site.register(KhoHangHoa, KhoHangHoaAdmin)
