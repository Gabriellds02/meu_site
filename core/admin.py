from django.contrib import admin
from core.models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'preco', 'estoque']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome','email']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
