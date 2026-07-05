import React from 'react';
import { PieChart, Pie, Cell, Tooltip, Legend, BarChart, Bar, XAxis, YAxis, CartesianGrid } from 'recharts';

const COLORS = { Positive: '#2ecc71', Negative: '#e74c3c', Neutral: '#f39c12' };

function Dashboard({ product }) {
  if (!product) return null;

  const pieData = product.sentimentData;
  const barData = product.ratingData;

 return (
  <div style={styles.container}>
    <h2>📊 Sentiment Analysis - {product.name}</h2>

    {/* Summary Cards */}
    <div style={styles.cards}>
      <div style={{ ...styles.card, borderTop: "5px solid #3498db" }}>
        <h4>⭐ Rating</h4>
        <h2>{product.rating}/5</h2>
      </div>

      <div style={{ ...styles.card, borderTop: "5px solid #2ecc71" }}>
        <h4>😊 Positive</h4>
        <h2>{pieData[0]?.value}%</h2>
      </div>

      <div style={{ ...styles.card, borderTop: "5px solid #f39c12" }}>
        <h4>😐 Neutral</h4>
        <h2>{pieData[2]?.value}%</h2>
      </div>

      <div style={{ ...styles.card, borderTop: "5px solid #e74c3c" }}>
        <h4>😞 Negative</h4>
        <h2>{pieData[1]?.value}%</h2>
      </div>
    </div>

    {/* Charts */}
    <div style={styles.charts}>
      <PieChart width={350} height={300}>
        <Pie
          data={pieData}
          cx={175}
          cy={150}
          outerRadius={100}
          dataKey="value"
          label
        >
          {pieData.map((entry, index) => (
            <Cell key={index} fill={COLORS[entry.name]} />
          ))}
        </Pie>

        <Tooltip />
        <Legend />
      </PieChart>

      <BarChart width={400} height={300} data={barData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="rating" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count" fill="#3498db" />
      </BarChart>
    </div>
  </div>
);
}

const styles = {
  container: {
    background: "white",
    borderRadius: "15px",
    padding: "25px",
    marginBottom: "25px",
    boxShadow: "0 2px 10px rgba(0,0,0,0.1)"
  },

  cards: {
    display: "grid",
    gridTemplateColumns: "repeat(4,1fr)",
    gap: "20px",
    marginTop: "25px",
    marginBottom: "25px"
  },

  card: {
    background: "#fff",
    padding: "20px",
    borderRadius: "12px",
    textAlign: "center",
    boxShadow: "0 3px 10px rgba(0,0,0,.1)"
  },

  charts: {
    display: "flex",
    gap: "20px",
    flexWrap: "wrap",
    justifyContent: "center",
    marginTop: "20px"
  }
};



export default Dashboard;