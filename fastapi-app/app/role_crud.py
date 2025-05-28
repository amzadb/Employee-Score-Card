from sqlalchemy.orm import Session
from .models.role import Role

def get_roles(db: Session):
    return db.query(Role).all()

def get_role_by_id(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()

def create_role(db: Session, role_name: str):
    new_role = Role(role_name=role_name)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def update_role(db: Session, role_id: int, role_name: str):
    role = db.query(Role).filter(Role.id == role_id).first()
    if role:
        role.role_name = role_name
        db.commit()
        db.refresh(role)
    return role

def delete_role(db: Session, role_id: int):
    role = db.query(Role).filter(Role.id == role_id).first()
    if role:
        db.delete(role)
        db.commit()
        return True
    return False