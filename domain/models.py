from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("postgresql+psycopg2://postgres:123@localhost/contacts", echo=True)
base = declarative_base()


class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)


class Contact(base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer)
    name = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)


Session = sessionmaker(engine)

base.metadata.create_all(engine)
