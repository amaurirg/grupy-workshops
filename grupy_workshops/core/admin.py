from django.contrib import admin
from grupy_workshops.core.models import Workshops, Palestrantes, Interessados, Locais


class WorkshopsAdmin(admin.ModelAdmin):
    list_display = ('workshop', 'votos', 'agendado', 'realizado', 'total_participantes')


class PalestrantesAdmin(admin.ModelAdmin):
    list_display = ('palestrante', 'id_telegram')


class InteressadosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id_telegram', 'assunto_votado', 'data_votacao')


class LocaisAdmin(admin.ModelAdmin):
    list_display = ('local', 'endereco', 'data', 'hora')


admin.site.register(Workshops, WorkshopsAdmin)
admin.site.register(Palestrantes, PalestrantesAdmin)
admin.site.register(Interessados, InteressadosAdmin)
admin.site.register(Locais, LocaisAdmin)

