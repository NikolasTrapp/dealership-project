from geral.config import *
from models.offers import Offer

@app.route("/listOffers", methods = ["GET"])
def list_offers():
    try:
        offers = [o.json() for o in db.session.query(Offer).all()]
        if len(offers) <= 0:
            raise Exception("Any employee found!")
        else:
            response = jsonify({"result": "ok", "details": offers})
    except Exception as e:
        response = jsonify({"result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response