from models.customer import Customer
from models.employee import Employee
from models.offers import Offer
from geral.config import *
from models.vehicle import Vehicle
from datetime import date

@app.route("/")
def home():
    return "Hello World!!!"

@app.route("/delete-tables")
def delete_tables():
    db.drop_all()
    return "Apagou tudo"

@app.route("/create-tables")
def create_tables():
    db.create_all()
    return "Criou tudo"