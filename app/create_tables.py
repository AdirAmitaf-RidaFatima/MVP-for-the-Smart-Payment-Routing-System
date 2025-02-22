from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import DATABASE_URL
from app.models import Base

engine = create_engine("DATABASE_URL")
Base.metadata.create_all(bind=engine)
