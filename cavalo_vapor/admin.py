from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Endereco)
admin.site.register(Email)
admin.site.register(Empresa)
admin.site.register(Funcionario)
admin.site.register(Caminhoneiro)
admin.site.register(FuncionarioEmpresa)
admin.site.register(Caminhao)
admin.site.register(Carreta)

admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Marca)
admin.site.register(TipoCarreta)
admin.site.register(TipoReboque)