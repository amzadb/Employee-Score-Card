import { useLocation } from "react-router-dom";

function UserDetails() {
const { state } = useLocation();
//No Data
if (!state) return <p>No data submitted.</p>;

return (
    <div className="main-content">
    <h2>Submitted Data</h2>
    <p><strong>Activity:</strong> {state.userInput}</p>
    <p><strong>Date/Time:</strong> {state.dateInput}</p>
    <p><strong>Description:</strong> {state.description}</p>
    <p><strong>Attached File:</strong> {state.fileName}</p>
    </div>
);
}

export default UserDetails;
