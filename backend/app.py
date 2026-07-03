
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import certifi
import os

app = Flask(__name__)
CORS(app)



uri = os.getenv("MONGO_URI")

client = MongoClient(uri, tlsCAFile=certifi.where())

db = client["Majorproject1"]
collection = db["reviews"]


@app.route("/")
def home():
    return jsonify({
        "message": "Product Sentiment Analyzer API is Running!"
    })


@app.route("/products", methods=["GET"])
def get_products():

    products = collection.distinct("product_name")

    return jsonify(products)


@app.route("/reviews", methods=["GET"])
def get_reviews():

    reviews = list(collection.find({}, {"_id": 0}))

    return jsonify(reviews)


@app.route("/reviews/<product_name>", methods=["GET"])
def get_reviews_by_product(product_name):

    reviews = list(
        collection.find(
            {"product_name": product_name},
            {"_id": 0}
        )
    )

    return jsonify(reviews)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)