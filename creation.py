"""
from models import Base
from connection import engine
Base.metadata.create_all(bind=engine)
"""
from models import Base, Admins  
from connection import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

admin_exists = session.query(Admins).filter_by(username='admin').first()

if not admin_exists:
    admin_user = Admins(
        username='admin',
        password='2340',  
        firstname='Admin',
        secondname='User',
        email='admin@example.com'
    )
    session.add(admin_user)
    session.commit()

session.close()
