from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import Depends
from typing import Annotated
from app.database.connection import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]