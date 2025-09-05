from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base 

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String)
    rides = relationship("Ride", back_populates="driver")

class Ride(Base):
    __tablename__ = 'rides'
    
    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    driver_id = Column(Integer, ForeignKey('users.id'))
    driver = relationship("User", back_populates="rides")

class Driver(Base):
    __tablename__ = 'drivers'
    
    id = Column(Integer, primary_key=True, index=True)
    license_number = Column(String, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
