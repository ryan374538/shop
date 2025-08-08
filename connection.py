#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker

#username="root"
#password="2480"
#database="users"

#path=f"mysql+pymysql://{username}:{password}@localhost/{database}"

#engine=create_engine(path)

#SessionLocal = sessionmaker(bind=engine)

#session=SessionLocal()

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Get the full database URL from an environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Ensure URL uses psycopg2 driver if needed
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg2://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
