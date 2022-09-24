from geral.config import *
from models.car import *
from models.customer import *
from models.employee import *
from models.motorcycle import *
from models.person import *
from models.sales import *
from models.vehicle import *

c = Employee(name = "a", age=13, cpf = "111", email = "dddd", salary = 300.00)
db.session.add(c)
db.session.commit()