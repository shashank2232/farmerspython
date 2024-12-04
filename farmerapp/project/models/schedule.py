from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from extensions import db

class Schedule(db.Model):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True)
    days_after_sowing = Column(Integer, nullable=False)
    fertiliser = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    quantity_unit = Column(String, nullable=False)
    price_per_unit = Column(Float, nullable=False)    # ton, kg, g, L, mL
    farm_id = Column(Integer, ForeignKey('farms.id'))

    farm = relationship("Farm", back_populates="schedules")

    def __repr__(self):
        return f"<Schedule(id={self.id}, fertiliser={self.fertiliser}, days_after_sowing={self.days_after_sowing})>"
