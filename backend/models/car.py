from models.vehicle import Vehicle
from geral.config import *


class Car(Vehicle):
    __tablename__ = "car"

    id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), primary_key=True)
    doors = db.Column(db.Integer(), nullable = False)

    __mapper_args__ = {
        "polymorphic_identity": "car",
    }

    def json(self):
        return super.json().update({"doors": self.doors})

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
        self.doors = dados["doors"]