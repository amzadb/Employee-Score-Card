from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .role import Role  # Import Role model
from .user import User  # Import User model
from .user_role import UserRole  # Import UserRole model
from .activity_type import ActivityType  # Import ActivityType model
from .activity_submission import ActivitySubmission  # Import ActivitySubmission model