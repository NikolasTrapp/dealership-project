from geral.config import *
import re


class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    cpf = db.Column(db.String(14), nullable = False, unique = True)
    email = db.Column(db.String(254), nullable = False, unique = True)
    type = db.Column(db.String(50))

    __mapper_args__ = {
        "polymorphic_identity": "person",
        "polymorphic_on": type,
    }