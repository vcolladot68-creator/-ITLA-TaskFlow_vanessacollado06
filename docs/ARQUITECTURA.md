\# Arquitectura del sistema ITLA TaskFlow



\## 1. Introducción



ITLA TaskFlow es una aplicación web desarrollada para facilitar la administración de tareas y proyectos.



El sistema utiliza una arquitectura organizada por componentes para separar las responsabilidades de cada parte de la aplicación.



\## 2. Tecnologías utilizadas



\- Python: lenguaje principal de programación.

\- Flask: framework para desarrollar la aplicación web.

\- MySQL: sistema de gestión de base de datos.

\- SQLAlchemy: herramienta para interactuar con la base de datos.

\- HTML: estructura de las páginas.

\- CSS: presentación visual.

\- Bootstrap: diseño adaptable de la interfaz.

\- Git y GitHub: control de versiones y colaboración.



\## 3. Componentes principales



\### Capa de presentación

Se encarga de mostrar las páginas y formularios con los que interactúa el usuario.



\### Capa de rutas

Recibe las solicitudes del navegador y determina las operaciones que debe ejecutar la aplicación.



\### Capa de modelos

Representa las entidades del sistema y permite gestionar la información almacenada en MySQL.



\### Capa de autenticación

Gestiona el registro, inicio y cierre de sesión de los usuarios.



\### Capa de persistencia

Permite almacenar, consultar, actualizar y eliminar información en la base de datos.



\## 4. Funcionamiento general



1\. El usuario accede a la aplicación desde el navegador.

2\. Flask recibe la solicitud mediante una ruta.

3\. La aplicación procesa la solicitud.

4\. Cuando es necesario, se consulta o modifica la base de datos.

5\. Se genera una respuesta para el usuario.

6\. El navegador muestra el resultado.



\## 5. Organización del proyecto



El proyecto utiliza una estructura modular para separar sus componentes:



\- app: contiene los componentes principales de Flask.

\- models: contiene los modelos de datos.

\- routes: organiza las rutas de la aplicación.

\- templates: contiene las plantillas HTML.

\- static: almacena los recursos estáticos.

\- tests: contiene documentación y recursos relacionados con las pruebas.

\- docs: contiene la documentación técnica.



\## 6. Gestión de datos



MySQL almacena la información necesaria para el funcionamiento del sistema, incluyendo los datos relacionados con usuarios, proyectos y tareas.



SQLAlchemy facilita las operaciones de acceso y manipulación de datos.



\## 7. Control de versiones



El desarrollo utiliza Git Flow para organizar el trabajo mediante las ramas main, developer, qa, feature y hotfix.



\## 8. Conclusión



La arquitectura de ITLA TaskFlow permite organizar el código, separar responsabilidades y facilitar el mantenimiento y crecimiento de la aplicación.

