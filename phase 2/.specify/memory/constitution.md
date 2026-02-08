<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.0
Modified principles: None (new constitution)
Added sections: All core principles, constraints, workflow, governance
Removed sections: None
Templates requiring updates: ✅ .specify/templates/plan-template.md, ✅ .specify/templates/spec-template.md, ✅ .specify/templates/tasks-template.md
Follow-up TODOs: None
-->
# Todo Full-Stack Web Application Constitution

## Core Principles

### I. Spec-First Development
All implementation must be preceded by an approved specification document; No code implementation without corresponding spec under /specs/**; Features must map directly to approved specifications.

### II. End-to-End Consistency
Maintain strict consistency across frontend, backend, API, and database layers; All components must adhere to the same data models and business logic; Cross-layer validation required before deployment.

### III. User Data Security and Isolation
Implement zero-trust security model for user data; Enforce strict user data isolation with proper authentication and authorization; All user data access must be filtered by authenticated user ID.

### IV. Zero Manual Coding Constraint
All code generation must be performed via Claude Code or designated automated tools; Manual coding is prohibited except for initial setup; Maintain full automation of implementation pipeline.

### V. Production-Minded Architecture
Design all components with production readiness in mind; Implement stateless, scalable architecture patterns; Follow cloud-native best practices for deployment and scaling.

### VI. JWT-Protected API Access
All REST APIs must be fully protected with JWT authentication; Require Authorization: Bearer <token> header for all protected endpoints; Enforce proper authentication before any data access.

## Additional Constraints

Technology stack requirements:
- Frontend: Next.js 16+ (App Router, TypeScript, Tailwind)
- Backend: FastAPI (Python) with SQLModel for database access
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth with JWT tokens
- Shared JWT secret via BETTER_AUTH_SECRET environment variable

API requirements:
- All endpoints under `/api/`
- No endpoint accessible without valid JWT
- User identity derived from JWT, not request body
- Task ownership enforced on every CRUD operation
- Proper HTTP status codes required (401, 403, 404, 422)

Database requirements:
- Database access must use SQLModel only (no raw SQL)
- All task data must be filtered by authenticated user ID
- Backend must never trust client-provided user_id without JWT verification

## Development Workflow

Workflow stages:
1. Read and validate relevant specs under /specs/**
2. Generate implementation plan using Claude Code
3. Break plan into atomic tasks
4. Implement via Claude Code only
5. Review against acceptance criteria
6. Update specs if behavior changes

Quality gates:
- All features must satisfy matching spec acceptance criteria
- Complete backend + frontend implementation required
- All implementations must reference relevant specs using @specs/ paths
- Centralized API client required for all backend calls on frontend
- Authentication handled exclusively via Better Auth + JWT

Review requirements:
- All pull requests must verify compliance with constitution principles
- Automated validation of JWT protection on all endpoints
- Verification of user data isolation in database queries
- Confirmation that no manual coding occurred during implementation

## Governance

This constitution supersedes all other development practices and guidelines; All amendments must be documented with approval from project stakeholders; Any changes to core principles require a migration plan for existing codebase; All development activities must comply with these principles.

All pull requests and code reviews must verify constitutional compliance; Complexity must be justified with clear business value; Use this constitution as the primary guidance document for all development decisions; Regular compliance audits should be conducted to ensure adherence.

**Version**: 1.1.0 | **Ratified**: 2026-01-28 | **Last Amended**: 2026-01-28
