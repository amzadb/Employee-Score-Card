from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, Date, Numeric, Enum
from sqlalchemy.sql import func
from . import Base
import enum

class ApprovalStatus(str, enum.Enum):
    pending_manager_approval = "Pending Manager Approval"
    approved_by_manager = "Approved by Manager"
    pending_business_head_approval = "Pending Business Head Approval"
    approved = "Approved"
    rejected = "Rejected"

class ActivitySubmission(Base):
    __tablename__ = "activity_submissions"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    activity_type_id = Column(Integer, ForeignKey("activity_types.id", ondelete="RESTRICT"), nullable=False)
    submission_date = Column(Date, nullable=False)
    description = Column(Text, nullable=False)
    proof_link = Column(String(500), nullable=True)
    submitted_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    current_status = Column(Enum(ApprovalStatus), default=ApprovalStatus.pending_manager_approval, nullable=False)
    manager_id_approver = Column(Integer, ForeignKey("users.id"), nullable=True)
    manager_approval_at = Column(TIMESTAMP(timezone=True), nullable=True)
    manager_comments = Column(Text, nullable=True)
    business_head_id_approver = Column(Integer, ForeignKey("users.id"), nullable=True)
    business_head_approval_at = Column(TIMESTAMP(timezone=True), nullable=True)
    business_head_comments = Column(Text, nullable=True)
    awarded_points = Column(Numeric(10, 2), default=0.00, nullable=False)