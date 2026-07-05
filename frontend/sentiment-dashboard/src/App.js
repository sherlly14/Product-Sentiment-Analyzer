import React, { useState } from "react";
import Sidebar from "./Sidebar";
import Header from "./Header";
import SearchBar from "./searchBar";
import Dashboard from "./Dashboard";
import ReviewsList from "./ReviewsList";
import "./App.css";

function App() {
  const [product, setProduct] = useState(null);

  return (
    <>
      <Sidebar />

      <div
        className="app"
        style={{
          marginLeft: "250px",
          padding: "20px",
        }}
      >
        <Header />

        <div id="search">
          <SearchBar setProduct={setProduct} />
        </div>

        {product && (
          <div id="dashboard">
            <Dashboard product={product} />
          </div>
        )}

        {product && (
          <div id="reviews">
            <ReviewsList product={product} />
          </div>
        )}
      </div>
    </>
  );
}

export default App;