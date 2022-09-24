from geral.config import *
from models.person import Person
from models.sales import Sales
import bcrypt


class Customer(Person):
    __tablename__ = "customer"

    id = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)
    password = db.Column(db.String(254), nullable = False)

    sales = db.relationship("Sales", back_populates="customer")

    __mapper_args__ = {
        "polymorphic_identity": "customer",
    }

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "cpf": self.cpf,
            "email": self.email,
            "password": str(self.password)
        }

    def encypt_password(self) -> None:
        self.password = bcrypt.hashpw(self.password.encode("utf-8"), bcrypt.gensalt())

    def verify_password(self, passowrd:str) -> bool:
        return bcrypt.checkpw(passowrd.encode("utf-8"), self.password)