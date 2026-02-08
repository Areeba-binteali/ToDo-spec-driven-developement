from fastapi import APIRouter
from sqlmodel import select
from ..database import get_session
from ..models.user import User
from typing import Dict

router = APIRouter()

@router.get("/health")
async def health_check():
    """Health check endpoint to verify the application is running"""
    try:
        # Test database connection by attempting a simple query
        session_gen = get_session()
        session = next(session_gen)

        # Attempt to query the User table (just check if it's accessible)
        statement = select(User).limit(1)
        result = session.exec(statement)

        # If we get here, the database connection is working
        return {
            "status": "healthy",
            "database": "connected",
            "message": "Application is running normally"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "message": f"Database connection failed: {str(e)}"
        }