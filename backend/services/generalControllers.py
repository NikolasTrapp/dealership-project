from services.import_models import *
from geral.cifrar import *


@app.route("/query/<string:entity>", methods = ["GET"])
@jwt_required(optional = True)
def queryController(entity: str):
    try:
        obj = [Car, Motorcycle, Customer, Employee, Offer, Sales, Person, Vehicle][ENTITIES[entity]]
        entities = [x.json() for x in db.session.query(obj).all()]
        if len(entities) <= 0:
            raise Exception(f"Any {entity} found!")
        response = jsonify({"result": "ok", "details": entities})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/search/<string:entity>/<int:id>", methods = ["GET"])
@jwt_required(optional = True)
def searchController(entity: str, id: int):
    try:
        obj = [Car, Motorcycle, Customer, Employee, Offer, Sales, Person, Vehicle][ENTITIES[entity]]
        query = db.session.query(obj).filter_by(id = id).first()
        if query is None:
            raise Exception(f"No entity with id {id} was found!")
        else:
            response = jsonify({"result": "ok", "details": query.json()})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/insert/<string:entity>", methods = ["POST"])
@jwt_required(optional = True)
def insertController(entity: str):
    try:
        data = request.get_json(force= True)
        if entity == "Sale" or entity == "Offer":
            print(date.today())
            data["date"] = date.today()
            obj = [Car, Motorcycle, Customer, Employee, Offer, Sales][ENTITIES[entity]](**data)
        elif entity == "Employee" or entity == "Customer":
            data["password"] = encrypt(data["password"])
            obj = [Car, Motorcycle, Customer, Employee, Offer, Sales][ENTITIES[entity]](**data)
            if not obj.verify_cpf():
                raise Exception("Invalid CPF!")
        else:
            obj = [Car, Motorcycle, Customer, Employee, Offer, Sales][ENTITIES[entity]](**data)
        db.session.add(obj)
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/delete/<string:entity>/<int:id>", methods = ["DELETE"])
@jwt_required()
def deleteController(entity: str, id: int):
    try:
        obj = [Car, Motorcycle, Customer, Employee, Offer, Sales, Person, Vehicle][ENTITIES[entity]]
        number_deleted = db.session.query(obj).filter_by(id = id).delete()
        if number_deleted == 0:
            raise Exception("Entity not found!")
        else:
            db.session.commit()
            response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/update/<string:entity>/<int:id>", methods = ["PUT"])
@jwt_required()
def updateController(entity: str, id: int):
    try:
        data = request.get_json(force= True)
        obj = [Car, Motorcycle, Customer, Employee, Offer, Sales][ENTITIES[entity]]
        if entity == "Sale":
            d = data["data"].split("-")
            data["data"] = date(int(d[2]), int(d[1]), int(d[0]))
        elif entity == "Employee" or entity == "Customer":
            obj = db.session.query(obj).filter_by(id = id).update(data)
            if not obj.verify_cpf():
                raise Exception("Invalid CPF!")
        db.session.query(obj).filter_by(id = id).update(data)
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/save_image", methods=['POST'])
def salvar_imagem():
    try:
        file_val = request.files['image']
        if file_val.filename == "":
            raise Exception("No selected file")
        elif allowed_file(file_val.filename):
            raise Exception("Unsupported image extension")
        else:
            print("Image saved in: images/"+file_val.filename)
            imgfile = os.path.join(path, 'images/'+file_val.filename)
            file_val.save(imgfile)
            response = jsonify({"result":"ok", "details": file_val.filename})
    except Exception as e:
        response = jsonify({"result":"error", "details": str(e)})
    print(response)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/get_image/<int:id>')
@jwt_required(optional = True)
def get_image(id):
    try:
        imgfile = db.session.query(Vehicle).get(id)
        if imgfile == None:
            raise Exception("Any vehicle found!")
        else:
            imgpath = os.path.join(path, 'images/'+ imgfile.image_name)
            return send_file(imgpath, mimetype='image/gif')
    except Exception as e:
        response = jsonify({"result":"error", "details": str(e)})
        return response

@app.route("/getData")
@jwt_required(optional = True)
def getData():
    try:
        vehicles = [v.json() for v in db.session.query(Vehicle).all()]
        customers = [c.json() for c in db.session.query(Customer).all()]
        employees = [e.json() for e in db.session.query(Employee).all()]
        offers = [o.json() for o in db.session.query(Offer).all()]
        response = jsonify({"vehicles": vehicles, "customers": customers, "employees": employees, "offers": offers})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def allowed_file(filename):
    return '.' not in filename or filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS
    