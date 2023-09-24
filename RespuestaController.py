from flask import jsonify, request

from sqlalchemy.orm import sessionmaker
from Model import Respuestas_back,User
from app import app,engine


Session= sessionmaker(bind=engine)


from sqlalchemy.orm import Session

@app.route("/api/recomendacion-inversion/<string:id>/<string:years>", methods=["GET"])
def get_respuesta(id, years):
    session = Session()
    user = session.query(User).filter_by(id=int(id)).first()
    session.close()
    if user:
        return jsonify({"message": "Trabajando en respuesta"})
    else:
        return jsonify({"message": "no está registrado"})

@app.route("/api/get2", methods=["GET"])
def get_respuesta():
    return jsonify({"mesagge": "si jalo"})
    
    
