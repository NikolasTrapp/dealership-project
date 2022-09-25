from geral.config import *
from models.sales import Sales

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
        print({
                "x": [s.date.strftime("%d/%m/%Y") for s in db.session.query(Sales).all()],
                "y": [s.value for s in db.session.query(Sales).all()],
                "type": 'pie'
            })
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response