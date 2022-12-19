import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name=Column(String(250), nullable=False)
    last_name=Column(String(250), nullable=False)

class Post(Base):
    __tablename__="post"
    id = Column(Integer, primary_key=True)
    post_created_by = Column(String(250), ForeignKey('person.username'))
    person_id = Column(Integer, ForeignKey('person.id'))

class Followers(Base):
    __tablename__="followers"
    id= Column(Integer, primary_key=True)
    following_user_id: Column(String(250), ForeignKey('person.username'))

class post_media(Base):
    __tablename__="media"
    id=Column(Integer, primary_key=True)
    post_id=Column(Integer, ForeignKey('post.id'))
    media_file=Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id= Column(Integer, ForeignKey('person.id'))
    post_id=Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
