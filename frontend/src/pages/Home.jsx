import React from "react";
import { Link } from "react-router-dom";

const Home = () => (
  <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 text-gray-900">
    <h1 className="text-4xl font-bold mb-4">Welcome to Society Management</h1>
    <p className="text-lg mb-6">Manage your society efficiently!</p>
    <Link to="/login">
      <button className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
        Login
      </button>
    </Link>
  </div>
);

export default Home;
