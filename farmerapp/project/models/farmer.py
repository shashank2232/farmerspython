from extensions import db

class Farmer(db.Model):
    __tablename__ = 'farmers'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    language = db.Column(db.String)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))

    country = db.relationship("Country", back_populates="farmers")
    farms = db.relationship("Farm", back_populates="farmer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Farmer(id={self.id}, name={self.name}, phone_number={self.phone_number})>"
