from flask import Flask, jsonify

app= Flask(__name__)

from products import products as pr

@app.route("/api/products", methods=['GET'])
def get_endpint():
     return jsonify(pr)

if __name__ == "__main__":
    app.run(debug=True, port=4000)