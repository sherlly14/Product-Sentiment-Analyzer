
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import certifi
import os
from collections import Counter

app = Flask(__name__)
CORS(app)

# MongoDB Connection
uri = os.getenv("MONGO_URI")

client = MongoClient(uri, tlsCAFile=certifi.where())

db = client["Majorproject1"]
collection = db["reviews"]


# Home Route
@app.route("/")
def home():
    return jsonify({
        "message": "Product Sentiment Analyzer API is Running!"
    })


# Get all product names
@app.route("/products", methods=["GET"])
def get_products():
    products = collection.distinct("product_name")
    return jsonify(products)


# Get all reviews
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
    

# Get dashboard data for a specific product
@app.route("/product/<product_name>", methods=["GET"])
def get_product(product_name):
    try:
        count = collection.count_documents({"product_name": product_name})

        return jsonify({
            "product": product_name,
            "count": count
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)