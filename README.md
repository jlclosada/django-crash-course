# Curso Django

## 1. Creación del entorno virtual e instalación de Django

Lo primero de todo es crear un entorno virtual en nuestra carpeta de trabajo.
En este caso vamos a llamar a nuestra carpeta de trabajo "django-crash-course".

 Al estar trabajando con Python, el comando para crear un nuevo entorno de trabajo es:
 `python -m venv {venv}`
 - {venv} --> Lo sustituimos con el nombre que queramos. En mi caso **.env**
 
###  1.1. Activación del entorno virtual
Para la instalación y gestión de los paquetes de nuestro proyecto debemos activar nuestro entorno virtual. Dependiendo de nuestro SO, el comando puede variar:
> CMD
`venv\Scripts\activate.bat`

> Poweshell
`venv\Scripts\Activate.ps1`

> Git Bash
`source venv/Scripts/activate`

Nosotros estamos trabajando en Windows, con una terminal CMD. Por lo que nuestro comando es:
`.env\Scripts\activate`

Si lo hemos hecho bien, nuestra terminal deberá aparecer de la siguiente manera: 
> (.env) PS D:\Code\Proyectos\django-crash-course>

### 1.2. Instalación de Django
Una vez que tenemos activado nuestro entorno virtual, podemos instalar las dependencias necesarias en nuestro proyecto. Django no viene instalado por defceto en Python ,por lo que tendremos que descargarlo e instalarlo usando el gestor de paquetes **pip**

En la terminal lanzamos el siguiente comando:
`pip install django`

Automáticamente, Django y todas sus dependencias se descargarán y se isntalarán en nuestro entorno virtual y ya podremos empezar a usar Django :)


## 2. Primeros pasos con Django
### 2.1. Creación de un proyecto en Django
Una vez que hemos instalado Django en nuestro entorno virtual, podemos crear nuestro primer proyecto. Podemos comprobar que Django se ha instalado correctamente deesta manera:
`python -m django --version`

El siguiente paso es crear nuestro proyecto, directamente desde la terminal:
`django-admin startproject mysite`

Ester comando lo que hará será crear un proyecto de Django llamado **mysite**.
> Debes evitar nombrar proyectos con nombres de componentes integrados de Python o Django. Esto significa que debes evitar usar nombres como django(que entrará en conflicto con el propio Django) o test(que entra en conflicto con un paquete integrado de Python).

En mi caso, a la misma altura que el .env, he creado una carpeta nueva llamada **"django-crash-course"** y después he utilizado el siguiente comando:
`django-admin startproject mysite django-crash-course `

De esta manera, se ha creado mi proyecto de Django de nombre **mysite**, dentro de la carpeta **"django-crash-course"**. 

Automáticamente se habrá creado mi estructura principal del proyecto:
- djangotutorial/
    - manage.py
    - mysite/
        - __init__.py
        - settings.py
		- urls.py
        - asgi.py
        - wsgi.py

Estos archivos son:

- manage.py --> Una utilidad de línea de comandos que te permite interactuar con este proyecto de Django de diversas maneras. Puedes leer todos los detalles manage.py en django-admin y manage.py .

- mysite/ --> Un directorio que contiene el paquete de Python de tu proyecto. Su nombre es el nombre del paquete de Python que necesitarás para importar cualquier contenido (por ejemplo, mysite.urls).

- mysite/__init__.py --> Un archivo vacío que indica a Python que este directorio debe considerarse un paquete. Si eres principiante en Python, lee más sobre paquetes en la documentación oficial de Python.

- mysite/settings.py --> Configuración de este proyecto de Django. La configuración de Django te explicará todo sobre su funcionamiento.

- mysite/urls.py --> Las declaraciones de URL de este proyecto de Django; una tabla de contenido de tu sitio web basado en Django.

- mysite/asgi.py --> Un punto de entrada para servidores web compatibles con ASGI que atiendan tu proyecto.

