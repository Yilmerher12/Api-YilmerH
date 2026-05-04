# Verde App Api - FastApi
Este proyecto es el desarrollo de una API robusta y moderna utilizando el framework ``FastAPI``. El objetivo principal es proporcionar el respaldo tecnológico para ``VerdeApp``, un proyecto enfocado en la gestión y separación de residuos sólidos dentro del ecosistema del ``SENA``.

Como aprendiz de ``ADSO``, este repositorio refleja la implementación de buenas prácticas de desarrollo, manejo de entornos virtuales y documentación automática de endpoints.

## Organización del Proyecto
Actualmente, el proyecto mantiene una estructura inicial simplificada para facilitar el aprendizaje y la configuración base:
* ``main.py:``
 Es el "cerebro" o punto de entrada de la aplicación. Aquí se importa la librería, se instancia la aplicación y se definen las rutas ``(endpoints)``
 iniciales.

* ``requirements.txt:`` Es la "lista de compras" del proyecto. Contiene todas las librerías necesarias *(con sus versiones exactas)* para que el proyecto funcione en cualquier computadora.

* ``.gitignore:`` Un archivo de seguridad que le dice a Git qué carpetas no debe subir a GitHub `(como .venv)`, evitando que el repositorio pese gigas innecesarios.

* ``.venv/:`` *(Ignorado por Git)* Es el entorno virtual. Una `"caja aislada"` donde viven las dependencias instaladas para que no choquen con otros proyectos de Python en el sistema.

## Guía de Comandos (Cheat Sheet)
Utilizar estos comandos en la terminal para gestionar el proyecto. 
**Nota:** Se utiliza el prefijo ``python -m`` para garantizar que se use la versión correcta de Python en el sistema.


1. `Preparación del Entorno:`

| Acción | **Comando (PowerShell / Bash)** |
| :--- | :---: |
| **Crear entorno virtual** | ``python -m venv .venv ``|
| **Activar (PowerShell)** | ``.\.venv\Scripts\Activate.ps1`` |
|**Activar (Git Bash)**|``source .venv/Scripts/activate``|

2. `Gestión de dependencias:`

| Acción | **Comando (PowerShell / Bash)** |
| :--- | :---: |
| **Instalar FastAPI y Servidor** | ``python -m pip install "fastapi[all]"``|
| **Generar archivo requirements** | ``python -m pip freeze > requirements.txt`` |
|**Instalar desde requirements**|``python -m pip install -r requirements.txt``|

3. ``Ejecución del servidor:``
```bash
python -m pip install "fastapi[all]"
```

## Guia de Inicio: ¿Cómo empezar?

Para asegurar que el proyecto **VerdeApp** funcione correctamente en cualquier entorno, sigue los pasos según tu situación:

### Caso A: Si vas a colaborar (Clonando este repositorio)
Utiliza estos pasos si acabas de descargar el código de GitHub en una nueva computadora para continuar el desarrollo:
1. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Yilmerher12/Api-YilmerH.git
    cd Api-YilmerH
    ```
2. **Crear el entorno virtual (Caja aislada):**
    ```bash
    python -m venv .venv
    ```
3. **Activar el entorno:**
   * **PowerShell**: ``.\.venv\Scripts\Activate.ps1``
   * **Git Bash**: ``source .venv/Scripts/activate``
    ```bash
    python -m venv .venv
    ```
4. **Instalar las librerías necesarias (desde la lista)**
   ```bash
    python -m pip install -r requirements.txt
    ```
5.  **Iniciar el servidor:**
    ```bash
    uvicorn main:app --reload
    ```



### Caso B: Si estás iniciando un proyecto nuevo desde cero
Sigue este orden lógico para configurar tu estructura inicial y mantener el orden del framework:

1.  **Crear la carpeta del proyecto y el entorno:**
    
```bash
    python -m venv .venv
```

2.  **Activar el entorno:** (Ver comandos en el Caso A según tu terminal).
3.  **Instalar FastAPI y el servidor Uvicorn:**
    ```bash
    python -m pip install fastapi uvicorn
    ```
4.  **Generar la lista de dependencias:**
    Este paso es vital para que otros puedan replicar tu trabajo:
    
    ```bash
    python -m pip freeze > requirements.txt
    ```
5.  **Desarrollar y subir:** Crea tu archivo `main.py`, configura tu `.gitignore` para excluir la carpeta `.venv/` y realiza tu primer commit.



## Documentación Interactiva (Swagger)

Una de las mayores ventajas de FastAPI es que genera la documentación técnica de forma automática. Una vez que el servidor esté corriendo, puedes acceder a ella en:

* **Swagger UI:** http://127.0.0.1:8000/docs

Aquí puedes probar tus endpoints (como el de /saludo) directamente desde el navegador sin necesidad de usar herramientas externas.

* **Redoc:** http://127.0.0.1:8000/redoc