# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Random Forest para Predicción de Tasas de la FED en niveles
- **Plataforma de despliegue:** Google Colab con FastAPI y ngrok
- **Requisitos técnicos:**
  - Python 3.7 o superior
  - Bibliotecas: scikit-learn, Keras, TensorFlow, numpy, pandas, matplotlib, fastapi, uvicorn, pyngrok, joblib
- **Requisitos de seguridad:**
  - Comunicación segura a través de HTTPS proporcionada por ngrok


## Código de despliegue

- **Archivo principal:** El código del despliegue se encuentra en el cuaderno de colab
- **Rutas de acceso a los archivos:** Los archivos del modelo y los datos están almacenados temporalmente en el entorno de ejecución de Colab
- **Variables de entorno:** No se requieren para el despliegue en Colab

## Documentación del despliegue

- **Instrucciones de instalación:**
  - Abrir el cuaderno en Google Colab
  - Ejecutar todas las celdas para instalar las dependencias y entrenar el modelo

- **Instrucciones de configuración:**
  - Configurar el endpoint de FastAPI en una celda del cuaderno
  - Iniciar ngrok para exponer el endpoint de FastAPI a internet

- **Instrucciones de uso:**
  - Utilizar la URL pública generada por ngrok para enviar solicitudes POST al endpoint `/predict`
  - La solicitud debe contener datos en el formato JSON con una clave "features" que contiene los datos de entrada para el modelo

- **Instrucciones de mantenimiento:**
  - Monitorizar y reiniciar el cuaderno en Colab si la sesión expira
  - Actualizar las dependencias cuando sea necesario
