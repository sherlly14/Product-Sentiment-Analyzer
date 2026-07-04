
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

    reviews = list(collection.find({"product_name": product_name}))

    if not reviews:
        return jsonify({"error": "Product not found"}), 404

    overall_rating = reviews[0]["overall_rating"]

    sentiment_counts = Counter(review["sentiment"] for review in reviews)

    sentiment_data = [
        {
            "name": "Positive",
            "value": sentiment_counts.get("Positive", 0)
        },
        {
            "name": "Negative",
            "value": sentiment_counts.get("Negative", 0)
        },
        {
            "name": "Neutral",
            "value": sentiment_counts.get("Neutral", 0)
        }
    ]

    rating_counts = Counter(review["review_rating"] for review in reviews)

    rating_data = [
        {"rating": 1, "count": rating_counts.get(1, 0)},
        {"rating": 2, "count": rating_counts.get(2, 0)},
        {"rating": 3, "count": rating_counts.get(3, 0)},
        {"rating": 4, "count": rating_counts.get(4, 0)},
        {"rating": 5, "count": rating_counts.get(5, 0)}
    ]

    return jsonify({
        "name": product_name,
        "rating": overall_rating,
        "sentimentData": sentiment_data,
        "ratingData": rating_data
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)