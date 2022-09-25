from geral.config import *
from models.car import *
from models.customer import *
from models.employee import *
from models.motorcycle import *
from models.person import *
from models.sales import *
from models.vehicle import *
import datetime

car = Car(name = "Ferrari", color = "Red", year = 2022, mileage = 0, engine_capacity = 830, price = 3400000.00, image_name = "bingapoo.jpg")
motorcycle = Motorcycle(name = "Hornet", color = "Black", year = 2021, mileage = 0, engine_capacity = 6000, price = 35000.00,image_name = "bingapoo.jpg")
employee = Employee(name = "Geraldo", age = 45, cpf = "123.456.789-90", email = "geraldo@gmail.com", salary = 2300.00)
customer = Customer(name = "Cleber", age = 30, cpf = "321.654.987-90", email = "cleber@gmail.com", password = "123")
customer.encypt_password()
sale = Sales(vehicle_id = 1, customer_id = 1, employee_id = 2, value = car.price, date = datetime.date(2022, 9, 24))

def add(entity):
    db.session.add(entity)
    db.session.commit()

def query(entity):
    print([x.json() for x in db.session.query(entity).all()])

def delete(entity, id):
    db.session.query(entity).filter_by(id = id).delete()
    db.session.commit()

add(car)
add(customer)
add(employee)
add(motorcycle)
add(sale)