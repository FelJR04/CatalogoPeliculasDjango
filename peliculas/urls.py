from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (UsuarioViewSet, ColeccionViewSet, PeliculaViewSet,
                    ColeccionPeliculaViewSet, SerieViewSet,
                    ColeccionSerieViewSet, FavoritoViewSet, AuditoriaViewSet)

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('colecciones', ColeccionViewSet)
router.register('peliculas', PeliculaViewSet)
router.register('coleccion-peliculas', ColeccionPeliculaViewSet)
router.register('series', SerieViewSet)
router.register('coleccion-series', ColeccionSerieViewSet)
router.register('favoritos', FavoritoViewSet)
router.register('auditorias', AuditoriaViewSet)

urlpatterns = [path('', include(router.urls))]
