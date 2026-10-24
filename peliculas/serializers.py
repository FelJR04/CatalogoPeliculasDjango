from rest_framework import serializers
from .models import (Usuario, Coleccion, Pelicula, ColeccionPelicula,
                     Serie, ColeccionSerie, Favorito, Auditoria)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['contrasena']
        read_only_fields = ['id_usuario', 'created_at', 'updated_at']


class ColeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coleccion
        fields = '__all__'
        read_only_fields = ['id_coleccion', 'coleccion_created_at', 'coleccion_update_at']


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'
        read_only_fields = ['id_pelicula', 'pelicula_created_at', 'pelicula_updated_at']


class ColeccionPeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColeccionPelicula
        fields = '__all__'
        read_only_fields = ['id_coleccion_pelicula', 'fecha_agregado', 'coleccion_pelicula_created_at', 'coleccion_pelicula_update_at']


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = '__all__'
        read_only_fields = ['id_serie', 'serie_created_at', 'serie_updated_at']


class ColeccionSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColeccionSerie
        fields = '__all__'
        read_only_fields = ['id_coleccion_serie', 'fecha_agregado', 'coleccion_serie_created_at', 'coleccion_serie_update_at']


class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'
        read_only_fields = ['id_favorito', 'fecha_agregado']

    def validate(self, attrs):
        tipo = attrs.get('tipo', getattr(self.instance, 'tipo', None))
        id_item = attrs.get('id_item', getattr(self.instance, 'id_item', None))
        modelo = Pelicula if tipo == 'pelicula' else Serie
        if tipo and id_item is not None and not modelo.objects.filter(pk=id_item).exists():
            raise serializers.ValidationError({'id_item': 'El registro indicado no existe.'})
        return attrs


class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        fields = '__all__'
        read_only_fields = ['id_auditoria', 'fecha']
