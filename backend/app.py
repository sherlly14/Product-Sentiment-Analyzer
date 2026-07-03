from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import certifi

app = Flask(__name__)
CORS(app)

uri = "mongodb+srv://sibilannat30:Sibil382@cluster0.pmhuizc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

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


if __name__ == "__main__":
    app.run(debug=True)