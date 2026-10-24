
from django.contrib import admin
from .models import (
    Usuario,
    Coleccion,
    Pelicula,
    ColeccionPelicula,
    Serie,
    ColeccionSerie,
    Favorito,
    Auditoria,
)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre', 'email')
    search_fields = ('nombre', 'email')


@admin.register(Coleccion)
class ColeccionAdmin(admin.ModelAdmin):
    list_display = ('id_coleccion', 'nombre', 'usuario', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre',)


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('id_pelicula', 'titulo', 'anio', 'genero')
    search_fields = ('titulo', 'genero')
    list_filter = ('genero',)


@admin.register(ColeccionPelicula)
class ColeccionPeliculaAdmin(admin.ModelAdmin):
    list_display = ('id_coleccion_pelicula', 'pelicula', 'coleccion', 'calificacion')


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('id_serie', 'titulo', 'genero', 'estado')
    search_fields = ('titulo', 'genero')
    list_filter = ('estado', 'genero')


@admin.register(ColeccionSerie)
class ColeccionSerieAdmin(admin.ModelAdmin):
    list_display = ('id_coleccion_serie', 'serie', 'coleccion', 'calificacion')


@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('id_favorito', 'usuario', 'tipo', 'id_item')
    list_filter = ('tipo',)


@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ('id_auditoria', 'tabla', 'operacion', 'usuario', 'fecha')
    list_filter = ('tabla', 'operacion')
    readonly_fields = ('fecha',)
