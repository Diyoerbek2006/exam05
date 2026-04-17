from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

DATABASE_URL = f"sqlite:///./{settings.DB_NAME}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLite uchun kerak
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()