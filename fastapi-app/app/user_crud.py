from sqlalchemy.orm import Session
from .models.user import User

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_employee_id(db: Session, employee_id: str):
    return db.query(User).filter(User.employee_id == employee_id).first()

def create_user(db: Session, employee_id: str, first_name: str, last_name: str, email: str, manager_id: int = None):
    new_user = User(
        employee_id=employee_id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        manager_id=manager_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db: Session, user_id: int, first_name: str = None, last_name: str = None, email: str = None, is_active: bool = None):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        if is_active is not None:
            user.is_active = is_active
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False