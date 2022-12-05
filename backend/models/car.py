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
        dados = super().json()
        dados["doors"] = self.doors
        return dados