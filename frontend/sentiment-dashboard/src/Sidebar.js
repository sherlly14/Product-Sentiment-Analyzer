import React from "react";
import "./Sidebar.css";

function Sidebar() {

  const scrollToSection = (id) => {
    const section = document.getElementById(id);

    if (section) {
      section.scrollIntoView({
        behavior: "smooth"
      });
    }
  };

  return (
    <div className="sidebar">
      <h2 className="logo">📊 PSA</h2>

      <ul className="menu">

        <li onClick={() => scrollToSection("dashboard")}>
          🏠 Dashboard
        </li>

        <li onClick={() => scrollToSection("search")}>
          🔍 Search
        </li>

        <li onClick={() => scrollToSection("reviews")}>
          📝 Reviews
        </li>

        <li onClick={() => scrollToSection("dashboard")}>
          📈 Analytics
        </li>

      </ul>
    </div>
  );
}

export default Sidebar;