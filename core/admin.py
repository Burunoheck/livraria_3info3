from django.contrib import admin

from core.models import Autor, Categoria, Editora

admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Categoria)
