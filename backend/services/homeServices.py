from models.customer import Customer
from models.employee import Employee
from models.offers import Offer
from geral.config import *
from models.vehicle import Vehicle
from datetime import date
from geral.cifrar import *

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

@app.route("/login", methods = ["POST"])
def login():
    data = request.get_json()

    name = data["name"]
    email = data["email"]
    password = data["password"]

    customer = Customer.query.filter_by(email=email, name=name, password=encrypt(password)).first()
    if customer is None:
        resposta = jsonify({"result": "error", "details": "Login denied"})
    else:
        access_token = create_access_token(identity = email)
        resposta = jsonify({"result": "ok", "token": access_token, "customer": customer.json()})
    resposta.headers.add("-CoAccessntrol-Allow-Origin", "*")
    return resposta