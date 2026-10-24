
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Tabla: usuario
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=32)
    email = models.EmailField(max_length=30, unique=True)
    contrasena = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


# Tabla: coleccion
class Coleccion(models.Model):
    id_coleccion = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario',
        related_name='colecciones'
    )
    nombre = models.CharField(max_length=32)
    activo = models.BooleanField(default=True)
    coleccion_created_at = models.DateTimeField(auto_now_add=True)
    coleccion_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'coleccion'
        verbose_name = 'Colección'
        verbose_name_plural = 'Colecciones'


# Tabla: pelicula
class Pelicula(models.Model):
    id_pelicula = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=32, db_index=True)
    anio = models.IntegerField(null=True, blank=True)
    genero = models.CharField(max_length=30, db_index=True)
    pelicula_created_at = models.DateTimeField(auto_now_add=True)
    pelicula_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'pelicula'
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'


# Tabla: coleccionpelicula
class ColeccionPelicula(models.Model):
    id_coleccion_pelicula = models.AutoField(primary_key=True)

    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.PROTECT,
        db_column='id_pelicula',
        related_name='colecciones_pelicula'
    )

    coleccion = models.ForeignKey(
        Coleccion,
        on_delete=models.CASCADE,
        db_column='id_coleccion',
        related_name='peliculas_coleccion'
    )

    fecha_agregado = models.DateTimeField(auto_now_add=True)
    opinion = models.CharField(max_length=255, null=True, blank=True)
    nombre_personalizado = models.CharField(
        max_length=32, null=True, blank=True
    )
    calificacion = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    coleccion_pelicula_created_at = models.DateTimeField(auto_now_add=True)
    coleccion_pelicula_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pelicula} - {self.coleccion}'

    class Meta:
        db_table = 'coleccionpelicula'
        verbose_name = 'Película en colección'
        verbose_name_plural = 'Películas en colecciones'
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(calificacion__gte=1, calificacion__lte=5)
                    | models.Q(calificacion__isnull=True)
                ),
                name='chk_calificacion_pelicula'
            )
        ]


# Tabla: series
class Serie(models.Model):
    ESTADOS = [
        ('En emisión', 'En emisión'),
        ('Finalizada', 'Finalizada'),
        ('Cancelada', 'Cancelada'),
    ]

    id_serie = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=32, db_index=True)
    anio_inicio = models.IntegerField(null=True, blank=True)
    anio_fin = models.IntegerField(null=True, blank=True)
    genero = models.CharField(max_length=30, db_index=True)
    temporadas = models.IntegerField(null=True, blank=True)
    episodios = models.IntegerField(null=True, blank=True)
    sinopsis = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        null=True,
        blank=True
    )
    serie_created_at = models.DateTimeField(auto_now_add=True)
    serie_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'series'
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'


# Tabla: coleccionserie
class ColeccionSerie(models.Model):
    id_coleccion_serie = models.AutoField(primary_key=True)

    serie = models.ForeignKey(
        Serie,
        on_delete=models.PROTECT,
        db_column='id_serie',
        related_name='colecciones_serie'
    )

    coleccion = models.ForeignKey(
        Coleccion,
        on_delete=models.CASCADE,
        db_column='id_coleccion',
        related_name='series_coleccion'
    )

    fecha_agregado = models.DateTimeField(auto_now_add=True)
    opinion = models.CharField(max_length=255, null=True, blank=True)
    calificacion = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    nombre_personalizado = models.CharField(
        max_length=32, null=True, blank=True
    )
    coleccion_serie_created_at = models.DateTimeField(auto_now_add=True)
    coleccion_serie_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.serie} - {self.coleccion}'

    class Meta:
        db_table = 'coleccionserie'
        verbose_name = 'Serie en colección'
        verbose_name_plural = 'Series en colecciones'
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(calificacion__gte=1, calificacion__lte=5)
                    | models.Q(calificacion__isnull=True)
                ),
                name='chk_calificacion_serie'
            )
        ]


# Tabla: favorito
class Favorito(models.Model):
    TIPOS = [
        ('pelicula', 'Película'),
        ('serie', 'Serie'),
    ]

    id_favorito = models.AutoField(primary_key=True)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario',
        related_name='favoritos'
    )

    tipo = models.CharField(max_length=20, choices=TIPOS)
    id_item = models.IntegerField()
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario} - {self.tipo} ({self.id_item})'

    class Meta:
        db_table = 'favorito'
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'tipo', 'id_item'],
                name='uk_favorito_unico'
            )
        ]


# Tabla: auditoria
class Auditoria(models.Model):
    id_auditoria = models.AutoField(primary_key=True)
    tabla = models.CharField(max_length=50)
    operacion = models.CharField(max_length=20)
    id_registro = models.IntegerField()

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='usuario_id',
        related_name='auditorias'
    )

    datos_anteriores = models.TextField(null=True, blank=True)
    datos_nuevos = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f'{self.operacion} - {self.tabla} ({self.id_registro})'

    class Meta:
        db_table = 'auditoria'
        verbose_name = 'Auditoría'
        verbose_name_plural = 'Auditorías'
        indexes = [
            models.Index(fields=['tabla', 'id_registro'])
        ]
