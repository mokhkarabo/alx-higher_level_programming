from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an instance of the declarative_base class
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'  # Links to the MySQL table states
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)  # auto-generated, unique integer, can't be null, primary key
    name = Column(String(128), nullable=False)  # column of a string with maximum 128 characters and can't be null

# SQLAlchemy engine that will interact with the MySQL database
engine = create_engine('mysql+mysqlconnector://user:password@localhost:3306/dbname', echo=True)

# Create all tables stored in this metadata (Base subclasses)
Base.metadata.create_all(engine)

# Session creation to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example usage: Creating a new State
new_state = State(name='New York')
session.add(new_state)
session.commit()

# Close the session
session.close()
