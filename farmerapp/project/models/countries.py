from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from extensions import db

class Country(db.Model):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    farmers = relationship("Farmer", back_populates="country")
    farms = relationship("Farm", back_populates="country")

    def __repr__(self):
        return f"<Country(id={self.id}, name={self.name})>"
