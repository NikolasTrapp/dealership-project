from geral.config import *
from models.sales import Sales
from datetime import date

@app.route("/listSales", methods = ["GET"])
def list_sales():
    try:
        if len(db.session.query(Sales).all()) <= 0:
            raise Exception("Any sale found!")
        else:
            response = jsonify({"result": "ok", "details": {
                "labels": [s.date.strftime("%d/%m/%Y") for s in db.session.query(Sales).all()],
                "values": [s.value for s in db.session.query(Sales).all()],
                "type": 'pie'
            }
        })
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/addSale", methods=["POST"])
def add_sale():
    try:
        data = request.get_json(force=True)
        data["date"] = date.today()
        print(data["date"])
        sale = Sales(**data)
        db.session.add(sale)
        db.session.commit()
        response = jsonify({"result": "ok", "details": "ok"})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response