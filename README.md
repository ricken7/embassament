# Flask Embassaments Project

Este proyecto es una aplicación web desarrollada con Flask que permite obtener datos sobre embalses y calcular el porcentaje global de volumen embalsado.

## Estructura del Proyecto

```
flask-app
├── src
│   ├── embassaments.py  # Lógica principal de la aplicación Flask
├── requirements.txt      # Dependencias necesarias
├── Procfile              # Instrucciones para Heroku
└── README.md             # Documentación del proyecto
```

## Requisitos

Asegúrate de tener Python y pip instalados en tu máquina. Este proyecto requiere las siguientes dependencias:

- Flask
- requests

## Instalación

1. Clona el repositorio:

   ```
   git clone <URL_DEL_REPOSITORIO>
   cd flask-app
   ```

2. Crea un entorno virtual (opcional pero recomendado):

   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:

   ```
   pip install -r requirements.txt
   ```

## Ejecución Local

Para ejecutar la aplicación localmente, utiliza el siguiente comando:

```
python src/embassaments.py
```

La aplicación estará disponible en `http://127.0.0.1:5000`.

## Despliegue en Heroku

Para desplegar la aplicación en Heroku, sigue estos pasos:

1. Asegúrate de tener la CLI de Heroku instalada y autenticada.
2. Crea una nueva aplicación en Heroku:

   ```
   heroku create nombre-de-tu-aplicacion
   ```

3. Despliega tu aplicación:

   ```
   git push heroku master
   ```

4. Abre la aplicación en el navegador:

   ```
   heroku open
   ```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.