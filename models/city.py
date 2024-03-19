#!/usr/bin/python3
"""Combined module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models import storage_type

class User(BaseModel, Base):
    """User class that inherits from BaseModel and Base"""
    __tablename__ = 'users'
    # User-specific attributes
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    # Relationship with Place
    places = relationship('Place', backref='user', cascade='all, delete, delete-orphan')

class City(BaseModel, Base):
    """City class that inherits from BaseModel and Base"""
    __tablename__ = 'cities'
    # City-specific attributes
    name = Column(String(128), nullable=False)
    # Relationship with Place
    places = relationship('Place', backref='cities', cascade='all, delete, delete-orphan')

class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = 'places'
    # Place-specific attributes
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    # Relationships with Review and Amenity
    if storage_type == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False, backref='place_amenities')
