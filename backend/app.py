from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import certifi
import os
from collections import Counter

app = Flask(__name__)
CORS(app)

# -----------------------------
# MongoDB Connection
# -----------------------------
uri = os.getenv("MONGO_URI")

client = MongoClient(uri, tlsCAFile=certifi.where())

db = client["Majorproject1"]
collection = db["reviews"]

# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Product Sentiment Analyzer API is Running!"
    })

# -----------------------------
# Get All Products
# -----------------------------
@app.route("/products", methods=["GET"])
def get_products():
    try:
        products = sorted(collection.distinct("product_name"))
        return jsonify(products)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------
# Get All Reviews
# -----------------------------
@app.route("/reviews", methods=["GET"])
def get_reviews():
    try:
        reviews = list(collection.find({}, {"_id": 0}))
        return jsonify(reviews)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------
# Get Reviews By Product
# -----------------------------
@app.route("/reviews/<product_name>", methods=["GET"])
def get_reviews_by_product(product_name):
    try:
        reviews = list(
            collection.find(
                {"product_name": product_name},
                {"_id": 0}
            )
        )

        return jsonify(reviews)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------
# Dashboard Data
# -----------------------------
@app.route("/product/<product_name>", methods=["GET"])
def get_product(product_name):

    try:

        reviews = list(collection.find({"product_name": product_name}))

        if len(reviews) == 0:
            return jsonify({"error": "Product not found"}), 404

        # -----------------------------
        # Average Rating
        # -----------------------------
        ratings = []

        for review in reviews:
            try:
                ratings.append(float(review.get("review_rating", 0)))
            except:
                ratings.append(0)

        avg_rating = round(sum(ratings) / len(ratings), 1)

        # -----------------------------
        # Sentiment Counts
        # -----------------------------
        sentiments = [r.get("sentiment", "Neutral") for r in reviews]

        sentiment_counter = Counter(sentiments)

        total = len(reviews)

        positive = sentiment_counter.get("Positive", 0)
        negative = sentiment_counter.get("Negative", 0)
        neutral = sentiment_counter.get("Neutral", 0)

        sentimentData = [
            {
                "name": "Positive",
                "value": round((positive / total) * 100, 1)
            },
            {
                "name": "Negative",
                "value": round((negative / total) * 100, 1)
            },
            {
                "name": "Neutral",
                "value": round((neutral / total) * 100, 1)
            }
        ]

        # -----------------------------
        # Rating Distribution
        # -----------------------------
        rating_counter = Counter()

        for r in ratings:
            rating_counter[int(round(r))] += 1

        ratingData = []

        for i in range(1, 6):
            ratingData.append({
                "rating": str(i),
                "count": rating_counter.get(i, 0)
            })

        # -----------------------------
        # Final JSON
        # -----------------------------
        return jsonify({
            "name": product_name,
            "rating": avg_rating,
            "sentimentData": sentimentData,
            "ratingData": ratingData
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)