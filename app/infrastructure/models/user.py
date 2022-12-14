from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.infrastructure.config import Base


class User(Base):

    """Users Models"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id_pet = relationship("Pet")

    def __rep__(self):
        return f"Usr [name={self.name}]"
