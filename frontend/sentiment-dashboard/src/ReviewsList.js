import React from 'react';

function ReviewsList({ product }) {
  if (!product) return null;

  const reviews = product.reviews;

  const getColor = (sentiment) => {
    if (sentiment === 'Positive') return '#2ecc71';
    if (sentiment === 'Negative') return '#e74c3c';
    return '#f39c12';
  };

  return (
    <div style={styles.container}>
      <h2>📝 Reviews</h2>

      {reviews.length === 0 && <p>No reviews found.</p>}

      {reviews.map((review) => (
        <div
          key={review.id}
          style={{
            ...styles.card,
            borderLeft: `5px solid ${getColor(review.sentiment)}`
          }}
        >
          <p style={{ fontWeight: 'bold', marginBottom: '4px' }}>{review.user}</p>
          <p style={styles.text}>{review.text}</p>

          <span
            style={{
              ...styles.badge,
              background: getColor(review.sentiment)
            }}
          >
            {review.sentiment.toUpperCase()}
          </span>
        </div>
      ))}
    </div>
  );
}

const styles = {
  container: {
    background: 'white',
    borderRadius: '15px',
    padding: '25px',
    boxShadow: '0 2px 10px rgba(0,0,0,0.1)'
  },
  card: {
    padding: '15px',
    marginBottom: '15px',
    borderRadius: '8px',
    background: '#f9f9f9'
  },
  text: {
    fontSize: '0.95rem',
    color: '#333',
    marginBottom: '8px'
  },
  badge: {
    padding: '4px 12px',
    borderRadius: '20px',
    color: 'white',
    fontSize: '0.75rem',
    fontWeight: 'bold'
  }
};

export default ReviewsList;