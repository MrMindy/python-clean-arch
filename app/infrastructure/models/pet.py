from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from app.infrastructure.config import Base

import enum


class Species(enum.Enum):
    """Defining animals species"""

    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pet(Base):

    """Pet Model"""

    __tablename__ = "pet"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(Species), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, user_id={self.user_id}]"
