from __future__ import annotations

import os
import sys
from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship, declarative_base, Mapped
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


user_planet_favorite = Table(
    "UserPlanetFavorite",
    Base.metadata,
    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("planet_id", ForeignKey("Planet.id"), primary_key=True),
)

user_vehicle_favorite = Table(
    "UserVehicleFavorite",
    Base.metadata,
    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("vehicle_id", ForeignKey("Vehicle.id"), primary_key=True),
)

user_character_favorite = Table(
    "UserCharacterFavorite",
    Base.metadata,
    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("character_id", ForeignKey("Character.id"), primary_key=True),
)

user_starship_favorite = Table(
    "UserStarshipFavorite",
    Base.metadata,
    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("starship_id", ForeignKey("Starship.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    favorites: Mapped[List[Planet]] = relationship("Planet", secondary=user_planet_favorite)
    Vehicle_favorites: Mapped[List[Vehicle]] = relationship("Vehicle", secondary=user_vehicle_favorite)
    Character_favorites: Mapped[List[Character]] = relationship("Character", secondary=user_character_favorite)
    Starship_favorites: Mapped[List[Starship]] = relationship("Starship", secondary=user_starship_favorite)

class Planet(Base):
    __tablename__ = "Planet"

    id = Column(Integer, primary_key=True)
    population = Column(Integer,nullable=False)
    climate = Column(String, nullable=False)
    surface_water_percentage = Column(String, nullable=False)
    radius = Column(Float, nullable=False)
    gravity = Column(Float, nullable=False)
    favorites: Mapped[List[User]] = relationship("User", secondary=user_planet_favorite)

    
class Vehicle(Base):
    __tablename__ = "Vehicle"

    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(Integer,nullable=False)
    consumables = Column(String, nullable=False)
    cost_in_credits = Column(Float, nullable=False)
    manufacturer = Column(String, nullable=False)
    model = Column(String, nullable=False)
    vehicle_favorites: Mapped[List[User]] = relationship("user", secondary=user_vehicle_favorite)


class Character(Base):
    __tablename__ = "Character"

    id = Column(Integer, primary_key=True)
    birth_year = Column(Integer,nullable=False)
    eye_color = Column(String, nullable=False)
    films = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    height = Column(Float, nullable=False)
    character_favorites: Mapped[List[User]] = relationship("user", secondary=user_character_favorite)
    
class Starship(Base):
    __tablename__ = "Starship"

    id = Column(Integer, primary_key=True)
    birth_year = Column(Integer,nullable=False)
    eye_color = Column(String, nullable=False)
    films = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    height = Column(Float, nullable=False)
    starship_favorites: Mapped[List[User]] = relationship("user", secondary=user_starship_favorite)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')