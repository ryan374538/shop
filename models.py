from sqlalchemy import Integer,Column,Float,Boolean,String
from sqlalchemy.orm import declarative_base

Base=declarative_base()

class Users (Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    username=Column(String(100),nullable=False)
    password=Column(Integer,nullable=False)

    def __init__(self,username,password):
        self.username=username
        self.password=password

class Products(Base):
    __tablename__='products'
    id=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    product=Column(String(100),nullable=False)
    price=Column(Float,nullable=False)
    stock=Column(Boolean,nullable=False)

    
    def __init__(self,product,price,stock):
        self.product=product
        self.price=price
        self.stock=stock


