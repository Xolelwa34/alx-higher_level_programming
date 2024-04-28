#!/usr/bin/python3
""""Defines a state model."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ (str): Name of the MySQL table to store States.
    id (sqlalchemy.Integer): States id.
    name (sqlalchemy.String): Name of states.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
