import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(80), unique=True, nullable=False)
    first_name =Column(String(80), nullable=False)
    last_name =Column(String(80), nullable=False)
    email =Column(String(80),unique=True, nullable=False) 
    password= Column(String(10), nullable=False)
class Planets(Base):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(200))
    climate = Column(String(200))
    terrain =Column(String(200))
    population = Column(Integer)
    diameter= Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    surface_water = Column(Integer)
    residents = Column(Integer, ForeignKey('characters.character_id'))
    characters = relationship('Characters')
    #gravity = "1 standard"
class Characters(Base):
    __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True)
    name =  Column(String(200))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(200))
    skin_color = Column(String(200))
    eye_color = Column(String(200))
    #birth_year = Column(Integer)
    gender = Column(String(200))
    homeworld = Column(Integer, ForeignKey('planets.planet_id'))
    planets = relationship('Planets')
    vehicles = Column(Integer, ForeignKey('vehicles.vehicle_id'))
    vehicles = relationship('Vehicles')
class Vehicles(Base):
    __tablename__ = 'vehicles'
    vehicle_id = Column(Integer, primary_key=True)
    name = Column(String(200))
    model = Column(String(200))
    manufacturer = Column(String(200))
    cost_in_credits = Column(Integer)
    #length = "36.8 "
    #max_atmosphering_speed = "30"
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    #consumables = "2 months"
    vehicle_class = Column(String(200))
    pilots = Column(Integer, ForeignKey('characters.character_id'))
    characters = relationship('Characters')
class Favorites(Base):
    __tablename__ = 'favorites'
    like_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship('User')
    fav_planet_id = Column(Integer, ForeignKey('planets.planet_id'))
    planets = relationship('Planets')
    fav_character_id = Column(Integer, ForeignKey('characters.character_id'))
    characters = relationship('Characters')
    fav_vehicle_id = Column(Integer, ForeignKey('vehicles.vehicle_id'))
    vehicles = relationship('Vehicles')
    def to_dict(self):
        return {}

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e