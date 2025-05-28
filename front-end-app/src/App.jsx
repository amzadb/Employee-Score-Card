import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import AdminDashboard from "./pages/AdminDashboard";
// import ManagerDashboard from "./pages/ManagerDashboard";
// import BusinessHeadDashboard from "./pages/BusinessHeadDashboard";
// import UserDashboard from "./pages/UserDashboard";
import LoginPage from "./pages/LoginPage";

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <Routes>
          <Route path="/" element={<LoginPage />} />
          {/* <Route path="/admin" element={<AdminDashboard />} />
          <Route path="/manager" element={<ManagerDashboard />} />
          <Route path="/business-head" element={<BusinessHeadDashboard />} />
          <Route path="/user" element={<UserDashboard />} /> */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;