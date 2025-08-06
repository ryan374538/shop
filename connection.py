from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username="root"
password="2480"
database="users"

path=f"mysql+pymysql://{username}:{password}@localhost/{database}"

engine=create_engine(path)

SessionLocal = sessionmaker(bind=engine)

session=SessionLocal()