from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configurações do banco de dados
DB_USER = "root"
DB_PASSWORD = "Password123890"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "pizzadb"

# Criar a URL do banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criar uma instância do engine SQLAlchemy
engine = create_engine(DATABASE_URL)

# Conexão com o banco de dados
connection = engine.connect()

# Criar uma sessão de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar uma instância da classe base declarativa
Base = declarative_base()
