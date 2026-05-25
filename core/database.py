
# Importo os para poder leer variables de entorno
import os

# Importo load_dotenv para cargar el archivo .env
from dotenv import load_dotenv

# Importo create_engine para crear la conexión con la base de datos
from sqlalchemy import create_engine

# Importo declarative_base para crear los modelos de la base de datos
from sqlalchemy.ext.declarative import declarative_base

# Importo sessionmaker para manejar sesiones con la base de datos
from sqlalchemy.orm import sessionmaker


# Cargo las variables del archivo .env
load_dotenv()


# Obtengo el usuario de la base de datos desde el .env
DB_USER = os.getenv("DB_USER")

# Obtengo la contraseña
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Obtengo el host
DB_HOST = os.getenv("DB_HOST")

# Obtengo el puerto
DB_PORT = os.getenv("DB_PORT")

# Obtengo el nombre de la base de datos
DB_NAME = os.getenv("DB_NAME")


# Construyo la URL de conexión a MySQL
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# Creo la conexión principal con la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# Creo una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Creo una clase base para los modelos
Base = declarative_base()


# Creo una función para abrir y cerrar sesiones de base de datos
def get_db():

    # Inicio una sesión
    db = SessionLocal()

    try:
        # Entrego la sesión para usarla en otros archivos
        yield db

    finally:
        # Cierro la sesión cuando termina
        db.close()