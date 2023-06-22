#!/usr/bin/python3
""" City Module for HBNB project """
import sqlalchemy
import models
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv

class City(BaseModel, Base):
    """ The city class"""
    if models.storage == "database":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id",
                          ondelete="CASCADE"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", cascade="all, delete", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize City """
        super().__init__(*args, **kwargs)
