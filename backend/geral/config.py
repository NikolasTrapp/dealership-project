# importações
from flask import Flask, jsonify, request, session, send_file
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from datetime import timedelta
from flask_cors import CORS, cross_origin  # permitir back receber json do front

app = Flask(__name__)
CORS(app)  

path = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
arquivobd = os.path.join(path, 'dealership.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # remover warnings
db = SQLAlchemy(app)

app.config["JWT_SECRET_KEY"] = "^4r#24h90S#b6fU@gg#5"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)
jwt = JWTManager(app)

ENTITIES = {
    "Car": 0,
    "Motorcycle": 1,
    "Customer": 2,
    "Employee": 3,
    "Offer": 4,
    "Sale": 5,
    "Person": 6,
    "Vehicle": 7
}