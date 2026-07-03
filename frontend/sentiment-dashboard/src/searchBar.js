import React, { useState } from 'react';
import { products } from './mockdata';

function SearchBar({ setProduct }) {
  const [query, setQuery] = useState('');

  const handleSearch = () => {
    if (!query) {
      alert("Please select or enter a product");
      return;
    }

    const found = products.find(
      (p) => p.name.toLowerCase() === query.toLowerCase()
    );

    if (found) {
      setProduct(found);
    } else {
      alert("Product not found!");
      setProduct(null);
    }
  };

  return (
    <div style={styles.container}>
      <select
        style={styles.input}
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      >
        <option value="">Select a Product</option>
        {products.map((p) => (
          <option key={p.id} value={p.name}>
            {p.name}
          </option>
        ))}
      </select>

      <input
        style={styles.input}
        type="text"
        placeholder="Or type product name..."
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