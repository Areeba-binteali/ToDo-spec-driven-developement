# Todo Full-Stack Web Application - Phase II

This is Phase II of the Evolution of Todo project - a full-stack web application with user authentication, persistent storage, and a responsive UI built using Spec-Driven Development with Claude Code and Spec-Kit Plus.

## Overview

This is Phase II of the Evolution of Todo project - a full-stack web application that allows multiple users to manage their personal todo lists with persistent storage and authentication. The application features user registration, authentication, and data isolation.

## Features

- User registration and authentication
- Secure JWT-based authentication
- Create, read, update, and delete todo items
- User data isolation (users can only access their own todos)
- Responsive web interface
- Data persistence with Neon PostgreSQL

## Tech Stack

- **Frontend**: Next.js 16+, TypeScript, Tailwind CSS
- **Backend**: FastAPI (Python), SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: JWT tokens with industry-standard security

## Prerequisites

- Node.js 18+
- Python 3.11+
- PostgreSQL-compatible database (Neon recommended)

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Set up the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
4. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Database Configuration
DATABASE_URL="postgresql://username:password@localhost:5432/todo_app"

# Authentication Configuration
BETTER_AUTH_SECRET="your-super-secret-key-here"
BETTER_AUTH_URL="http://localhost:3000"

# API Configuration
NEXT_PUBLIC_API_BASE_URL="http://localhost:8000/api/v1"
```

## Running the Application

### Backend

```bash
cd backend
python -m src.main
```

The backend will be available at `http://localhost:8000`

### Frontend

```bash
cd frontend
npm run dev
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

All API endpoints are prefixed with `/api/v1`

### Authentication

- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Login and get JWT token
- `POST /api/v1/auth/logout` - Logout

### Todo Management

- `GET /api/v1/todos` - Get user's todos
- `POST /api/v1/todos` - Create a new todo
- `PUT /api/v1/todos/{id}` - Update a todo
- `DELETE /api/v1/todos/{id}` - Delete a todo

### Health Check

- `GET /health` - Health check endpoint

## Security

- All endpoints (except auth/register and auth/login) require a valid JWT token in the Authorization header
- User data is isolated - users can only access their own todos
- Passwords are hashed using bcrypt
- Input validation is performed on both frontend and backend

## Architecture

The application follows a monorepo structure with separate frontend and backend directories:

```
backend/
├── src/
│   ├── models/     # Database models
│   ├── services/   # Business logic
│   ├── api/        # API routes
│   ├── database/   # Database configuration
│   └── middleware/ # Middleware (authentication, etc.)
└── requirements.txt

frontend/
├── src/
│   ├── components/ # React components
│   ├── pages/      # Next.js pages
│   └── services/   # Client-side services
└── package.json
```

## Development

The project was developed using the Agentic Dev Stack workflow:
1. Write spec → Generate plan → Break into tasks → Implement via Claude Code
2. No manual coding was performed; all implementation was done through Claude Code
3. Follows the principles defined in the project constitution

## Phase I Evolution

This implementation evolved from Phase I (an in-memory CLI Todo application) to a full-stack, database-backed web application while maintaining the same core functionality and extending it with user management and data persistence.