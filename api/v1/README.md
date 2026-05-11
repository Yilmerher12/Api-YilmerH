# Agregador de Rutas (V1)

Este directorio constituye la capa de orquestación para la versión 1 de la API.

Su función principal es centralizar todos los módulos de endpoints independientes en un único objeto de enrutamiento.

---

# Propósito Técnico

En una arquitectura escalable, no es eficiente registrar cada controlador directamente en el punto de entrada (`main.py`).

Este archivo actúa como un **HUB** o concentrador que utiliza la clase `APIRouter` de FastAPI para agrupar funcionalidades.

---

# Componentes Clave

## `api_router`

Instancia maestra de `APIRouter` que encapsula todas las sub-rutas de la versión 1.

---

## `include_router`

Método encargado de inyectar los routers específicos (`productos`, `usuarios`, etc.) dentro del agregador principal.

---

# Parámetros de Configuración

Al incluir routers hijos, se aplican dos configuraciones críticas.

## `prefix`

Define el prefijo de nivel secundario en la URL.

### Ejemplo

```python
prefix="/users"
```

Sumado al prefijo definido en `main.py`, construye la ruta completa:

```bash
/api/v1/users
```

---

## `tags`

Organiza y agrupa visualmente los endpoints en la documentación interactiva de Swagger UI.

### Ejemplo

```python
tags=["Usuarios"]
```

---

# Flujo de Integración

## 1. Creación del Router Principal

```python
api_router = APIRouter()
```

---

## 2. Inclusión de Routers Hijos

```python
api_router.include_router(users.router, prefix="/users", tags=["Usuarios"])
```

---

## 3. Registro Global en `main.py`

```python
app.include_router(api_router, prefix="/api/v1")
```

---

# Beneficios Arquitectónicos

- Separación modular de funcionalidades.
- Escalabilidad en proyectos grandes.
- Organización limpia del código.
- Versionamiento estructurado de la API.
- Reutilización de routers independientes.
- Mejor mantenimiento y desacoplamiento.