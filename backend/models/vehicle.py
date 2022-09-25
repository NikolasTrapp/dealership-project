from geral.config import *
# from models.sales import Sales


class Vehicle(db.Model):
    __tablename__ = "vehicle"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(70), nullable = False)
    color = db.Column(db.String(70), nullable = False)
    year = db.Column(db.Integer, nullable = False)
    mileage = db.Column(db.Integer, nullable = False)
    engine_capacity = db.Column(db.Integer, nullable = False)
    price = db.Column(db.Float, nullable = False)
    image_name = db.Column(db.String(254), nullable = False)
    type = db.Column(db.String(50))

    sales = db.relationship("Sales", back_populates="vehicle")

    __mapper_args__ = {
        "polymorphic_identity": "vehicle",
        "polymorphic_on": type,
    }

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "year": self.year,
            "mileage": self.mileage,
            "engine_capacity": self.engine_capacity,
            "price": self.price,
            "image_name": self.image_name
        }