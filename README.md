Aprendiendo Django paso a paso
PASO PARA CREAR UNA WEB EN DJANDO

1. Crear entorno virtual con Python
   virtualenv env

2. Activar ambiente virtual en Mac
   source env/bin/activate
   deactivate -->Para desactivar mi entorno virtual

3. Instalar Djando desde Pip en nuestro entorno virtual.
   python -m pip install Django
   pip install Django

4. Crear el proyecto con Djando
   django-admin startproject core .
   El punto . es crucial porque le dice al script que instale Django en el directorio actual,
   para el cual el punto sirve de abreviatura

   - Ya en este punto se puede correr el proyecto que a creado Django,
     usando python manage.py runserver

5. Crear mi primera aplicación en Django
   python manage.py startapp blog

6. Instalar nuestra aplicación (blog) ya creada en nuestro proyecto
   archivo settings.py
   INSTALLED_APPS = [
   ----,
   'blog',
   ]

7. Crear el archivo urls.py en nuestra aplicación creada (blog)
   from django.urls import path
   from . import views

   urlpatterns = [

   # this is the home url

   path('', views.home, name='home'),

   # this is the single book url

   path('book-detail/<str:id>/', views.book_detail, name='book-detail'),

   # this is the add book url

   path('add-book/', views.add_book, name='add-book'),

   # this is the edit book url

   path('edit-book/<str:id>/', views.edit_book, name='edit-book'),

   # this is the delete book url

   path('delete-book/<str:id>/', views.delete_book, name='delete-book'),
   ]

8. Conectar nuestra aplicación ir a uls.py este archivo esta en el proyecto
   from django.urls import path, include
   urlpatterns = [
   path('admin/', admin.site.urls),

   # registering blog application's urls in project

   path('blog/', include('blog.urls')),
   ]

9. Correr el proyecto creado en Python & Django
   python manage.py runserver

10. Revisar la consola y visitar la URL http://127.0.0.1:8000

11. Agregar el gitignore de Python y Djando
    https://github.com/jpadilla/django-project-template/blob/master/.gitignore

12. Crear archivo README.md para describir el proyecto etc.

13. Crear la carpeta 'templates' dentro de mi aplicacion donde estaran mis archivos .html

14. Crear la carpeta 'static' dentro de mi aplicacion, aqui estaran archivos
    estaticos (css, js, imagenes, etc..)

COMANDO ADICIONALES:

1. Correr migraciones
   python manage.py migrate

2. Crear migraciones
   python manage.py makemigrations blog

3. ver todo el historial de migraciones:
   python manage.py showmigrations

4. listar paquetes del instalador en el proyecto
   pip list
   pip freeze

5. Version de Djando en mi proyecto
   python -m django --version

6. Instalar Paquete para crear variables de entorno
   pip install django-environ
7. Crear el archivo requirements.txt
   pip freeze > requirements.txt

8. Correr archivo requirement.txt
   pip install -r requirements.txt

9. Driver para conectar MySQL con Django
   pip install pymysql

Jinja2 (una biblioteca de plantillas)
Django es un framework web gratuito y de código abierto publicado por primera vez en 2005 por
Adrian Holovaty y Simon Willison.

Django es un sofisticado framework basado en Python con configuraciones de desarrollo de pila completa,
como diseños de plantillas, solicitud y resolución de problemas, cookies, validación de formularios,
pruebas unitarias, configuración de tablas y otras funcionalidades que los desarrolladores
utilizan para crear aplicaciones web dinámicas.

Django sigue un patrón arquitectónico Modelo-Vista-Plantilla (MVT) que ayuda a los desarrolladores a
realizar tareas rutinarias o complejas de forma eficiente con poca intervención de protocolos,
administración y sistemas al crear aplicaciones de alta intensidad y sitios web basados en bases de datos.
Importante Djando genera las migraciones a partir de la informacion que existe en el modelo

---

Un proyecto en Django vs aplicacion (son como modulos de mi proyecto) en Django, en generar un
proyecto en Django esta compuesto por aplicaciones.

amazon.com -> es el proyecto
usuarios ->crear, editar, borrar, recuperar etc seria mi aplicacion o modulo
tienda ->agregar, producto, borrar, editar, enviar producto etc.

---

Los modelos Django proporciona una capa de abstracción
(los «modelos») para estructurar y manipular los datos de su aplicación web.

Crear administrador:
python manage.py createsuperuser
Luego escribir cualquier usuario y clave
Las migraciones comprenden;la autentiticafion por defecto de Django
Existen vistas de clases y vistas de funciones.
