from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./homework.db"
# for github (postgresql)
#host=> ep-red-dawn-83306951.us-east-1.postgres.vercel-storage.com
#user=> default
#password=> 8RUjDA7dBQoC
#database=> verceldb
# SQLALCHEMY_DATABASE_URL = "postgresql://default:8RUjDA7dBQoC@ep-red-dawn-83306951.us-east-1.postgres.vercel-storage.com:5432/verceldb"

#with docker yml
#postgresql://${{POSTGRES_USER}}:${{POSTGRES_PASSWORD}}@${{hostname}}:${{ports}}/${{POSTGRES_DB}}
SQLALCHEMY_DATABASE_URL = "postgresql://ntue:ntuedtd@db:5432/ntue"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()