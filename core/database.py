import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Cargo las variables del archivo .env
load_dotenv()


# Obtengo el usuario de la base de datos desde el .env
DB_USER = os.getenv("DB_USER")
# Obtengo la contraseña
DB_PASSWORD = os.getenv("DB_PASSWORD", "Yilmerher12_")
# Obtengo el host
DB_HOST = os.getenv("DB_HOST", "localhost")
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Cargo las variables del archivo .env (si existe)
load_dotenv()


# Obtengo las variables de entorno (pueden ser None)
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")


# Si no están configuradas las credenciales básicas, no creamos el engine
if DB_USER and DB_NAME:
    SQLALCHEMY_DATABASE_URL = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Creo la conexión principal con la base de datos
    engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

    # Creo una sesión para interactuar con la base de datos
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
else:
    engine = None
    SessionLocal = None


# Creo una clase base para los modelos
Base = declarative_base()


# Creo una función para abrir y cerrar sesiones de base de datos
def get_db():
    """Dependencia de FastAPI que retorna una sesión de DB.

    Si la conexión no fue configurada (SessionLocal es None), lanza RuntimeError
    para indicar que la base de datos no está configurada.
    """
    if SessionLocal is None:
        raise RuntimeError("Base de datos no configurada. Defina DB_USER/DB_PASSWORD/DB_NAME en .env o configure core.database")

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()