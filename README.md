# ITLA TaskFlow



Sistema web de gestión de tareas y proyectos desarrollado con Flask y MySQL como proyecto académico para practicar Git y Git Flow en ITLA.



## Descripción



ITLA TaskFlow permite organizar tareas, administrar proyectos y dar seguimiento al progreso de las actividades desde una interfaz web.



## Funcionalidades



- Registro e inicio de sesión de usuarios.

- Panel principal con información de las tareas.

- Creación, consulta, actualización y eliminación de tareas (CRUD).

- Organización de tareas por proyectos y categorías.

- Asignación de prioridades.

- Control del estado de las tareas.

- Búsqueda y filtros por estado y prioridad.

- Validación de formularios.

- Protección de rutas mediante autenticación.



## Tecnologías utilizadas



- Python 3

- Flask

- MySQL 8.0

- SQLAlchemy

- Flask-Migrate

- Flask-Login

- Flask-WTF

- Flask-Bcrypt

- Bootstrap 5

- HTML, CSS y JavaScript

- Docker Compose

- Pytest



## Requisitos previos



- Python 3 instalado.

- Git instalado.

- Docker Desktop con Docker Compose.



## Instalación y configuración



### 1. Clonar el repositorio



       git clone https://github.com/vcolladot68-creator/-ITLA-TaskFlow_vanessacollado06.git

       cd -ITLA-TaskFlow_vanessacollado06



### 2. Crear el entorno virtual



       python -m venv venv

       .\venv\Scripts\Activate.ps1



### 3. Instalar dependencias



       pip install -r requirements.txt



### 4. Configurar variables de entorno



       Copy-Item .env.example .env



Editar el archivo `.env` y establecer contraseñas seguras y una clave secreta propia. No subir este archivo a GitHub.



### 5. Iniciar MySQL



       docker compose up -d



### 6. Aplicar migraciones



       flask db upgrade



### 7. Ejecutar la aplicación



       python run.py



Abrir en el navegador:



http://127.0.0.1:5000



## Estructura del proyecto



- `app/`: aplicación Flask, rutas, modelos, plantillas y archivos estáticos.

- `database/`: archivos relacionados con la base de datos.

- `migrations/`: migraciones de la base de datos.

- `tests/`: pruebas automatizadas.

- `.env.example`: plantilla de variables de entorno.

- `docker-compose.yml`: configuración del servicio MySQL.

- `requirements.txt`: dependencias del proyecto.

- `run.py`: punto de entrada de la aplicación.



## Flujo de trabajo Git Flow



- `main`: versión principal y estable.

- `developer`: integración de funcionalidades.

- `qa`: revisión y validación de cambios.

- `feature/`: desarrollo de nuevas funcionalidades.

- `hotfix/`: correcciones urgentes.



Los cambios se desarrollan en ramas independientes y se integran mediante Pull Requests.



## Pruebas



Para ejecutar las pruebas automatizadas:



       pytest



## Seguridad



- Las credenciales se configuran mediante variables de entorno.

- El archivo `.env` no debe subirse al repositorio.

- Se proporciona `.env.example` como plantilla.



## Autora



Proyecto académico desarrollado para la asignatura de Git y Git Flow.



**ITLA - Instituto Tecnológico de las Américas**

