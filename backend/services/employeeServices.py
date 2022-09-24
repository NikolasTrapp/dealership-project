from geral.config import *
from models.employee import Employee

@app.route("/listEmployees", methods = ["GET"])
def list_employees():
    try:
        employees = [c.json() for c in db.session.query(Employee).all()]
        if len(employees) <= 0:
            raise Exception("Any employee found!")
        else:
            response = jsonify({"result": "ok", "details": employees})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/listEmployeesById/<int:id>", methods = ["GET"])
def listEmployees(id: int):
    try:
        employee = db.session.query(Employee).filter_by(id = id).first()
        if employee == None:
            raise Exception("Any employee found!")
        else:
            response = jsonify({"result": "ok", "details": employee})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/addEmployee", methods = ["POST"])
def add_employee():
    data = request.get_json(force=True)
    try:
        employee = Employee(**data)
        if employee.verify_cpf() == None:
            raise Exception("Wrong CPF pattern")
        else:
            db.session.add(employee)
            db.session.commit()
            response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/deleteEmployee/<int:id>", methods = ["DELETE"])
def delete_employee(id: int):
    try:
        db.session.query(Employee).filter_by(id = id).delete()
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/updateEmployee/<int:id>", methods = ["PUT"])
def update_employee(id: int):
    data = request.get_json(force=True)
    try:
        db.session.query(Employee).filter_by(id = id).update(data)
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
