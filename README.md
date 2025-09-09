# Sentilo ACA Embassaments API

Una aplicación Flask containerizada con Docker que proporciona datos sobre embalses de la ACA (Agència Catalana de l'Aigua) a través de la API de Sentilo.

## 🚀 Características

- **API REST** para consultar datos de embalses
- **Dockerizado** para fácil despliegue
- **Datos en tiempo real** desde la API de Sentilo ACA
- **Endpoints optimizados** para consultas específicas

## 📁 Estructura del Proyecto

```
sentilo-aca/
├── src/
│   └── embassaments.py      # Aplicación Flask principal
├── docs/                    # Documentación
├── requirements.txt         # Dependencias Python
├── Dockerfile              # Configuración Docker
├── docker-compose.yml      # Orquestación de contenedores
├── .dockerignore           # Archivos excluidos del build
└── README.md               # Este archivo
```

## 🛠️ Requisitos

- **Docker** y **Docker Compose** instalados
- Acceso a internet para consultar la API de Sentilo

## 🚀 Inicio Rápido

### Usando Docker Compose (Recomendado)

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/ricken7/embassament.git
   cd embassament
   ```

2. **Ejecuta la aplicación:**
   ```bash
   docker-compose up
   ```

3. **Accede a la API:**
   - La aplicación estará disponible en `http://localhost:8500`

### Usando Docker directamente

1. **Construye la imagen:**
   ```bash
   docker build -t sentilo-aca .
   ```

2. **Ejecuta el contenedor:**
   ```bash
   docker run -p 8500:8500 sentilo-aca
   ```

### Ejecución local (sin Docker)

1. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecuta la aplicación:**
   ```bash
   python src/embassaments.py
   ```

## 📡 API Endpoints

### `GET /embassaments`
Obtiene datos detallados de todos los embalses.

**Respuesta:**
```json
[
  {
    "embassament": "Nombre del embalse",
    "capacitat_maxima": "X.X hm³",
    "volum_embassat_actual": 123.45,
    "fecha_hora": "2025-01-XX"
  }
]
```

### `GET /global_percentage`
Calcula el porcentaje global de llenado de todos los embalses.

**Respuesta:**
```json
{
  "global_percentage": 67.85,
  "newest_date": "2025-01-XX"
}
```

## 🐳 Comandos Docker Útiles

```bash
# Detener la aplicación
docker-compose down

# Reconstruir la imagen
docker-compose build

# Ver logs
docker-compose logs

# Ejecutar en segundo plano
docker-compose up -d
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.