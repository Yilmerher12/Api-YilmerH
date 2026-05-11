# Módulo de Esquemas (Pydantic Models)

Este directorio contiene las definiciones de los modelos de datos utilizados por la API para la validación, serialización y desacoplamiento de la información.

Se utiliza la librería `Pydantic` para asegurar que los datos procesados cumplan con las reglas de negocio antes de llegar a la lógica de los endpoints.

---

# Propósito Técnico

En el desarrollo de APIs, es una práctica de arquitectura separar la representación interna de los datos (Base de Datos) de la representación externa (JSON). Este patrón se conoce como **DTO (Data Transfer Object)**.

El uso de esquemas permite:

- **Validación Automática:** Verificar tipos de datos (`int`, `str`, `float`) y restricciones (`min_length`, `ge`).
- **Seguridad de la Información:** Filtrar campos sensibles (como contraseñas) para que no sean expuestos en las respuestas de la API.
- **Documentación Dinámica:** Generar automáticamente el esquema JSON que se muestra en Swagger UI (`/docs`).

---

# Estructura de los Modelos

Para cada entidad (Productos, Usuarios), se implementa una jerarquía basada en la herencia de clases.

## 1. Base Model (`EntityBase`)

Define los atributos comunes que siempre están presentes en la entidad.

- **Hereda de:** `pydantic.BaseModel`
- **Función:** Centralizar la definición de tipos básicos y reglas generales.

---

## 2. Create Model (`EntityCreate`)

Define los datos requeridos para la creación de un nuevo registro.

### Características

- Incluye campos obligatorios.
- Omite identificadores autogenerados (`id`) o fechas de sistema (`created_at`).

---

## 3. Update Model (`EntityUpdate`)

Estructura diseñada para actualizaciones parciales (`PUT` o `PATCH`).

### Características

- Utiliza el tipo `Optional[T]` para permitir que el cliente envíe solo los campos que desea modificar.

### Técnica utilizada

```python
exclude_unset=True
```

Se utiliza en la lógica del endpoint para procesar únicamente los datos enviados por el cliente.

---

## 4. Output Model (`EntityOut`)

Define la estructura de la respuesta que el cliente recibirá.

### Seguridad

- Omite explícitamente campos sensibles (ejemplo: contraseñas).

### Configuración

```python
class Config:
    from_attributes = True
```

Permite el mapeo automático desde objetos de bases de datos relacionales (ORMs).

---

# Validadores y Restricciones Utilizadas

| Atributo / Función | Descripción Técnica |
|---|---|
| `Field(..., gt=0)` | Valida que un valor numérico sea estrictamente mayor a cero. |
| `Field(..., min_length=x)` | Establece una longitud mínima obligatoria para cadenas de texto. |
| `EmailStr` | Valida que la cadena cumpla con el estándar RFC 5322 para correos electrónicos. |
| `Optional[T]` | Indica que el campo puede recibir un valor de tipo `T` o ser nulo (`None`). |
| `example` | Proporciona un valor de ejemplo para la documentación interactiva. |

---

# Flujo de Validación de Datos

## 1. Recepción

El cliente envía un JSON al servidor.

## 2. Mapeo

FastAPI intenta instanciar el modelo de Pydantic correspondiente (ejemplo: `UserCreate`) con esos datos.

## 3. Validación

Pydantic verifica:

- Tipos de datos.
- Longitudes.
- Restricciones definidas.

## 4. Ejecución

- Si la validación es exitosa, la función del endpoint recibe un objeto validado.
- Si falla, el sistema retorna automáticamente un error:

```http
422 Unprocessable Entity
```