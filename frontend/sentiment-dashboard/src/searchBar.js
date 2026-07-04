import React, { useState, useEffect } from "react";

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
      const res = await fetch(`${API}/product/${encodeURIComponent(query)}`);
      const data = await res.json();
      setProduct(data);
    } catch (err) {
      console.error(err);
      alert("Failed to fetch product data.");
    }
  };

  return (
    <div style={{ textAlign: "center", marginBottom: "20px" }}>
      <select
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      >
        <option value="">Select Product</option>
        {products.map((p) => (
          <option key={p} value={p}>
            {p}
          </option>
        ))}
      </select>

      <button onClick={handleSearch}>Search</button>
    </div>
  );
}

export default SearchBar;