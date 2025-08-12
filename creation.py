"""
from models import Base
from connection import engine
Base.metadata.create_all(bind=engine)
"""


import os
from connection import engine, SessionLocal
from models import Users ,Base

# ✅ Create tables
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")
print("Using DB file:", os.path.abspath("users"))

# ✅ Add default admin user
def add_admin_user():
    db = SessionLocal()
    try:
        existing_user = db.query(Users).filter_by(username="admin").first()
        if existing_user:
            print("ℹ️ Admin user already exists.")
        else:
            admin = Users(
                username="admin",
                password="admin123",  # You can hash this later
                role="admin"
            )
            db.add(admin)
            db.commit()
            print("✅ Admin user created! Username: admin | Password: admin123")
    finally:
        db.close()

if __name__ == "__main__":
    add_admin_user()