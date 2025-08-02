# Proyecto Urban Grocers 
### Proyecto Sprint 7 QA Grupo 34

##### El objetivo es automatizar las pruebas de una lista de comprobación, cargar el código en GitHub y enviar el repositorio a revisión.

###### Descripción del proyecto:

- Se hace comprobación de cómo la aplicación **"Urban Grocers"** crea kits de productos.
- Una de ellas es para el campo "name" en la solicitud de creación de un kit de productos...;
- Se clona el repositorio del proyecto desde Github hacia el equipo local.;
- Se trabaja de forma local el proyecto **"qa-project-Urban-Grocers-app-es"**;
- Creación de un kit para el usuario o usuarias;
- Ejemplo de la lista de comprobación utilizada:
№   		Description	 	 ER:
1	El número permitido de caracteres (1): kit_body = { "name": "a"}	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

#### Rutas (Endpoinst) almacenados en "configuration.py"
##### Los cuerpos de la solicitud POST estan en el archivo "data.py"

La lista de comprobación completa se encuentra en el archivo "create_kit_name_kit_test.py"

#### Fuente de la documentación: [https://cnt-0be6a661-4072-454c-b5ae-640455ac56af.containerhub.tripleten-services.com/docs/]

Ejemplos de codigos utilizados:

####Código Agregar Usuario con token


    def get_new_user_token():
		response = sender_stand_request.post_new_user(data.user_body)
		 return response.json()["authToken"]
    


##### Tecnologías y Técnicas Utilizadas
Este proyecto ha sido desarrollado predominantemente con Python y sus librerías/frameworks asociados. 
A continuación, se detallan las principales tecnologías y enfoques utilizados:
- Lenguaje de Programación:
**Python**: Se ha utilizado la versión:

PyCharm 2025.1.3.1 (Community Edition)
Runtime version: 21.0.7+9-b895.130
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Windows 11.0

- Por sus capacidades en ["Automatización"]
- Librerias notables [Requests, Pytest]
- Repositorio [Git/Github]
- Consola "Git Bash"
- Pruebas [Pytest]


***Gracias Tripleten**

