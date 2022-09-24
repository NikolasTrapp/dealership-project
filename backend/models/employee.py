from models.person import Person
# from models.sales import Sales
from geral.config import *


class Employee(Person):
    __tablename__ = "employee"

    id = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)
    salary = db.Column(db.Float, nullable = False)

    sales = db.relationship("Sales", back_populates="employee")

    __mapper_args__ = {
        "polymorphic_identity": "employee",
    }

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "cpf": self.cpf,
            "email": self.email
        }
