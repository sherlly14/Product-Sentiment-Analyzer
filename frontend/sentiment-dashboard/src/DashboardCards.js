import React from "react";
import "./DashboardCards.css";

function DashboardCards({ product }) {
  if (!product) return null;

  return (
    <div className="cards-container">
      <div className="card rating">
        <h3>⭐ Rating</h3>
        <h2>{product.rating || "N/A"}</h2>
      </div>

      <div className="card positive">
        <h3>😊 Positive</h3>
        <h2>{product.positive_percentage || 0}%</h2>
      </div>

      <div className="card neutral">
        <h3>😐 Neutral</h3>
        <h2>{product.neutral_percentage || 0}%</h2>
      </div>

      <div className="card negative">
        <h3>😞 Negative</h3>
        <h2>{product.negative_percentage || 0}%</h2>
      </div>
    </div>
  );
}

export default DashboardCards;