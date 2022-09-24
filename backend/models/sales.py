from geral.config import *


class Sales(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key = True)

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    vehicle = db.relationship("Vehicle", back_populates="sales")

    

    '''customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = False)
    customer = db.relationship('Customer')

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable = False)
    vehicle = db.relationship('Vehicle')

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable = False)
    employee = db.relationship('Employee')'''

    value = db.Column(db.Float, nullable = False)