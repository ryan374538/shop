"""
from models import Base
from connection import engine
Base.metadata.create_all(bind=engine)
"""
from werkzeug.security import generate_password_hash
from models import Users
from connection import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

admin_exists = session.query(Users).filter_by(username='admin').first()

if not admin_exists:
    hashed_password = generate_password_hash('2340')
    admin_user = Users(
        username='admin',
        password=hashed_password,
        firstname='Admin',
        secondname='User',
        email='admin@example.com'
    )
    session.add(admin_user)
    session.commit()

session.close()

