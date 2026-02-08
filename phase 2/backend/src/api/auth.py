from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlmodel import Session
from typing import Optional
from datetime import timedelta
from ..database import get_session
from ..models.user import User, UserCreate, UserRead
from ..services.user_service import UserService
from ..middleware.auth import create_access_token, get_current_active_user
from jose import jwt
import uuid

router = APIRouter()

@router.post("/register", response_model=UserRead)
def register(user_create: UserCreate, session: Session = Depends(get_session)):
    """Register a new user"""
    user_service = UserService(session)

    # Check if user already exists
    existing_user = user_service.get_by_email(user_create.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    # Create new user
    new_user = user_service.create_user(user_create)
    return new_user

@router.post("/login")
async def login(request: Request, session: Session = Depends(get_session)):
    """Login a user and return access token"""
    # Parse email and password from request body
    body = await request.json()
    email = body.get("email")
    password = body.get("password")

    if not email or not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email and password required"
        )

    user_service = UserService(session)
    user = user_service.authenticate_user(email, password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email
        }
    }

@router.post("/logout")
async def logout(current_user: dict = Depends(get_current_active_user)):
    """Logout the current user"""
    # In a real implementation, you might invalidate the token
    # For now, we just return a success message
    return {"message": "Logged out successfully"}