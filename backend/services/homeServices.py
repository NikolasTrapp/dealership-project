from models.customer import Customer
from models.employee import Employee
from geral.config import *
from models.vehicle import Vehicle
# from PIL import Image

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
    
@app.route("/listVehicles", methods = ["GET"])
def list_vehicles():
    try:
        vehicles = [v.json() for v in db.session.query(Vehicle).all()]
        if len(vehicles) <= 0:
            raise Exception("Any vehicle found!")
        else:
            response = jsonify({"result": "ok", "details": vehicles})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/getData")
def getData():
    try:
        vehicles = [v.json() for v in db.session.query(Vehicle).all()]
        customers = [c.json() for c in db.session.query(Customer).all()]
        employees = [e.json() for e in db.session.query(Employee).all()]
        response = jsonify({"vehicles": vehicles, "customers": customers, "employees": employees})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def allowed_file(filename):
    return '.' not in filename or filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS