import React, { useState } from 'react';
import SearchBar from './searchBar';
import Dashboard from './Dashboard';
import ReviewsList from './ReviewsList';
import './App.css';

function App() {
  const [product, setProduct] = useState(null);

  return (
    <div className="app">
      <h1 style={{
  textAlign: 'center',
  fontSize: '2.5rem',
  fontWeight: 'bold',
  color: '#2c3e50',
  marginBottom: '30px',
  marginTop: '20px'
}}>
  📊 Product Sentiment Analyzer
</h1>
      <SearchBar setProduct={setProduct} />
      {product && <Dashboard product={product} />}
      {product && <ReviewsList product={product} />}
    </div>
  );
}

export default App;