from geral.config import *
# from models.customer import Customer
from models.employee import Employee
from models.vehicle import Vehicle


class Sales(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key = True)

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable = False)
    vehicle = db.relationship("Vehicle", back_populates="sales")

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = False)
    customer = db.relationship("Customer", back_populates="sales")

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable = False)
    employee = db.relationship("Employee", back_populates="sales")

    value = db.Column(db.Float, nullable = False)
    date = db.Column(db.Date, nullable = False)

    def json(self):
        return {
            "id": self.id,
            "value": self.value,
            "date": self.date,
            "vehicle": self.vehicle.id,
            "employee": self.employee.id,
            "customer": self.customer.id
        }