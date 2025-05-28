from sqlalchemy.orm import Session
from .models.activity_type import ActivityType

def get_activity_types(db: Session):
    return db.query(ActivityType).all()

def get_activity_type_by_id(db: Session, activity_type_id: int):
    return db.query(ActivityType).filter(ActivityType.id == activity_type_id).first()

def create_activity_type(db: Session, name: str, points: float, description: str = None, is_active: bool = True):
    new_activity_type = ActivityType(
        name=name,
        points=points,
        description=description,
        is_active=is_active
    )
    db.add(new_activity_type)
    db.commit()
    db.refresh(new_activity_type)
    return new_activity_type

def update_activity_type(db: Session, activity_type_id: int, name: str = None, points: float = None, description: str = None, is_active: bool = None):
    activity_type = db.query(ActivityType).filter(ActivityType.id == activity_type_id).first()
    if activity_type:
        if name:
            activity_type.name = name
        if points is not None:
            activity_type.points = points
        if description is not None:
            activity_type.description = description
        if is_active is not None:
            activity_type.is_active = is_active
        db.commit()
        db.refresh(activity_type)
    return activity_type

def delete_activity_type(db: Session, activity_type_id: int):
    activity_type = db.query(ActivityType).filter(ActivityType.id == activity_type_id).first()
    if activity_type:
        db.delete(activity_type)
        db.commit()
        return True
    return False