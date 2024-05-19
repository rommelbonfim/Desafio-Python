from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import usuario, Produto, Pedido

# Definindo uma classe UserAdmin personalizada
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('email',)}),
    )
    search_fields = ('username', 'email', 'first_name')


admin.site.register(usuario, UserAdmin)

# Registrando o modelo de produto
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

# Registrando o modelo de Pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario','produto')
    list_filter = ('usuario',)
    search_fields = ('usuario__username', 'usuario__email')

    def usuario(self, obj):
        return obj.usuario.username
