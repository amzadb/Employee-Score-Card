from sqlalchemy.orm import Session
from .models.activity_submission import ActivitySubmission, ApprovalStatus

def get_activity_submissions(db: Session):
    return db.query(ActivitySubmission).all()

def get_activity_submission_by_id(db: Session, submission_id: int):
    return db.query(ActivitySubmission).filter(ActivitySubmission.id == submission_id).first()

def create_activity_submission(db: Session, employee_id: int, activity_type_id: int, submission_date: str, description: str, proof_link: str = None):
    new_submission = ActivitySubmission(
        employee_id=employee_id,
        activity_type_id=activity_type_id,
        submission_date=submission_date,
        description=description,
        proof_link=proof_link
    )
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)
    return new_submission

def update_activity_submission_status(db: Session, submission_id: int, status: ApprovalStatus, approver_id: int, comments: str, is_manager: bool):
    submission = db.query(ActivitySubmission).filter(ActivitySubmission.id == submission_id).first()
    if submission:
        submission.current_status = status
        if is_manager:
            submission.manager_id_approver = approver_id
            submission.manager_approval_at = func.now()
            submission.manager_comments = comments
        else:
            submission.business_head_id_approver = approver_id
            submission.business_head_approval_at = func.now()
            submission.business_head_comments = comments
        db.commit()
        db.refresh(submission)
    return submission

def delete_activity_submission(db: Session, submission_id: int):
    submission = db.query(ActivitySubmission).filter(ActivitySubmission.id == submission_id).first()
    if submission:
        db.delete(submission)
        db.commit()
        return True
    return False