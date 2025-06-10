import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import AdminDashboard from "./pages/AdminDashboard";
// import ManagerDashboard from "./pages/ManagerDashboard";
// import BusinessHeadDashboard from "./pages/BusinessHeadDashboard";
// import UserDashboard from "./pages/UserDashboard";
import LoginPage from "./pages/LoginPage";
import UserPage from './pages/UserPage';
import UserDetails from "./pages/userdetails";

function App() {
   const dummyUser = { name: "Dhanush Chalamcharla" };
  const dummyModules = [
    { id: 1, name: "DashBoard" },
    { id: 2, name: "Module 2" },
  ];
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <Routes>
          <Route path="/" element={<LoginPage />} />
           <Route
            path="/UserPage"
            element={<UserPage user={dummyUser} modules={dummyModules} loading={false} />}
          />
          <Route path="/userdetails" element={<UserDetails />} />
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