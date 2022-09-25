from geral.config import *
from models.car import Car

@app.route("/listCars", methods = ["GET"])
def list_cars():
    try:
        cars = [c.json() for c in db.session.query(Car).all()]
        if len(cars) <= 0:
            raise Exception("Any car found!")
        else:
            response = jsonify({"result": "ok", "details": cars})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/listCarsById/<int:id>", methods = ["GET"])
def listCars(id: int):
    try:
        car = db.session.query(Car).filter_by(id = id).first()
        if car == None:
            raise Exception("Any car found!")
        else:
            response = jsonify({"result": "ok", "details": car})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/addCar", methods = ["POST"])
def add_car():
    print("Oi")
    data = request.get_json(force=True)
    try:
        car = Car(**data)
        db.session.add(car)
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/deleteCar/<int:id>", methods = ["DELETE"])
def delete_car(id: int):
    try:
        db.session.query(Car).filter_by(id = id).delete()
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/updateCar/<int:id>", methods = ["PUT"])
def update_car(id: int):
    data = request.get_json(force=True)
    try:
        db.session.query(Car).filter_by(id = id).update(data)
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
