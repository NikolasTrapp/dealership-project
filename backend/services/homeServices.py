from geral.config import *

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