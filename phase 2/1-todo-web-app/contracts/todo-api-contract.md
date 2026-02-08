# API Contract: Todo Full-Stack Web Application

## Authentication Endpoints

### POST /api/auth/register
Register a new user account.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (201 Created):**
```json
{
  "user_id": "uuid-string",
  "email": "user@example.com",
  "created_at": "2026-01-28T12:00:00Z"
}
```

**Response (400 Bad Request):**
```json
{
  "error": "Invalid email format or weak password"
}
```

**Response (409 Conflict):**
```json
{
  "error": "Email already registered"
}
```

### POST /api/auth/login
Authenticate user and return JWT token.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (200 OK):**
```json
{
  "token": "jwt-token-string",
  "user": {
    "id": "uuid-string",
    "email": "user@example.com"
  }
}
```

**Response (401 Unauthorized):**
```json
{
  "error": "Invalid credentials"
}
```

### POST /api/auth/logout
Invalidate user session.

**Headers:**
```
Authorization: Bearer {jwt-token}
```

**Response (200 OK):**
```json
{
  "message": "Logged out successfully"
}
```

## Todo Management Endpoints

### GET /api/todos
Retrieve the authenticated user's todo list.

**Headers:**
```
Authorization: Bearer {jwt-token}
```

**Response (200 OK):**
```json
{
  "todos": [
    {
      "id": "uuid-string",
      "title": "Sample todo",
      "description": "Optional description",
      "completed": false,
      "user_id": "uuid-string",
      "created_at": "2026-01-28T12:00:00Z",
      "updated_at": "2026-01-28T12:00:00Z"
    }
  ]
}
```

### POST /api/todos
Create a new todo item.

**Headers:**
```
Authorization: Bearer {jwt-token}
```

**Request:**
```json
{
  "title": "New todo",
  "description": "Optional description"
}
```

**Response (201 Created):**
```json
{
  "id": "uuid-string",
  "title": "New todo",
  "description": "Optional description",
  "completed": false,
  "user_id": "uuid-string",
  "created_at": "2026-01-28T12:00:00Z",
  "updated_at": "2026-01-28T12:00:00Z"
}
```

### PUT /api/todos/{id}
Update an existing todo item.

**Headers:**
```
Authorization: Bearer {jwt-token}
```

**Request:**
```json
{
  "title": "Updated todo",
  "description": "Updated description",
  "completed": true
}
```

**Response (200 OK):**
```json
{
  "id": "uuid-string",
  "title": "Updated todo",
  "description": "Updated description",
  "completed": true,
  "user_id": "uuid-string",
  "created_at": "2026-01-28T12:00:00Z",
  "updated_at": "2026-01-28T12:05:00Z"
}
```

### DELETE /api/todos/{id}
Delete a todo item.

**Headers:**
```
Authorization: Bearer {jwt-token}
```

**Response (200 OK):**
```json
{
  "message": "Todo deleted successfully"
}
```

## Error Format

All error responses follow this format:
```json
{
  "error": "Descriptive error message",
  "code": "ERROR_CODE"
}
```

Common error codes:
- `VALIDATION_ERROR`: Request data doesn't meet validation requirements
- `AUTHENTICATION_ERROR`: Missing or invalid authentication
- `AUTHORIZATION_ERROR`: User lacks permission for the action
- `NOT_FOUND`: Requested resource doesn't exist
- `INTERNAL_ERROR`: Unexpected server error