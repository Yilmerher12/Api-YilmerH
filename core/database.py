# importamos de la libreria que va actuar como ORM en nuestro proyecto, herramientas como 'create_engine' y 'sessionmaker' que nos ayudan a establecer la conexión con la base de datos y gestionar las sesiones de trabajo.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Es la URL de nuestra base de datos, con el motor, usuario, contraseña, host, puerto y nombre de la base de datos.
URL_BASE_DATOS = "postgresql://postgres:12345@localhost:5432/mi_base_datos"

# Se usa la herramienta 'create_engine' para establecer la conexión con la base de datos utilizando la URL proporcionada.
## inicia sesion una vez cuando prendo el servidor, abre multiples conexiones al motor cada vez que se necesite interactuar con la base de datos.
engine = create_engine(URL_BASE_DATOS)

# se usa la herramienta 'sessionmaker' para crear una clase de sesión personalizada que está vinculada al 'engine' que acabamos de crear. 
# utiliza el motor 'engine' y solo fabrica una sesion conectada a ese engine
SessionLocal = sessionmaker(bind=engine)