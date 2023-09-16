from django.contrib import admin
from app_cad_usuarios.models import Usuario

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nome', 'idade', 'email', 'telefone')
    list_filter = ('nome', 'idade', 'email', 'telefone')

admin.site.register(Usuario, UsuarioAdmin)