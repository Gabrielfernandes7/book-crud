from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_DATABASE = "mysql+mysqlconnector://root:Password123&PythonSQL@localhost:3306/userdb"
# URL_DATABASE = "postgresql://postgres:Password123890@localhost:5432/userdb"

engine = create_engine(
    URL_DATABASE,
    pool_size = 10,
    max_overflow= 30
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
