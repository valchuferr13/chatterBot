# **CHATTERBOT**

## Introducción

La API de chatbot simple es un proyecto desarrollado en Python v3.7 que permite interactuar con un chatbot básico. La API es capaz de recibir mensajes de saludo de los usuarios y proporcionar una respuesta genérica para mensajes no reconocidos.

El objetivo de este proyecto es brindar una base para la implementación de un chatbot que pueda manejar interacciones básicas con los usuarios. La API está diseñada para ser escalable y capaz de manejar múltiples solicitudes simultáneas, lo que permite su integración en sistemas más grandes.

La API de chatbot se ha implementado en Python, aprovechando su facilidad de uso y amplia disponibilidad de bibliotecas y herramientas. Además, se han incluido pruebas unitarias básicas para verificar el correcto funcionamiento de los saludos y las respuestas predeterminadas.

## Instrucciones para utilizar la API de chatbot

La API de chatbot simple es fácil de usar y se puede integrar en otros sistemas para interactuar con un chatbot básico. Sigue los siguientes pasos para comenzar a utilizarla:

### Requisitos previos
Asegúrate de tener instalado lo siguiente antes de comenzar:
- Python 3.7 instalado en tu sistema.
- Un entorno virtual (opcional pero recomendado) para aislar las dependencias del proyecto.
- Instalar las librerias del archivo requirements.txt

#### Paso 1: Configuración del entorno
1. Clona o descarga el repositorio de la API de chatbot desde [enlace del repositorio].

2. Navega hasta la carpeta raíz del proyecto en tu terminal.

3. Opcional: Crea y activa un entorno virtual para el proyecto:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

4. Instala las dependencias necesarias ejecutando el siguiente comando:
   ```bash
   pip install -r requirements.txt
   ```

#### Paso 2: Ejecutar la API de chatbot
1. En la carpeta raíz del proyecto, ejecuta el siguiente comando para iniciar la API:
   ```bash
   python chatbot_api.py
   ```

2. La API se ejecutará localmente en `http://localhost:5000`. Puedes acceder a ella utilizando tu navegador web o herramientas como Postman.

#### Paso 3: Interactuar con el chatbot
1. Envía una solicitud POST a la siguiente URL: `http://localhost:5000/chatbot`.

2. Incluye un cuerpo JSON con el siguiente formato:
   ```json
   {
     "message": "Hola"
   }
   ```

3. El campo `message` debe contener el mensaje que deseas enviar al chatbot. Puedes enviar diferentes mensajes para probar su funcionalidad.

4. La API responderá con una respuesta JSON que contiene el mensaje de respuesta del chatbot:
   ```json
   {
     "response": "¡Hola! ¿En qué puedo ayudarte?"
   }
   ```

#### Paso 4: Pruebas unitarias
Se han incluido pruebas unitarias básicas para verificar el funcionamiento correcto de la API de chatbot. Puedes ejecutar estas pruebas utilizando el siguiente comando:
```bash
python -m unittest chatBotTestCase.py
```

Las pruebas se ejecutarán y te mostrarán los resultados en la terminal. Asegúrate de que todas las pruebas pasen sin errores.

## Links de interés
Para este proyecto se utilizaron los siguientes recursos:

[Documentación Flask](https://flask-es.readthedocs.io/)
[IA Wolverine para debuggear el proyecto](https://github.com/biobootloader/wolverine)