from django.urls import path
from . import frontend_views

urlpatterns = [
    path('', frontend_views.inicio, name='inicio'),
    path('peliculas/', frontend_views.peliculas, name='pagina_peliculas'),
    path('series/', frontend_views.series, name='pagina_series'),
    path('colecciones/', frontend_views.colecciones, name='pagina_colecciones'),
]