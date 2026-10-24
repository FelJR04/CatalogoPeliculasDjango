from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import (Usuario, Coleccion, Pelicula, ColeccionPelicula,
                     Serie, ColeccionSerie, Favorito, Auditoria)
from .serializers import (UsuarioSerializer, ColeccionSerializer, PeliculaSerializer,
                          ColeccionPeliculaSerializer, SerieSerializer,
                          ColeccionSerieSerializer, FavoritoSerializer, AuditoriaSerializer)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]


class ColeccionViewSet(viewsets.ModelViewSet):
    queryset = Coleccion.objects.all()
    serializer_class = ColeccionSerializer
    permission_classes = [IsAdminUser]


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [IsAdminUser]


class ColeccionPeliculaViewSet(viewsets.ModelViewSet):
    queryset = ColeccionPelicula.objects.all()
    serializer_class = ColeccionPeliculaSerializer
    permission_classes = [IsAdminUser]


class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    permission_classes = [IsAdminUser]


class ColeccionSerieViewSet(viewsets.ModelViewSet):
    queryset = ColeccionSerie.objects.all()
    serializer_class = ColeccionSerieSerializer
    permission_classes = [IsAdminUser]


class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer
    permission_classes = [IsAdminUser]


class AuditoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer
    permission_classes = [IsAdminUser]
