from django.contrib import admin
from .models import *

# Register your models here.
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('data', 'valor', 'descricao', 'usuario')
    search_fields = ('data', )
    list_filter = ('usuario',)

admin.site.register(Despesa, DespesaAdmin)