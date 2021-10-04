from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("postgresql+psycopg2://postgres:123@localhost/contacts")
base = declarative_base()


class User(base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True, unique=True)
    username = Column(String(), nullable=False)
    email = Column(String(), nullable=False)
    password = Column(String(), nullable=False)


class Contact(base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100), nullable=False, unique=True)
    phone = Column(String(100), nullable=False)
    users = relationship('User')


Session = sessionmaker(engine)

base.metadata.create_all(engine)

