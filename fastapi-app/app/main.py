from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base
from fastapi.middleware.cors import CORSMiddleware

# Import CRUD operations
from .role_crud import (
    get_roles, get_role_by_id, create_role, update_role, delete_role
)

from .user_crud import (
    get_users, get_user_by_id, get_user_by_employee_id, create_user, update_user, delete_user
)

from .user_role_crud import (
    get_user_roles, get_roles_by_user_id, get_users_by_role_id, assign_role_to_user, remove_role_from_user
)

from .activity_type_crud import (
    get_activity_types, get_activity_type_by_id, create_activity_type, update_activity_type, delete_activity_type
)

from .activity_submission_crud import (
    get_activity_submissions, get_activity_submission_by_id, create_activity_submission, update_activity_submission_status, delete_activity_submission
)
from .models.activity_submission import ApprovalStatus

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Endpoints        
@app.get("/roles/")
async def read_roles(db: Session = Depends(get_db)):
    return get_roles(db)

@app.get("/roles/{role_id}")
async def read_role(role_id: int, db: Session = Depends(get_db)):
    role = get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@app.post("/roles/")
async def create_new_role(role_name: str, db: Session = Depends(get_db)):
    return create_role(db, role_name)

@app.put("/roles/{role_id}")
async def update_existing_role(role_id: int, role_name: str, db: Session = Depends(get_db)):
    role = update_role(db, role_id, role_name)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@app.delete("/roles/{role_id}")
async def delete_existing_role(role_id: int, db: Session = Depends(get_db)):
    success = delete_role(db, role_id)
    if not success:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"message": "Role deleted successfully"}

@app.get("/users/")
async def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@app.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/by-employee-id/{employee_id}")
async def get_user(employee_id: str, db: Session = Depends(get_db)):
    user = get_user_by_employee_id(db, employee_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/")
async def create_new_user(employee_id: str, first_name: str, last_name: str, email: str, manager_id: int = None, db: Session = Depends(get_db)):
    return create_user(db, employee_id, first_name, last_name, email, manager_id)

@app.put("/users/{user_id}")
async def update_existing_user(user_id: int, first_name: str = None, last_name: str = None, email: str = None, is_active: bool = None, db: Session = Depends(get_db)):
    user = update_user(db, user_id, first_name, last_name, email, is_active)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}")
async def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    success = delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

@app.get("/user_roles/")
async def read_user_roles(db: Session = Depends(get_db)):
    return get_user_roles(db)

@app.get("/user_roles/user/{user_id}")
async def read_roles_by_user(user_id: int, db: Session = Depends(get_db)):
    roles = get_roles_by_user_id(db, user_id)
    if not roles:
        raise HTTPException(status_code=404, detail="No roles found for the user")
    # Format the response as a list of dictionaries
    return [{"role_id": role.id, "role_name": role.role_name} for role in roles]

@app.get("/user_roles/role/{role_id}")
async def read_users_by_role(role_id: int, db: Session = Depends(get_db)):
    return get_users_by_role_id(db, role_id)

@app.post("/user_roles/")
async def assign_role(user_id: int, role_id: int, db: Session = Depends(get_db)):
    return assign_role_to_user(db, user_id, role_id)

@app.delete("/user_roles/")
async def remove_role(user_id: int, role_id: int, db: Session = Depends(get_db)):
    success = remove_role_from_user(db, user_id, role_id)
    if not success:
        raise HTTPException(status_code=404, detail="User role mapping not found")
    return {"message": "Role removed from user successfully"}

@app.get("/activity_types/")
async def read_activity_types(db: Session = Depends(get_db)):
    return get_activity_types(db)

@app.get("/activity_types/{activity_type_id}")
async def read_activity_type(activity_type_id: int, db: Session = Depends(get_db)):
    activity_type = get_activity_type_by_id(db, activity_type_id)
    if not activity_type:
        raise HTTPException(status_code=404, detail="Activity type not found")
    return activity_type

@app.post("/activity_types/")
async def create_new_activity_type(name: str, points: float, description: str = None, is_active: bool = True, db: Session = Depends(get_db)):
    return create_activity_type(db, name, points, description, is_active)

@app.put("/activity_types/{activity_type_id}")
async def update_existing_activity_type(activity_type_id: int, name: str = None, points: float = None, description: str = None, is_active: bool = None, db: Session = Depends(get_db)):
    activity_type = update_activity_type(db, activity_type_id, name, points, description, is_active)
    if not activity_type:
        raise HTTPException(status_code=404, detail="Activity type not found")
    return activity_type

@app.delete("/activity_types/{activity_type_id}")
async def delete_existing_activity_type(activity_type_id: int, db: Session = Depends(get_db)):
    success = delete_activity_type(db, activity_type_id)
    if not success:
        raise HTTPException(status_code=404, detail="Activity type not found")
    return {"message": "Activity type deleted successfully"}

@app.get("/activity_submissions/")
async def read_activity_submissions(db: Session = Depends(get_db)):
    return get_activity_submissions(db)

@app.get("/activity_submissions/{submission_id}")
async def read_activity_submission(submission_id: int, db: Session = Depends(get_db)):
    submission = get_activity_submission_by_id(db, submission_id)
    if not submission:
        raise HTTPException(status_code=404, detail="Activity submission not found")
    return submission

@app.post("/activity_submissions/")
async def create_new_activity_submission(employee_id: int, activity_type_id: int, submission_date: str, description: str, proof_link: str = None, db: Session = Depends(get_db)):
    return create_activity_submission(db, employee_id, activity_type_id, submission_date, description, proof_link)

@app.put("/activity_submissions/{submission_id}/status")
async def update_activity_submission(submission_id: int, status: ApprovalStatus, approver_id: int, comments: str, is_manager: bool, db: Session = Depends(get_db)):
    submission = update_activity_submission_status(db, submission_id, status, approver_id, comments, is_manager)
    if not submission:
        raise HTTPException(status_code=404, detail="Activity submission not found")
    return submission

@app.delete("/activity_submissions/{submission_id}")
async def delete_activity_submission(submission_id: int, db: Session = Depends(get_db)):
    success = delete_activity_submission(db, submission_id)
    if not success:
        raise HTTPException(status_code=404, detail="Activity submission not found")
    return {"message": "Activity submission deleted successfully"}