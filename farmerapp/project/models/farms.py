from extensions import db

class Farm(db.Model):
    __tablename__ = 'farms'

    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String, nullable=False)
    village = db.Column(db.String, nullable=False)
    crop_grown = db.Column(db.String, nullable=False)
    sowing_date = db.Column(db.Date, nullable=False)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmers.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))

    farmer = db.relationship("Farmer", back_populates="farms")
    country = db.relationship("Country", back_populates="farms")
    schedules = db.relationship("Schedule", back_populates="farm", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Farm(id={self.id}, crop_grown={self.crop_grown}, sowing_date={self.sowing_date})>"
