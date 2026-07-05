import React from "react";
import "./Header.css";

function Header() {
  return (
    <div className="header">
      <div>
        <h1>Welcome 👋</h1>
        <p>Analyze customer reviews using AI sentiment analysis.</p>
      </div>

      <div className="header-icons">
        🔔
        ⚙️
      </div>
    </div>
  );
}

export default Header;