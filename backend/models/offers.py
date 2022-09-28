from geral.config import *
from models.employee import Employee
# from models.vehicle import Vehicle


class Offer(db.Model):
    __tablename__ = "offers"
    
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, nullable = False)
    adress = db.Column(db.String(254), nullable = False)
    adress_number = db.Column(db.Integer, nullable = False)
    phone = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(254), nullable = False)
    
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable = False)
    vehicle = db.relationship("Vehicle", back_populates="offers")

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = False)
    customer = db.relationship("Customer", back_populates="offers")
    
    def json(self):
        return {
            "id": self.id,
            "date": self.date,
            "adress": self.adress,
            "adress_number": self.adress_number,
            "phone": self.phone,
            "email": self.email,
            "vehicle": self.vehicle.id,
            "customer": self.customer.id
        }