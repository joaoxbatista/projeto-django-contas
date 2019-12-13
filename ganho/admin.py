from django.contrib import admin
from .models import *

# Register your models here.
class GanhoAdmin(admin.ModelAdmin):
    list_display = ('data', 'valor', 'descricao', 'usuario')
    search_fields = ('data', )
    list_filter = ('valor',)

admin.site.register(Ganho, GanhoAdmin)