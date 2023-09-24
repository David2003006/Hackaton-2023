from flask import Flask, jsonify, request
import app
from products import products as pr
from Model import User

@app.route("/api/products", methods=['GET'])
def get_endpint():
     return jsonify(pr)

@app.route('/api/<string:id>', methods=['GET'])
def getProducts(id):
     productsFound= [product for product in pr if product["id"]==int(id)]
     if (len(productsFound) > 0 ):
          return jsonify({"product": productsFound[0]})
     return jsonify({"message": "producto con el id no encontrado"})

@app.route('/api/post', methods=['POST'])
def addProduct():
     new_product={
         "id": request.json["id"],
         "name": request.json["name"],
         "price": request.json["price"],
         "quatity": request.json["quatity"]
    }
     pr.append(new_product)
     return jsonify({"message":"Product Added Suscefuley", "products": pr})

@app.route('/api/update/<string:id>',methods=['PUT'])
def editProduct(id):
     productsFound= [product for product in pr if product["id"]==int(id)]
     if(len(productsFound) > 0):
          productsFound[0]["id"]= request.json["id"]
          productsFound[0]["name"]= request.json["name"]
          productsFound[0]["price"]= request.json["price"]
          productsFound[0]["quatity"]= request.json["quatity"]
          return jsonify({
               "mesagge": "product update",
               "product":  productsFound[0]
          })
     return jsonify({"mesagge": "product not found"})

@app.route('/api/delete/<string:id>',methods=['DELETE'])
def deleteProduct(id):
     productsFound= [product for product in pr if product["id"]==int(id)]
     if(len(productsFound)> 0):
            pr.remove(productsFound[0])
            return jsonify({
                "mesagge": "Product delete",
                "products": pr
               })
     return jsonify({"mesaagge":"Product not found"})