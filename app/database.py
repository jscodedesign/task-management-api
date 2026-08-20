from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://postgres:5428154281@localhost/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)