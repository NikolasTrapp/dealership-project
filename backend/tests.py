from geral.config import *
from models.car import *
from models.customer import *
from models.employee import *
from models.motorcycle import *
from models.person import *
from models.sales import *
from models.vehicle import *
import datetime

'''car = Car(name = "Ferrari", color = "Red", year = 2022, mileage = 0, engine_capacity = 830, price = 3400000.00, image_name = "bingapoo.jpg")
motorcycle = Motorcycle(name = "Hornet", color = "Black", year = 2021, mileage = 0, engine_capacity = 6000, price = 35000.00,image_name = "bingapoo.jpg")
employee = Employee(name = "Geraldo", age = 45, cpf = "123.456.789-90", email = "geraldo@gmail.com", salary = 2300.00)
customer = Customer(name = "Cleber", age = 30, cpf = "321.654.987-90", email = "cleber@gmail.com", password = "123", phone = "(47) 99999-9999", adress = "R. tchurusbango tchurusbago", adress_number = 81)
customer.encypt_password()
sale = Sales(vehicle_id = 1, customer_id = 1, employee_id = 2, value = car.price, date = datetime.date(2022, 9, 24))

def add(entity):
    db.session.add(entity)
    db.session.commit()

def query(entity):
    print([x.json() for x in db.session.query(entity).all()])

def delete(entity, id):
    db.session.query(entity).filter_by(id = id).delete()
    db.session.commit()'''

def addCars():
    car1 = Car(name = "Ferrari F8", brand = "Ferrari", color = "Red", year = 2022, mileage = 0, engine_capacity = 720, price = 4350000.00, image_name = "ferrari.jpg")
    car2 = Car(name = "Fusca", brand = "Volkswagen", color = "Blue", year = 1973, mileage = 0, engine_capacity = 65, price = 28000.00, image_name = "fusca.jpg")
    car3 = Car(name = "Fiat Uno", brand = "Fiat", color = "White", year = 1990, mileage = 170, engine_capacity = 75, price = 12484.00, image_name = "fiatuno.jpg")
    car4 = Car(name = "Kicks", brand = "Nissan", color = "Silver", year = 2022, mileage = 0, engine_capacity = 430, price = 106000.00, image_name = "kicks.jpg")
    car5 = Car(name = "Gol Bolinha", brand = "Volkswagen", color = "White", year = 2000, mileage = 0, engine_capacity = 109, price = 35000.00, image_name = "golbolinha.jpg")
    car6 = Car(name = "Monza", brand = "Chevrolet", color = "Red", year = 1994, mileage = 0, engine_capacity = 99, price = 16990.00, image_name = "monza.jpg")
    car7 = Car(name = "Del Rey", brand = "Ford", color = "Cyan", year = 1989, mileage = 0, engine_capacity = 830, price = 29990.00, image_name = "delrey.jpg")
    car8 = Car(name = "Ford GT", brand = "Ford", color = "White", year = 2021, mileage = 0, engine_capacity = 669, price = 2450000.00, image_name = "fordgt.jpg")
    car9 = Car(name = "Lamborghini Aventador", brand = "Lamborghini", color = "Black", year = 2013, mileage = 0, engine_capacity = 770, price = 8700000.00, image_name = "aventador.jpg")
    car10 = Car(name = "Camaro", brand="Ford", color = "Yellow", year = 2010, mileage = 0, engine_capacity = 461, price = 481000.00, image_name = "camaro.jpg")
    db.session.add(car1)
    db.session.add(car2)
    db.session.add(car3)
    db.session.add(car4)
    db.session.add(car5)
    db.session.add(car6)
    db.session.add(car7)
    db.session.add(car8)
    db.session.add(car9)
    db.session.add(car10)
    db.session.commit()
    
