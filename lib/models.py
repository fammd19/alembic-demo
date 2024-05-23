from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = "dogs"

    id = Column ( Integer(), primary_key=True )
    name = Column ( String(), nullable=False )
    breed = Column ( String() )
    age = Column ( Integer() )

    def __repr__(self):
        return f"{self.id}: {self.name} {self.breed}"