- mysite/wsgi.py --> Un punto de entrada para servidores web compatibles con WSGI que atiendan tu proyecto.

Ya tendríamos Django listo, y si ejecutamos dentro de nuestra nueva carpeta el siguiente comando, podremos comprobar que nuestra aplicación ya está corriendo:
`python manage.py runserver`

Por defecto, como buen backend, esto se ejecuta en la ruta http://127.0.0.1:8000/; pero podemos cambiar el puerto de esta manera: 
`python manage.py runserver 8001`

Así, podemos especificar el puerto en el que correr nuestra aplicación.

### 2.2 . Proyectos vs. Apps y tu primera App
Perfecto, ya has creado el proyecto mysite. Ahora toca entender uno de los conceptos más importantes de Django: la diferencia entre un Proyecto y una App.

- **Proyecto Django**: Piensa en el proyecto como el contenedor de todo tu sitio web. Gestiona la configuración global (settings.py), las rutas URL principales (urls.py) y agrupa una o más "apps".

- **App Django**: Una "app" es un módulo autocontenido que realiza una función específica. Por ejemplo, podrías tener una app para los usuarios, otra para los productos, y otra para los pedidos. Las apps están diseñadas para ser reutilizables.

Nuestro objetivo es crear una API, así que vamos a crear una app dedicada a gestionar toda la lógica de la API.

#### Paso 1: Crear nuestra primera app
1. Abre tu terminal.
2. Asegúrate de que estás dentro de la carpeta de tu proyecto, al mismo nivel que el archivo manage.py.
3. Ejecuta el siguiente comando para crear una app llamada **api**:
`python manage.py startapp api`

Ahora, si miras tu estructura de carpetas, verás que ha aparecido un nuevo directorio llamado api con varios archivos dentro (models.py, views.py, etc.). ¡Esa es tu primera app!

#### Paso 2: Registrar la App en el proyecto
Crear la app no es suficiente; debemos decirle a nuestro proyecto mysite que esta nueva app api existe y que debe tenerla en cuenta.

1. Abre el archivo mysite/settings.py.
2. Busca la lista llamada **INSTALLED_APPS**.
3. Añade el nombre de tu app ('api') al final de la lista. Te recomiendo añadir un comentario para saber cuáles son tus apps locales.
4. Guarda el archivo.

A mi personalmente me gusta diferenciar dentro de esta lista que apps son "base", cuales son mías, y cuales son de terceros. Las veremos más adelante. De maenra que se vería así:
```python
# mysite/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Apps
    'api',

    # Third Apps
]
```

¡Felicidades! Has creado y registrado correctamente tu primera aplicación. Este es el flujo de trabajo fundamental para añadir nuevas funcionalidades a cualquier proyecto de Django.

### 2.3. Tu Primer Modelo y las Migraciones
En Django, un Modelo es la única y definitiva fuente de información sobre tus datos. Es una clase de Python que representa una tabla en tu base de datos. Django usa estos modelos para crear las tablas y para interactuar con ellas (leer, escribir, actualizar, etc.).

Para nuestro proyecto, vamos a crear un modelo simple pero muy común: una Tarea (Task).