def addMotorcycles():
    motorcycle1 = Motorcycle(name = "Hornet", brand = "Honda", color = "Black", year = 2021, mileage = 0, engine_capacity = 6000, price = 35000.00,image_name = "hornet.jpg")
    motorcycle2 = Motorcycle(name = "Kawasaki Ninja", brand = "Kawasaki", color = "Black", year = 2021, mileage = 0, engine_capacity = 6000, price = 54000.00,image_name = "ninja.jpg")
    motorcycle3 = Motorcycle(name = "XJ6", brand = "Yamaha", color = "Black", year = 2009, mileage = 0, engine_capacity = 600, price = 28000.00,image_name = "xj6.jpg")
    motorcycle4 = Motorcycle(name = "Biz", brand = "Honda", color = "Red", year = 2010, mileage = 0, engine_capacity = 129, price = 8330.00, image_name = "biz.jpg")
    motorcycle5 = Motorcycle(name = "Harley Davidson", brand = "Harley", color = "Black", year = 2021, mileage = 0, engine_capacity = 210, price = 89500.00, image_name = "harley.jpg")
    db.session.add(motorcycle1)
    db.session.add(motorcycle2)
    db.session.add(motorcycle3)
    db.session.add(motorcycle4)
    db.session.add(motorcycle5)
    db.session.commit()
    
def addCustomers():
    customer1 = Customer(name = "Cleber", age = 30, cpf = "213.654.987-90", email = "cleber@gmail.com", password = "123", phone = "(47) 99999-2456", adress = "R. tchurusbango tchurusbago", adress_number = 81)
    customer2 = Customer(name = "Joao", age = 30, cpf = "341.568.367-92", email = "joao@gmail.com", password = "123", phone = "(47) 11111-1346", adress = "R. tchurusbango tchurusbago", adress_number = 82)
    customer3 = Customer(name = "Lucas", age = 30, cpf = "678.348.683-98", email = "lucas@gmail.com", password = "123", phone = "(47) 21312-1731", adress = "R. tchurusbango tchurusbago", adress_number = 83)
    customer4 = Customer(name = "Maria", age = 30, cpf = "321.214.651-62", email = "maria@gmail.com", password = "123", phone = "(47) 12668-1377", adress = "R. tchurusbango tchurusbago", adress_number = 84)
    customer5 = Customer(name = "Joana", age = 30, cpf = "515.746.825-37", email = "joana@gmail.com", password = "123", phone = "(47) 84362-1348", adress = "R. tchurusbango tchurusbago", adress_number = 85)
    customer1.encypt_password()
    customer2.encypt_password()
    customer3.encypt_password()
    customer4.encypt_password()
    customer5.encypt_password()
    db.session.add(customer1)
    db.session.add(customer2)
    db.session.add(customer3)
    db.session.add(customer4)
    db.session.add(customer5)
    db.session.commit()
    
def addEmployees():
    employee1 = Employee(name = "Geraldo", age = 45, cpf = "123.456.789-90", email = "geraldo@gmail.com", salary = 2300.00)
    employee2 = Employee(name = "Roberto", age = 45, cpf = "646.862.846-85", email = "roberto@gmail.com", salary = 2400.00)
    employee3 = Employee(name = "Jerivaldo", age = 45, cpf = "652.235.259-23", email = "jerivaldo@gmail.com", salary = 2500.00)
    employee4 = Employee(name = "Romulo", age = 45, cpf = "872.547.358-54", email = "romulo@gmail.com", salary = 2600.00)
    employee5 = Employee(name = "Jurema", age = 45, cpf = "547.234.471-32", email = "jurema@gmail.com", salary = 2700.00)
    db.session.add(employee1)
    db.session.add(employee2)
    db.session.add(employee3)
    db.session.add(employee4)
    db.session.add(employee5)
    db.session.commit()
    
def addSales():
    sale1 = Sales(vehicle_id = 1, customer_id = 1, employee_id = 6, value = 4350000.00, date = datetime.date(2022, 9, 24))
    sale2 = Sales(vehicle_id = 11, customer_id = 5, employee_id = 7, value = 35000.00, date = datetime.date(2022, 8, 26))
    sale3 = Sales(vehicle_id = 12, customer_id = 4, employee_id = 10, value = 54000.00, date = datetime.date(2022, 8, 27))
    sale4 = Sales(vehicle_id = 4, customer_id = 2, employee_id = 9, value = 106000.00, date = datetime.date(2022, 9, 10))
    sale5 = Sales(vehicle_id = 5, customer_id = 3, employee_id = 8, value = 35000.00, date = datetime.date(2022, 9, 12))
    db.session.add(sale1)
    db.session.add(sale2)
    db.session.add(sale3)
    db.session.add(sale4)
    db.session.add(sale5)
    db.session.commit()