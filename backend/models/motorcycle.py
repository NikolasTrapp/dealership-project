from geral.config import *
from models.vehicle import Vehicle


class Motorcycle(Vehicle):
    __tablename__ = "motorcycle"

    id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "motorcycle",
    }

    def make(self, dados):
        self.name = dados["name"]
        self.brand = dados["brand"]
        self.color = dados["color"]
        self.year = dados["year"]
        self.mileage = dados["mileage"]
        self.engine_capacity = dados["engine_capacity"]
        self.price = dados["price"]
        self.image_name = dados["image_name"]
        self.type = dados["type"]