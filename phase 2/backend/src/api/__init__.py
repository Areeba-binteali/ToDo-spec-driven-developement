from fastapi import APIRouter

# Main API router
api_router = APIRouter()

# Import and include other routers
from . import auth, todos, health
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(todos.router, prefix="/todos", tags=["todos"])
api_router.include_router(health.router, prefix="/health", tags=["health"])