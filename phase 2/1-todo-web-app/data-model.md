# Data Model: Todo Full-Stack Web Application

## User Entity

**Fields:**
- id: UUID (primary key, auto-generated)
- email: String (unique, required, validated as email format)
- password_hash: String (required, hashed using industry-standard algorithm)
- created_at: DateTime (auto-generated)
- updated_at: DateTime (auto-generated, updated on modification)

**Validation Rules:**
- Email must be unique across all users
- Email must match standard email format
- Password must meet strength requirements (defined in auth system)

**Relationships:**
- One-to-many with Todo items (user owns multiple todos)

## Todo Entity

**Fields:**
- id: UUID (primary key, auto-generated)
- title: String (required, max 255 characters)
- description: String (optional, max 1000 characters)
- completed: Boolean (default false)
- user_id: UUID (foreign key referencing User.id, required)
- created_at: DateTime (auto-generated)
- updated_at: DateTime (auto-generated, updated on modification)

**Validation Rules:**
- Title must not be empty
- User_id must reference an existing user
- Completed status can be toggled by the owning user

**State Transitions:**
- New todo: completed = false
- Toggle completion: completed = !completed
- Deletion: removes the record entirely

## Session Entity (Implicit in Better Auth)

**Fields:**
- id: UUID (primary key, auto-generated)
- user_id: UUID (foreign key referencing User.id, required)
- expires_at: DateTime (required, auto-calculated)
- created_at: DateTime (auto-generated)

**Validation Rules:**
- Session must be associated with a valid user
- Session must not be expired when accessed

## Relationships

**User → Todo (One-to-Many)**
- A user can own multiple todo items
- Todos are filtered by user_id for data isolation
- When a user is deleted, their todos should also be deleted (cascade delete)

**User → Session (One-to-Many)**
- A user can have multiple active sessions
- Sessions are validated during API authentication
- Sessions are invalidated on logout