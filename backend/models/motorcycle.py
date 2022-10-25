from geral.config import *
from models.vehicle import Vehicle


class Motorcycle(Vehicle):
    __tablename__ = "motorcycle"

    id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "motorcycle",
    }