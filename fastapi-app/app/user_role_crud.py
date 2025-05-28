from sqlalchemy.orm import Session
from .models.user_role import UserRole

def get_user_roles(db: Session):
    return db.query(UserRole).all()

def get_roles_by_user_id(db: Session, user_id: int):
    return db.query(UserRole).filter(UserRole.user_id == user_id).all()

def get_users_by_role_id(db: Session, role_id: int):
    return db.query(UserRole).filter(UserRole.role_id == role_id).all()

def assign_role_to_user(db: Session, user_id: int, role_id: int):
    user_role = UserRole(user_id=user_id, role_id=role_id)
    db.add(user_role)
    db.commit()
    db.refresh(user_role)
    return user_role

def remove_role_from_user(db: Session, user_id: int, role_id: int):
    user_role = db.query(UserRole).filter(UserRole.user_id == user_id, UserRole.role_id == role_id).first()
    if user_role:
        db.delete(user_role)
        db.commit()
        return True
    return False