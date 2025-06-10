import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function LoginPage() {
  const [employeeId, setEmployeeId] = useState("");
  const [roles, setRoles] = useState([]);
  const [selectedRole, setSelectedRole] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    setRoles([]);
    setSelectedRole("");

    try {
      // Check if the employee exists
      const userResponse = await axios.get(`http://localhost:8000/users/by-employee-id/${employeeId}`);
      const user = userResponse.data;

      if (!user) {
        setError("Employee ID not found.");
        return;
      }

      // Fetch user roles
      const rolesResponse = await axios.get(`http://localhost:8000/user_roles/user/${user.id}`);
      const rolesData = rolesResponse.data;

      if (rolesData.length === 0) {
        setError("No roles assigned to this user.");
        return;
      }

      // If multiple roles, display dropdown
      if (rolesData.length > 1) {
        setRoles(rolesData);
      } else {
        // If only one role, redirect directly
        redirectToDashboard(rolesData[0].role_id);
      }
    } catch (err) {
      console.error(err);
      setError("An error occurred while logging in.");
    }
  };

  const redirectToDashboard = (roleId) => {
    if (roleId === 1) {
      navigate("/admin"); // Admin role
    } else if (roleId === 2) {
      navigate("/manager"); // Manager role
    } else if (roleId === 3) {
      navigate("/business-head"); // Business Head role
    } else {
      navigate("/user"); // Default to User role
    }
  };

  const handleRoleSelection = (e) => {
    setSelectedRole(e.target.value);
  };

  const handleRoleSubmit = () => {
    if (selectedRole) {
      redirectToDashboard(parseInt(selectedRole));
    } else {
      setError("Please select a role.");
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold mb-4 text-center">Login</h1>
        <form onSubmit={handleLogin}>
          <div className="mb-4">
            <label htmlFor="employeeId" className="block text-sm font-medium text-gray-700">
              Employee ID
            </label>
            <input
              type="text"
              id="employeeId"
              value={employeeId}
              onChange={(e) => setEmployeeId(e.target.value)}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
              required
            />
          </div>
          {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
         <button
  type="submit"
  className="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
>
  Login
</button>
  <button
      style={{ marginLeft: '12px' }}
      onClick={() => navigate('/UserPage')}
    >
      Skip
    </button>

        </form>

        {roles.length > 0 && (
          <div className="mt-6">
            <label htmlFor="roles" className="block text-sm font-medium text-gray-700">
              Select Role
            </label>
            <select
              id="roles"
              value={selectedRole}
              onChange={handleRoleSelection}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
            >
              <option value="">-- Select a Role --</option>
              {roles.map((role) => (
                <option key={role.role_id} value={role.role_id}>
                  {role.role_name}
                </option>
              ))}
            </select>
            <button
              onClick={handleRoleSubmit}
              className="mt-4 w-full bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
            >
              Proceed
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default LoginPage;