import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => (
  <nav className="flex justify-between items-center px-6 py-4 bg-blue-600 text-white">
    <div className="text-xl font-bold">Society Management</div>
    <div>
      <Link to="/" className="mr-4 hover:underline">
        Home
      </Link>
      <Link to="/login" className="hover:underline">
        Login
      </Link>
    </div>
  </nav>
);

export default Navbar;
