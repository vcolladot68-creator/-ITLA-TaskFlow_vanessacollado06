\# Guía de contribución

\## Proyecto ITLA TaskFlow



\### 1. Introducción



Este documento establece las pautas que deben seguir los colaboradores que deseen participar en el desarrollo y mantenimiento de ITLA TaskFlow.



El objetivo es mantener un proceso de trabajo organizado, facilitar la colaboración y asegurar la calidad del código.



\### 2. Preparación del entorno



Antes de comenzar a colaborar, se recomienda:



\- Tener Git instalado.

\- Contar con Python y MySQL configurados.

\- Clonar el repositorio oficial.

\- Crear y activar un entorno virtual.

\- Instalar las dependencias del archivo requirements.txt.

\- Configurar las variables de entorno necesarias.



\### 3. Organización de ramas



El proyecto utiliza Git Flow para organizar el desarrollo:



\- main: contiene la versión principal y estable del proyecto.

\- developer: concentra el desarrollo de nuevas funcionalidades.

\- qa: permite integrar y revisar los cambios antes de su publicación.

\- feature: se utiliza para desarrollar funcionalidades o mejoras específicas.

\- hotfix: se utiliza para preparar correcciones urgentes.



\### 4. Creación de ramas



Cada nueva funcionalidad debe desarrollarse en una rama independiente.



Ejemplo:



&#x20;   git checkout developer

&#x20;   git pull origin developer

&#x20;   git checkout -b feature/nombre-funcionalidad



Se recomienda utilizar nombres claros y relacionados con el cambio que se realizará.



\### 5. Convenciones para commits



Los mensajes de commit deben describir brevemente los cambios realizados.



Se recomienda utilizar convenciones como:



\- feat: nueva funcionalidad.

\- fix: corrección de errores.

\- docs: cambios en la documentación.

\- test: incorporación o modificación de pruebas.

\- refactor: reorganización del código sin cambiar su comportamiento.



Ejemplo:



&#x20;   git commit -m "docs: actualizar guia de contribucion"



\### 6. Pull Requests



Los cambios deben compartirse mediante Pull Requests.



Cada Pull Request debe:



\- Tener un título claro.

\- Explicar el objetivo del cambio.

\- Describir los archivos modificados.

\- Indicar las verificaciones realizadas.

\- Dirigirse a la rama correspondiente.

\- Ser revisado antes de su integración.



\### 7. Buenas prácticas de desarrollo



\- Mantener el código organizado y legible.

\- Evitar duplicar funcionalidades.

\- Validar los datos recibidos.

\- No publicar contraseñas ni credenciales.

\- Mantener actualizada la documentación.

\- Realizar cambios pequeños y específicos.

\- Verificar que las funcionalidades existentes continúen trabajando.



\### 8. Proceso de integración



El flujo general de trabajo consiste en:



1\. Crear una rama para el cambio.

2\. Implementar la modificación.

3\. Realizar las verificaciones correspondientes.

4\. Crear un Pull Request.

5\. Revisar los cambios.

6\. Integrar la modificación en la rama de destino.

7\. Continuar con el proceso de pruebas y liberación.



\### 9. Conclusión



Seguir estas pautas permite mantener un historial de cambios organizado, mejorar la colaboración entre desarrolladores y facilitar el mantenimiento de ITLA TaskFlow.

