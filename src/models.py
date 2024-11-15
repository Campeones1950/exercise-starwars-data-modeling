import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email_username = Column (String(200), nullable= False, unique= True) 
    name = Column(String(250), nullable=False)
    password = Column(String(80), nullable=False)
    first_name = Column (String (250), nullable = False)
    last_name = Column (String (250), nullable = False)


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table Character.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    home_world = Column(String(250), nullable=False)
    
    

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table Character.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
  
  

class FavoritesCharacters(Base):
    __tablename__ ='favorite_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship('Characters')

class FavoritesPlanets(Base):
    __tablename__ ='favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship('Planets')

    
   

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "characters_id": self.characters_id
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
