import React, { useState } from 'react';

function SearchBar({ setProduct }) {
  const [query, setQuery] = useState('');

  // 🔥 CHANGE THIS TO YOUR RENDER BACKEND URL
  const API_URL ="https://product-sentiment-analyzer-utip.onrender.com/";

  const handleSearch = async () => {
    if (!query) {
      alert("Please select or enter a product");
      return;
    }

    try {
      // 🔥 Fetch products from backend
      const response = await fetch(`${API_URL}/products`);
      const data = await response.json();

      // Find matching product
      const found = data.find(
        (p) => p.toLowerCase() === query.toLowerCase()
      );

      if (found) {
        setProduct(found);
      } else {
        alert("Product not found!");
        setProduct(null);
      }
    } catch (error) {
      console.error("Error fetching products:", error);
      alert("Backend not reachable!");
      setProduct(null);
    }
  };

  return (
    <div style={styles.container}>
      <input
        style={styles.input}
        type="text"
        placeholder="Search product..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button style={styles.button} onClick={handleSearch}>
        🔍 Search
      </button>
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    gap: "10px",
    marginBottom: "30px",
    justifyContent: "center",
    alignItems: "center",
    flexWrap: "wrap"
  },
  input: {
    padding: "12px 20px",
    fontSize: "1rem",
    borderRadius: "25px",
    border: "2px solid #3498db",
    width: "300px",
    outline: "none"
  },
  button: {
    padding: "12px 25px",
    fontSize: "1rem",
    borderRadius: "25px",
    border: "none",
    background: "#3498db",
    color: "white",
    cursor: "pointer"
  }
};

export default SearchBar;