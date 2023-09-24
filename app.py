from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from Model import Base
import pymysql

#from Models.Model import Base

app= Flask(__name__)

from products import products as pr

pymysql.connect_timeout = 30

db_url='mysql+pymysql://jcUser:codingfiends2023@34.41.133.46:3306/BanorteIA2'
engine= create_engine(db_url, pool_pre_ping=True)
Base.metadata.create_all(engine)

     
if __name__ == "__main__":
    app.run(debug=True, port=4000)