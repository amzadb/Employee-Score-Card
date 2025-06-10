import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./UserPage.css";

function UserPage({ user, modules, loading }) {
    const [userInput, setUserInput] = useState("");
    const [dateInput, setDateInput] = useState("");
    const [description, setDescription] = useState("");
    const [file, setFile] = useState(null);

    const [errors, setErrors] = useState({});
    const navigate = useNavigate();
    //Empty comment
    const validateForm = () => {
        const newErrors = {};
        if (!userInput.trim()) newErrors.userInput = "Enter The Activity Type.";
        if (!dateInput) newErrors.dateInput = "Enter Date and time.";
        if (!description.trim()) newErrors.description = "Enter The Description.";
        return newErrors;
    };

    const handleSubmit = () => {
        const formErrors = validateForm();
        if (Object.keys(formErrors).length > 0) {
            setErrors(formErrors);
            return;
        }
        const formData = {
            userInput,
            dateInput,
            description,
            fileName: file?.name || "",
        };
        navigate("/userdetails", { state: formData });
    };
    return (
        <div className="user-page-container">
            <div className="sidebar">
                <h3>Modules</h3>
                {loading ? (
                    <p>Loading modules...</p>
                ) : (
                    modules.map((mod) => (
                        <div key={mod.id} className="module-box">
                            {mod.name}
                        </div>
                    ))
                )}
            </div>

            <div className="main-content">
                <div className="user-profile">
                    <span className="user-name">Welcome {user.name}</span>
                </div><br />

                <div className="userSucessfullyLogin">
                    Welcome {user.name}! You have successfully logged in.
                </div>

                <div className="input-section">
                    <label htmlFor="userInput">Enter Your Activities:</label>
                    <input type="text" id="userInput" value={userInput} onChange={(e) => setUserInput(e.target.value)} className="input-box" />
                    {errors.userInput && <p className="error-text">{errors.userInput}</p>}
                    <label htmlFor="dateInput">Select Date and Time:</label>
                    <input type="datetime-local" id="dateInput" value={dateInput} onChange={(e) => setDateInput(e.target.value)} className="input-box" />
                    {errors.dateInput && <p className="error-text">{errors.dateInput}</p>}
                    <label htmlFor="description">Description:</label>
                    <textarea id="description" rows="5" value={description} onChange={(e) => setDescription(e.target.value)} className="input-box" />
                    {errors.description && <p className="error-text">{errors.description}</p>}
                    <label htmlFor="fileInput">Attach a file:</label>
                    <input type="file" id="fileInput" onChange={(e) => setFile(e.target.files[0])} className="input-box" />
                    {file && <p className="file-info">Selected File: {file.name}</p>}
                    <button className="submit-button" onClick={handleSubmit}>Submit</button>
                </div>
            </div>
        </div>
    );
}

export default UserPage;
