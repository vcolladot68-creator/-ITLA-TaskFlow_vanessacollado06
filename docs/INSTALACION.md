\# Guía de instalación y configuración

\## ITLA TaskFlow



\### 1. Introducción



ITLA TaskFlow es una aplicación web desarrollada para facilitar la organización y administración de tareas y proyectos.



Esta guía describe los pasos necesarios para preparar el entorno e iniciar la aplicación localmente.



\### 2. Requisitos previos



Antes de comenzar, se recomienda tener instalados los siguientes componentes:



\- Python 3.12 o una versión compatible.

\- Git.

\- MySQL 8.0.

\- Visual Studio Code u otro editor de código.

\- Navegador web actualizado.



\### 3. Obtener el proyecto



Clonar el repositorio:



&#x20;   git clone https://github.com/vcolladot68-creator/-ITLA-TaskFlow\_vanessacollado06.git



Entrar en la carpeta:



&#x20;   cd -ITLA-TaskFlow\_vanessacollado06



\### 4. Crear el entorno virtual



Ejecutar:



&#x20;   python -m venv venv



Activar el entorno virtual en Windows PowerShell:



&#x20;   .\\venv\\Scripts\\Activate.ps1



\### 5. Instalar dependencias



Instalar las dependencias del proyecto:



&#x20;   pip install -r requirements.txt



\### 6. Configurar las variables de entorno



Crear un archivo `.env` tomando como referencia `.env.example`.



Configurar los datos de conexión a MySQL y la clave secreta de Flask.



No publicar el archivo `.env` ni compartir contraseñas reales en el repositorio.



\### 7. Preparar la base de datos



\- Verificar que el servicio MySQL esté funcionando.

\- Crear o configurar la base de datos correspondiente.

\- Revisar los parámetros de conexión definidos en el entorno.

\- Aplicar las migraciones disponibles cuando corresponda.



\### 8. Ejecutar la aplicación



Configurar Flask:



&#x20;   $env:FLASK\_APP = "run.py"



Iniciar la aplicación según la configuración del proyecto:



&#x20;   flask run



Abrir en el navegador la dirección local que indique Flask, normalmente:



&#x20;   http://127.0.0.1:5000



\### 9. Verificación



Comprobar que:



\- La aplicación inicia sin errores.

\- La página principal carga correctamente.

\- El registro de usuarios está disponible.

\- El inicio de sesión funciona.

\- Las operaciones de gestión de tareas están disponibles.

\- La conexión con MySQL funciona correctamente.



\### 10. Solución de problemas



\*\*Error de conexión con MySQL:\*\* verificar que el servicio esté activo y que las credenciales sean correctas.



\*\*Dependencias faltantes:\*\* ejecutar nuevamente `pip install -r requirements.txt`.



\*\*Problemas con el entorno virtual:\*\* comprobar que el entorno `venv` esté activado.



\*\*Error al iniciar Flask:\*\* verificar la configuración de `FLASK\_APP` y las variables de entorno.



\### 11. Consideraciones de seguridad



\- No compartir contraseñas ni claves secretas.

\- Mantener el archivo `.env` fuera del control de versiones.

\- Utilizar credenciales seguras.

\- Mantener actualizadas las dependencias.



\### 12. Conclusión



Esta guía facilita la instalación, configuración y ejecución de ITLA TaskFlow, permitiendo que otros desarrolladores puedan preparar el entorno y colaborar en el proyecto.

