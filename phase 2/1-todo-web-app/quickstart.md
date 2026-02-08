# Quickstart Guide: Todo Full-Stack Web Application

## Prerequisites

- Node.js 18+ for frontend development
- Python 3.11+ for backend development
- PostgreSQL-compatible database (Neon recommended)
- Better Auth account or self-hosted instance
- Environment variables configured (see below)

## Environment Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Set up environment variables:
   ```bash
   # Backend (.env)
   DATABASE_URL="postgresql://username:password@localhost:5432/todo_app"
   BETTER_AUTH_SECRET="your-secret-key-here"

   # Frontend (.env.local)
   NEXT_PUBLIC_API_BASE_URL="http://localhost:8000/api"
   ```

3. Install dependencies:
   ```bash
   # Backend
   cd backend
   pip install -r requirements.txt

   # Frontend
   cd ../frontend
   npm install
   ```

## Running the Application

### Backend (FastAPI)
```bash
cd backend
python -m uvicorn src.main:app --reload --port 8000
```

### Frontend (Next.js)
```bash
cd frontend
npm run dev
```

The application will be available at `http://localhost:3000`

## Database Setup

1. Ensure your PostgreSQL database is running
2. Run the initial migration:
   ```bash
   cd backend
   python -m src.database.migrate
   ```

## API Endpoints

All API endpoints require JWT authentication in the Authorization header:
```
Authorization: Bearer <jwt-token>
```

Available endpoints:
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Authenticate user and get token
- `POST /auth/logout` - Invalidate user session
- `GET /todos` - Get user's todo list
- `POST /todos` - Create a new todo
- `PUT /todos/{id}` - Update a todo
- `DELETE /todos/{id}` - Delete a todo

## Development Commands

### Backend
- Run tests: `pytest tests/`
- Format code: `black src/`
- Check types: `mypy src/`

### Frontend
- Run tests: `npm test`
- Build for production: `npm run build`
- Lint code: `npm run lint`

## Troubleshooting

- If you encounter database connection issues, verify your `DATABASE_URL` is correct
- For authentication problems, ensure `BETTER_AUTH_SECRET` is the same for both frontend and backend
- If the frontend can't connect to the backend, check that both are running and CORS is configured