from geral.config import *
from models.motorcycle import Motorcycle

@app.route("/listMotorcycles", methods = ["GET"])
def list_motorcycles():
    try:
        motorcycles = [c.json() for c in db.session.query(Motorcycle).all()]
        if len(motorcycles) <= 0:
            raise Exception("Any motorcycle found!")
        else:
            response = jsonify({"result": "ok", "details": motorcycles})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/listMotorcyclesById/<int:id>", methods = ["GET"])
def listMotorcycles(id: int):
    try:
        motorcycle = db.session.query(Motorcycle).filter_by(id = id).first()
        if motorcycle == None:
            raise Exception("Any motorcycle found!")
        else:
            response = jsonify({"result": "ok", "details": motorcycle})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/addMotorcycle", methods = ["POST"])
def add_motorcycle():
    data = request.get_json(force=True)
    try:
        motorcycle = Motorcycle(**data)
        db.session.add(motorcycle)
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/deleteMotorcycle/<int:id>", methods = ["DELETE"])
def delete_motorcycle(id: int):
    try:
        db.session.query(Motorcycle).filter_by(id = id).delete()
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/updateMotorcycle/<int:id>", methods = ["PUT"])
def update_motorcycle(id: int):
    data = request.get_json(force=True)
    try:
        db.session.query(Motorcycle).filter_by(id = id).update(data)
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
