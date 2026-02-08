from sqlmodel import Session, select
from typing import Optional
from passlib.context import CryptContext
from ..models.user import User, UserCreate, UserUpdate, validate_email_format, validate_password_strength
import uuid

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, session: Session):
        self.session = session

    def hash_password(self, password: str) -> str:
        """Hash a plain text password"""
        # Truncate password if it exceeds bcrypt's 72-byte limit
        if len(password.encode('utf-8')) > 72:
            password = password.encode('utf-8')[:72].decode('utf-8', errors='ignore')
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a plain password against a hashed password"""
        return pwd_context.verify(plain_password, hashed_password)

    def get_by_email(self, email: str) -> Optional[User]:
        """Get a user by email"""
        statement = select(User).where(User.email == email)
        result = self.session.exec(statement)
        return result.first()

    def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        """Get a user by ID"""
        statement = select(User).where(User.id == user_id)
        result = self.session.exec(statement)
        return result.first()

    def create_user(self, user_create: UserCreate) -> User:
        """Create a new user with validation"""
        # Validate email format
        if not validate_email_format(user_create.email):
            raise ValueError("Invalid email format")

        # Validate password strength
        is_valid, error_msg = validate_password_strength(user_create.password)
        if not is_valid:
            raise ValueError(error_msg)

        # Hash the password
        hashed_password = self.hash_password(user_create.password)

        # Create the user object
        db_user = User(
            email=user_create.email,
            password_hash=hashed_password
        )

        # Add to session and commit
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)

        return db_user

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate a user by email and password"""
        user = self.get_by_email(email)
        if not user or not self.verify_password(password, user.password_hash):
            return None
        return user

    def update_user(self, user_id: uuid.UUID, user_update: UserUpdate) -> Optional[User]:
        """Update a user"""
        db_user = self.get_by_id(user_id)
        if not db_user:
            return None

        # Update fields if provided
        if user_update.email is not None:
            if not validate_email_format(user_update.email):
                raise ValueError("Invalid email format")
            db_user.email = user_update.email

        # Commit changes
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)

        return db_user

    def delete_user(self, user_id: uuid.UUID) -> bool:
        """Delete a user"""
        db_user = self.get_by_id(user_id)
        if not db_user:
            return False

        self.session.delete(db_user)
        self.session.commit()
        return True