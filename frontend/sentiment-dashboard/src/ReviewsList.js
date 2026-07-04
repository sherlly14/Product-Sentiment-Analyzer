import React, { useEffect, useState } from "react";

const API = "https://product-sentiment-analyzer-utip.onrender.com";

function ReviewsList({ product }) {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    if (!product) return;

    fetch(`${API}/reviews/${encodeURIComponent(product.name)}`)
      .then((res) => res.json())
      .then((data) => setReviews(data))
      .catch((err) => console.error(err));
  }, [product]);

  const getColor = (sentiment) => {
    if (sentiment === "Positive") return "#2ecc71";
    if (sentiment === "Negative") return "#e74c3c";
    return "#f39c12";
  };

  if (!product) return null;

  return (
    <div style={styles.container}>
      <h2>📝 Reviews</h2>

      {reviews.length === 0 ? (
        <p>No reviews found.</p>
      ) : (
        reviews.map((review, index) => (
          <div
            key={index}
            style={{
              ...styles.card,
              borderLeft: `5px solid ${getColor(review.sentiment)}`
            }}
          >
            <h4>{review.review_title}</h4>

            <p style={styles.text}>{review.review_text}</p>

            <p>⭐ Rating: {review.review_rating}/5</p>

            <span
              style={{
                ...styles.badge,
                background: getColor(review.sentiment)
              }}
            >
              {review.sentiment}
            </span>
          </div>
        ))
      )}
    </div>
  );
}

const styles = {
  container: {
    background: "white",
    borderRadius: "15px",
    padding: "25px",
    boxShadow: "0 2px 10px rgba(0,0,0,0.1)"
  },
  card: {
    padding: "15px",
    marginBottom: "15px",
    borderRadius: "8px",
    background: "#f9f9f9"
  },
  text: {
    fontSize: "0.95rem",
    color: "#333",
    marginBottom: "8px"
  },
  badge: {
    padding: "4px 12px",
    borderRadius: "20px",
    color: "white",
    fontSize: "0.75rem",
    fontWeight: "bold"
  }
};

export default ReviewsList;