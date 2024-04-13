#!/usr/bin/python3

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sys

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State")

def list_cities(username, password, dbname):
    """Connect to the database and list all cities with their states."""
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{dbname}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying cities and joining with states, sorting by city id
    cities = session.query(City).join(State).order_by(City.id).all()
    
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_cities(username, password, dbname)
    else:
        print("Usage: script.py <mysql username> <mysql password> <database name>")
