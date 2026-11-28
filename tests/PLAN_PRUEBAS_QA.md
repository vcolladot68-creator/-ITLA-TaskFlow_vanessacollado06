# Plan de pruebas de ITLA TaskFlow

## Objetivo
Verificar que las funcionalidades principales de ITLA TaskFlow funcionen correctamente antes de integrar los cambios en la rama principal.

## Alcance
- Registro e inicio de sesión.
- Acceso al panel principal.
- Creación de tareas.
- Consulta de tareas.
- Actualización de tareas.
- Eliminación de tareas.
- Búsqueda y filtros.
- Validación de formularios.
- Protección de rutas privadas.
- Conexión con MySQL.

## Casos de prueba

| ID | Prueba | Resultado esperado |
|---|---|---|
| QA-01 | Registrar un usuario | Usuario registrado correctamente |
| QA-02 | Iniciar sesión | Acceso al panel principal |
| QA-03 | Crear una tarea | Tarea guardada en la base de datos |
| QA-04 | Consultar tareas | Se muestran las tareas del usuario |
| QA-05 | Editar una tarea | Se guardan los cambios |
| QA-06 | Eliminar una tarea | La tarea deja de aparecer |
| QA-07 | Buscar una tarea | Se muestran coincidencias |
| QA-08 | Filtrar por estado | Se muestran tareas del estado seleccionado |
| QA-09 | Enviar formulario inválido | Se muestran mensajes de validación |
| QA-10 | Acceder sin autenticación | Se solicita iniciar sesión |

## Criterios de aceptación
- Las operaciones CRUD deben ejecutarse correctamente.
- Los formularios deben validar los datos.
- Cada usuario debe acceder únicamente a sus propios registros.
- La aplicación debe mantener la conexión con MySQL.
- No deben existir errores que impidan utilizar las funciones principales.

## Observaciones
Los resultados de cada prueba deben registrarse durante la ejecución de las pruebas de calidad.
