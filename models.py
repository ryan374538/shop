from sqlalchemy import Integer, Column, Float, Boolean, String 
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    role=Column(String(100))
   

    def __init__(self, username, password , role):
        self.username = username
        self.password = password
        self.role =role 
     

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Boolean, nullable=False)
    quantity = Column(Integer,nullable=True)

    def __init__(self, product, price, stock,quantity):
        self.product = product
        self.price = price
        self.stock = stock
        self.quantity =quantity

