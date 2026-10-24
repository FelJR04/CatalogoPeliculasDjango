
from django.shortcuts import render
from .models import Pelicula, Serie, Coleccion


def inicio(request):
    peliculas_recientes = Pelicula.objects.order_by('-pk')[:4]
    series_recientes = Serie.objects.order_by('-pk')[:4]

    return render(request, 'peliculas/inicio.html', {
        'total_peliculas': Pelicula.objects.count(),
        'total_series': Serie.objects.count(),
        'total_colecciones': Coleccion.objects.count(),
        'ultimas_peliculas': peliculas_recientes,
        'ultimas_series': series_recientes,
    })


def peliculas(request):
    return render(request, 'peliculas/listado.html', {
        'titulo_pagina': 'Películas',
        'tipo': 'peliculas',
        'elementos': Pelicula.objects.all(),
    })


def series(request):
    return render(request, 'peliculas/listado.html', {
        'titulo_pagina': 'Series',
        'tipo': 'series',
        'elementos': Serie.objects.all(),
    })


def colecciones(request):
    return render(request, 'peliculas/colecciones.html', {
        'elementos': Coleccion.objects.all(),
    })
