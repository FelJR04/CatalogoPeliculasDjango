Gestor Personal de Películas y Series

Proyecto desarrollado por Felipe Quezada Maldonado para la materia Desarrollo de Software Frontend II de la Universidad CESUN.

Descripción

Es una aplicación web desarrollada con Django para organizar películas y series, crear colecciones personales y guardar favoritos.

En esta etapa se implementaron APIs REST para consultar, agregar, modificar y eliminar información.
Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- SQLite

Instalación

1. Descargar el proyecto desde GitHub.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Crear el entorno virtual con el comando: `python -m venv venv`
4. Activarlo con: `.\venv\Scripts\Activate.ps1`
5. Instalar las dependencias con: `pip install -r requirements.txt`
6. Configurar la clave secreta de Django según el archivo settings.py.
7. Aplicar las migraciones con: `python manage.py migrate`
8. Iniciar el servidor con: `python manage.py runserver`

APIs disponibles

- /api/peliculas/
- /api/series/
- /api/usuarios/
- /api/colecciones/
- /api/coleccion-peliculas/
- /api/coleccion-series/
- /api/favoritos/
- /api/auditorias/

Las APIs permiten consultar, registrar, modificar y eliminar información, dependiendo de los permisos configurados.

Estado del proyecto

Actualmente el proyecto cuenta con los modelos, la base de datos y las APIs REST. Todavía falta conectar estas funciones con la interfaz web y continuar trabajando en el diseño responsivo.