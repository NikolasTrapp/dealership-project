from geral.config import *
from models.person import Person


class Customer(Person):
    __tablename__ = "customer"


    id = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "customer",
    }

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "cpf": self.cpf,
            "emai": self.email
        }
    