# Capa de Endpoints (Controllers)

Este directorio contiene la lógica operativa de la API.

Cada archivo dentro de esta carpeta representa un módulo de negocio específico y es responsable de gestionar las peticiones HTTP (`GET`, `POST`, `PUT`, `DELETE`).

---

# Responsabilidades Técnicas

Los archivos en este nivel no gestionan la configuración del servidor.

Su enfoque principal es:

- Definición de rutas.
- Validación de datos.
- Procesamiento de lógica.
- Gestión de respuestas HTTP.
- Manejo de excepciones.

---

# Definición de Rutas

Se utilizan decoradores de operación proporcionados por FastAPI.

## Ejemplos

```python
@router.get("/")
@router.post("/")
@router.put("/{id}")
@router.delete("/{id}")
```

Cada decorador vincula una función Python con una operación HTTP específica.

---

# Validación de Dependencias

Los endpoints integran esquemas de `Pydantic` para validar automáticamente los cuerpos de las peticiones (`Request Body`).

## Ejemplo

```python
async def crear_usuario(usuario: UserCreate):
```

FastAPI valida:

- Tipos de datos.
- Campos obligatorios.
- Restricciones definidas en el esquema.

---

# Procesamiento de Lógica

Dentro de cada endpoint se ejecuta la lógica de negocio correspondiente.

## Ejemplos

- Manipulación de datos.
- Cálculos.
- Validaciones adicionales.
- Gestión de estados.
- Búsquedas y filtrados.

---

# Gestión de Respuestas

Los endpoints retornan:

- Objetos serializados.
- Modelos de salida (`response_model`).
- Códigos HTTP adecuados.

## Ejemplo

```python
@router.get("/", response_model=list[UserOut])
```

---

# Gestión de Datos (Mock Data)

Actualmente, los módulos utilizan una Base de Datos Simulada en memoria mediante:

- Listas (`list`)
- Diccionarios (`dict`)

## Ejemplo

```python
users_db = []
```

---

# Nota Importante

La persistencia actual es completamente volátil.

Esto significa que:

- Los datos se reinician al detener el servidor.
- No existe almacenamiento permanente.

En etapas posteriores, esta capa interactuará con un ORM como:

- SQLAlchemy
- SQLModel
- Tortoise ORM

para trabajar con sistemas de bases de datos relacionales reales.

---

# Manejo de Excepciones

Se utiliza la clase `HTTPException` para gestionar flujos de error controlados.

## Beneficios

- Interrumpir la ejecución de la función.
- Retornar códigos HTTP precisos.
- Proveer respuestas JSON estructuradas.

---

# Ejemplo de Error Controlado

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="Usuario no encontrado"
)
```

---

# Estructura de un Endpoint Estándar

```python
@router.verbo("/ruta", response_model=EsquemaSalida)
async def nombre_funcion(datos_entrada: EsquemaEntrada):

    # 1. Lógica de procesamiento

    # 2. Manejo de errores (HTTPException)

    # 3. Retorno de objeto validado
```

---

# Flujo de Ejecución de un Endpoint

## 1. Recepción de la Petición

El cliente envía una solicitud HTTP.

---

## 2. Validación Automática

FastAPI y Pydantic validan los datos recibidos.

---

## 3. Ejecución de la Lógica

Se procesa la operación solicitada.

---

## 4. Retorno de Respuesta

El servidor devuelve:

- Datos serializados.
- Código HTTP correspondiente.
- Mensajes de error si existen.

---

# Beneficios Arquitectónicos

- Modularidad.
- Separación de responsabilidades.
- Escalabilidad.
- Validación automática.
- Mantenimiento simplificado.
- Integración sencilla con bases de datos futuras.