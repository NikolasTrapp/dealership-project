from crypt import methods
from geral.config import *
from models.customer import Customer

@app.route("/listCustomers", methods = ["GET"])
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

@app.route("/listCustomersById/<int: id>", methods = ["GET"])
def list_customers(id: int):
    try:
        customer = db.session.query(Customer).filter_by(id = id).first()
        if customer == None:
            raise Exception("Any customer found!")
        else:
            response = jsonify({"result": "ok", "details": customer})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/addCustomer", methods = ["POST"])
def add_customer():
    data = request.get_json(force=True)
    try:
        customer = Customer(data)
        customer.encypt_password()
        db.session.add(customer)
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/deleteCustomer/<int: id>", methods = ["DELETE"])
def delete_customer(id: int):
    try:
        db.session.query(Customer).filter_by(id = id).delete()
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/updateCustomer/<int: id>", methods = ["PUT"])
def update_customer(id: int):
    data = request.get_json(force=True)
    try:
        db.session.query(Customer).filter_by(id = id).update(data)
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
