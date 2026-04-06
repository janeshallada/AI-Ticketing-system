from sqlalchemy import Column, Integer, String
from database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="New")
    department = Column(String)
    assigned_to = Column(String)

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    department = Column(String)
    skills = Column(String)
    load = Column(Integer, default=0)
    availability = Column(String, default="Available")
