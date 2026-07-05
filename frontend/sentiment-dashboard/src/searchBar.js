import React, { useState, useEffect } from "react";
import "./SearchBar.css";

const API = "https://product-sentiment-analyzer-utip.onrender.com";

function SearchBar({ setProduct }) {
  const [products, setProducts] = useState([]);
  const [query, setQuery] = useState("");

  useEffect(() => {
    fetch(`${API}/products`)
      .then((res) => res.json())
      .then((data) => setProducts(data))
      .catch((err) => console.error(err));
  }, []);

  const handleSearch = async () => {
    if (!query) {
      alert("Please select a product");
      return;
    }

    try {
      const res = await fetch(
        `${API}/product/${encodeURIComponent(query)}`
      );
      const data = await res.json();
      setProduct(data);
    } catch (err) {
      console.error(err);
      alert("Failed to fetch product data.");
    }
  };

  return (
    <div className="search-container">
      <h2 className="search-title">🔍 Search Product</h2>

      <p className="search-subtitle">
        Select a product to view sentiment analysis and customer reviews.
      </p>

      <div className="search-box">
        <select
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="search-select"
        >
          <option value="">Select Product</option>

          {products.map((product) => (
            <option key={product} value={product}>
              {product}
            </option>
          ))}
        </select>
      </div>

      <button className="search-btn" onClick={handleSearch}>
        🔍 Search
      </button>
    </div>
  );
}

export default SearchBar;