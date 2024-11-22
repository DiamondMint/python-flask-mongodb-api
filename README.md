# Python evaluation

El propósito de este proyecto es crear una API interna que realice una solicitud GET a la API pública "Dog CEO" para obtener una imagen aleatoria de un perro, basada en la raza proporcionada por el usuario. Este proyecto facilita la integración con la API "Dog CEO" y permite a los usuarios obtener imágenes de perros específicos de manera eficiente y sencilla.

El resultado de esta tarea es una función que, al recibir un nombre de raza de perro, hace una solicitud a la API "Dog CEO" y devuelve un objeto JSON con la URL de una imagen aleatoria de un perro de esa raza. Esto permite a los usuarios recibir instantáneamente imágenes de perros de la raza deseada, mejorando la funcionalidad y la interactividad de la aplicación.

## Tabla de Contenidos
- [Instalación](#instalación)
  1. Configurar el entorno
    - Instalar las Bibliotecas necesarias:
      - flask==3.1.0(para crear la API)
        - import render_template (para que flask pueda reconocer que ahi tengo los archivos que quiero renderizar)
        - import Flask (constructor)
        - import Blueprint (para crear las rutas a mi API)
        - import request
        - import Response
      - Flask-PyMongo==2.3.0
      - Flask-RESTful==0.3.10
      - pymongo==4.10.1
      - pytest==8.3.3
      - pytest-mongo==3.1.0
      - datetime
        - import date 
      - bson
        -  import json_util 
      - python-dotenv==1.0.1 (me va a permitir acceder a variables de ambiente)
        - import dot_env
        - load_dotenv (lo mandamos a llamar para poder usar la variable de ambiente)
        - import os
        - import requests
        - import json
          
  2. Configurar MongoDB: Asegúrate de tener una instancia de MongoDB en funcionamiento. Puedes usar una instancia local o un servicio en la nube como MongoDB Atlas.
     Esto es para que cuando nosotros usemos cada endpoint de la aplicación se registren, consulten, etc. todos los datos.

  3. Creamos un archivo llamado .gitignore para ignorar el .env y asaí este archivo no se va a subir al repositorio.

- [Uso](#uso)
  4. Crear el Wrapper de la API con Flask.
     - Configura una aplicación Flask que maneje las solicitudes GET, interactúe con la API de "Dog CEO" y almacene los resultados en MongoDB.
     - Implementa la lógica para almacenar los resultados en una base de datos MongoDB.
  5. Pruebas unitarias con Pytest
     - Crea casos de prueba usando pytest para verificar que la API funciona correctamente y maneja adecuadamente tanto las solicitudes válidas como las inválidas.
     - EEjecuta las pruebas utilizando pytest para asegurarte de que tu API responde correctamente y que todas las funcionalidades están cubiertas.        
  
- [Características](#características)
  - Wrapper Seguro de API: Envuelve la API pública "Dog CEO" para ofrecer una interfaz segura y simplificada.
  - Búsqueda por Raza: Permite a los usuarios obtener imágenes aleatorias de perros específicos según la raza proporcionada.
  - Integración con MongoDB: Almacena las respuestas de la API en una base de datos MongoDB para futuras referencias y análisis.
  - Manejo de Errores: Implementa un manejo robusto de errores para asegurar respuestas claras en caso de fallas en la solicitud.
  - Fácil de Configurar: Proceso de instalación sencillo con instrucciones claras para clonar el repositorio, instalar dependencias y configurar el entorno.
  - Pruebas Unitarias: Incluye pruebas unitarias escritas con pytest para asegurar que todas las funcionalidades del API funcionan correctamente.
  - Desarrollo Local: Configurado para un desarrollo local fácil con un servidor Flask en modo debug para pruebas y desarrollo.

Documentación Completa: Incluye documentación detallada sobre la instalación, uso, y contribución al proyecto.
- [Contribuir](#contribuir)
  - Hacer un fork del proyecto
  - Crear una rama con la nueva característica (git checkout -b nueva-caracteristica)
  - Hacer commit de los cambios (git commit -m 'Añadir nueva característica')
  - Hacer push a la rama (git push origin nueva-caracteristica)
  - Crear un Pull Request
    
- [Créditos](#créditos)
  - **API Pública "Dog CEO"**
  - *Descripción*: Una API pública que proporciona imágenes aleatorias de perros basadas en la raza.
  - *Enlace*: [Dog CEO API](https://dog.ceo/dog-api/)
- **Bibliotecas de Python**
  -  **Flask**
    - *Descripción*: Un microframework para Python que facilita la creación de aplicaciones web y APIs.
    -  *Enlace*: [Flask](https://flask.palletsprojects.com/)
  - *Requests**
  -  *Descripción*: Una biblioteca para realizar solicitudes HTTP de manera sencilla.
  -   *Enlace*: [Requests](https://requests.readthedocs.io/)
- **PyMongo**
  -  *Descripción*: Una biblioteca para interactuar con MongoDB desde Python.
  -   *Enlace*: [PyMongo](https://pymongo.readthedocs.io/)
- **Pytest**
  -  *Descripción*: Una biblioteca para escribir y ejecutar pruebas en Python.
  - *Enlace*: [Pytest](https://pytest.org/)
- [Licencia](#licencia)

## Instalación

Instrucciones paso a paso sobre cómo instalar el proyecto.

```bash
# Clonar el repositorio
git clone https://github.com/DiamondMint/python-flask-mongodb-api

# Entrar en el directorio del proyecto

# Crear un entorno virtual (opcional)
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