#### Paso 1: Creando el Modelo "Task"
1. Abre el archivo api/models.py. Por defecto, estará casi vacío.
2. Reemplaza su contenido con el siguiente código para definir nuestro modelo Task:


    # api/models.py
    from django.db import models
    
    class Task(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField(blank=True, null=True)
        completed = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            return self.title

- **class Task(models.Model)** -->  Define una clase llamada Task que hereda de **models.Model**. Así es como Django sabe que esto es un modelo.

- **title = models.CharField(...)** --> Un campo de texto para el título. max_length=200 es obligatorio para los CharField.

- **description = models.TextField(...)** --> Un campo para textos largos. blank=True, null=True significa que este campo es opcional.

- **completed = models.BooleanField(...)**: Un campo que será True o False. Por defecto (default=False), las tareas se crearán como no completadas.

- **created_at = models.DateTimeField(...)**: Un campo de fecha y hora. auto_now_add=True le dice a Django que guarde la fecha y hora actual automáticamente cuando se cree una nueva tarea.

- **def __str__(self):**: Este método especial le dice a Django cómo "mostrar" un objeto **Task** de forma legible (por ejemplo, en el panel de administrador). Aquí, le decimos que muestre el título de la tarea.


#### Paso 2: Las Migraciones (el 'Control de Versiones' de tu Base de Datos)
Ahora que hemos definido el modelo en Python, necesitamos traducir esa definición a un formato que la base de datos entienda (lenguaje SQL) y aplicarlo. Este proceso se hace en dos pasos.

1. **Crear el archivo de migración**:
Este comando analiza tus models.py, detecta los cambios (en este caso, la creación del modelo Task) y genera un archivo de instrucciones en la carpeta api/migrations/.

Abre tu terminal (asegúrate de estar en la carpeta del proyecto con manage.py) y ejecuta:
`python manage.py makemigrations`

> Verás una salida parecida a: Migrations for 'api': api/migrations/0001_initial.py.


**Aplicar la migración a la base de datos**:
Este comando toma todos los archivos de migración que no se han aplicado y los ejecuta contra la base de datos, creando las tablas y columnas necesarias.

Ejecuta el siguiente comando:
`python manage.py migrate`
Django aplicará no solo tu migración, sino también las migraciones iniciales de las otras apps que vienen por defecto (admin, auth, etc.).

¡Excelente! Has definido la estructura de tus datos y has creado la tabla correspondiente en la base de datos sin escribir una sola línea de SQL.

Y te preguntarás, ¿Cómo puede funcionar esto si no he creado ninguna base de datos, ni ninguna conexión, no he escrito SQL...? Muy sencillo.

En Django no necesitas crear manualmente la base de datos ni escribir SQL al principio porque Django está diseñado para abstraer y automatizar esas tareas usando su sistema de ORM (Object-Relational Mapping). Te explico por qué paso a paso:

Cuando creas un proyecto Django, en **settings.py** ya tienes configurada una base de datos por defecto:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

```
Eso significa que Django usará SQLite por defecto, que es un motor de base de datos ligero basado en archivos. Además, no necesitas instalar ni configurar un servidor de base de datos (como PostgreSQL o MySQL) al principio. Cuando ejecutas python manage.py migrate, Django crea el archivo db.sqlite3 automáticamente.

Ahora mismo estamos trabajando en un proyecto muy pequeño, por lo que no es necesario configurar otro servidor de base de datos, pero lo suyo es usar PostsgreSQL o MySQL, más grandes y potentes. 

Te dejo por aquí la forma de configurar una base de datos más grande por si te interesa:
#### Configuración de PostrgeSQL en lugar de SQLite
- Instala el conector de PostgreSQL
Primero, necesitas instalar el paquete que permite a Django conectarse con PostgreSQL:
`pip install psycopg2-binary
`
- Crea la base de datos en PostgreSQL
Abre psql o tu gestor favorito y ejecuta:


    CREATE DATABASE midb;
    CREATE USER miusuario WITH PASSWORD 'miclave';
    ALTER ROLE miusuario SET client_encoding TO 'utf8';
    ALTER ROLE miusuario SET default_transaction_isolation TO 'read committed';
    ALTER ROLE miusuario SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE midb TO miusuario;
    

- Configura settings.py de Django
Abre el archivo settings.py de tu proyecto y busca esta sección:


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / "db.sqlite3",
        }
    }
    
Reemplázala por:


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'midb',
            'USER': 'miusuario',
            'PASSWORD': 'miclave',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    
- Ejecuta migraciones
Una vez configurado, ejecuta los siguientes comandos:
`python manage.py makemigrations`
`python manage.py migrate`
Esto creará todas las tablas en la base de datos PostgreSQL que configuraste.

- Verifica que funciona
`python manage.py runserver
`
### 2.4. Panel de Administrador de Django

