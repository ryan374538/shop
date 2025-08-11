#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker

#username="root"
#password="2480"
#database="users"

#path=f"mysql+pymysql://{username}:{password}@localhost/{database}"

#engine=create_engine(path)

#SessionLocal = sessionmaker(bind=engine)

#session=SessionLocal()
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Get the full database URL from an environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Ensure URL uses psycopg2 driver if needed
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
   DATABASE_URL = f"postgresql://shop_system_user:bpNjv98mRwG4E7XPcQeoyVvmCBbIz61W@dpg-d2av1rfdiees73e7ddh0-a.oregon-postgres.render.com:5432/shop_system"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


hostname :dpg-d2cs7opr0fns73e8d21g-a
port:5432
database:shop_system_7dma
username:shop_system_7dma_user
password:fduDNgbk9ZaX0KyPd3HwyK6G6OjgTmQK
external link:fduDNgbk9ZaX0KyPd3HwyK6G6OjgTmQK
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define your database URL from Render
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://shop_system_7dma_user:fduDNgbk9ZaX0KyPd3HwyK6G6OjgTmQK@dpg-d2cs7opr0fns73e8d21g-a.oregon-postgres.render.com:5432/shop_system_7dma")

# Create an engine to connect to the PostgreSQL database
engine = create_engine(DATABASE_URL)

# Create a session maker
SessionLocal = sessionmaker(bind=engine)

# Instantiate the session
session = SessionLocal()

# Optional: Verify the connection
try:
    with engine.connect() as connection:
        print("Connection to the database was successful!")
except Exception as e:
    print("Error connecting to the database:", e)