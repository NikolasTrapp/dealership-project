from geral.config import *
from models.customer import Customer


@app.route("/listCustomers", methods=["GET"])
def list_customers():
    try:
        customers = [c.json() for c in db.session.query(Customer).all()]
        if len(customers) <= 0:
            raise Exception("Any customer found!")
        else:
            response = jsonify({"result": "ok", "details": customers})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/listCustomersById/<int:id>", methods=["GET"])
def listCustomers(id: int):
    try:
        customer = db.session.query(Customer).filter_by(id=id).first()
        if customer == None:
            raise Exception("Any customer found!")
        else:
            response = jsonify({"result": "ok", "details": customer})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/addCustomer", methods=["POST"])
def add_customer():
    data = request.get_json(force=True)
    print(data)
    try:
        customer = Customer(**data)
        customer.encypt_password()
        if customer.verify_cpf() == None:
            raise Exception("Wrong CPF pattern")
        else:
            db.session.add(customer)
            db.session.commit()
            response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/deleteCustomer/<int:id>", methods=["DELETE"])
def delete_customer(id: int):
    try:
        db.session.query(Customer).filter_by(id=id).delete()
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/updateCustomer/<int:id>", methods=["PUT"])
def update_customer(id: int):
    data = request.get_json(force=True)
    try:
        db.session.query(Customer).filter_by(id=id).update(data)
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/validate_login", methods=["POST"])
def validate_login():
    try:
        data = request.get_json(force=True)
        customer = db.session.query(Customer).filter_by(
            name=data["name"], email=data["email"]).first()
        if customer is None:
            response = jsonify({"result": "error", "details": "No customer found with this name or email"})
        elif customer.verify_password(data["password"]):
            access_token = create_access_token(identity=data["name"])
            response = jsonify({"result": "ok", "details": customer.json(), "token": access_token})
        else:
            response = jsonify({"result": "error", "details": "wrong password!"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response
